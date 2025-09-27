from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, DECIMAL, Text, BigInteger
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database.connection import Base


class Post(Base):
    __tablename__ = "Post"
    
    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey("Users.id"))
    content = Column(Text)
    location = Column(BigInteger, ForeignKey("UserLocation.id"))
    is_active = Column(Boolean, default=True)
    created = Column(DateTime(timezone=True), server_default=func.now())
    updated = Column(DateTime(timezone=True), onupdate=func.now())
    
    user = relationship("Users", back_populates="posts")
    user_location = relationship("UserLocation")
    comments = relationship("Comment", back_populates="post")
    likes = relationship("PostLike", back_populates="post")


class PostLike(Base):
    __tablename__ = "PostLike"
    
    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey("Users.id", ondelete="CASCADE"))
    post_id = Column(BigInteger, ForeignKey("Post.id", ondelete="CASCADE"))
    is_active = Column(Boolean, default=True)
    created = Column(DateTime(timezone=True), server_default=func.now())
    updated = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    
    # Relationships
    user = relationship("Users", back_populates="post_likes")
    post = relationship("Post", back_populates="likes")
    
    __table_args__ = (
        UniqueConstraint('user_id', 'post_id', name='uq_post_like'),
    )


class Comment(Base):
    __tablename__ = "Comment"
    
    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey("Users.id", ondelete="CASCADE"))
    post_id = Column(BigInteger, ForeignKey("Post.id", ondelete="CASCADE"))
    parent_id = Column(BigInteger, ForeignKey("Comment.id"))  # for nested comments
    content = Column(Text, nullable=False)
    is_active = Column(Boolean, default=True)
    created = Column(DateTime(timezone=True), server_default=func.now())
    updated = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    
    # Relationships
    user = relationship("Users", back_populates="comments")
    post = relationship("Post", back_populates="comments")
    parent = relationship("Comment", remote_side=[id], backref="replies")
    comment_likes = relationship("CommentLike", back_populates="comment")


class PostFile(Base):
    __tablename__ = "post_file"
    
    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    post_id = Column(BigInteger, ForeignKey("Post.id", ondelete="CASCADE"))
    file_id = Column(BigInteger, ForeignKey("upload_file.id", ondelete="CASCADE"))
    order_index = Column(Integer, default=0)
    created = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    post = relationship("Post")
    file = relationship("File")


class CommentLike(Base):
    __tablename__ = "comment_like"
    
    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey("Users.id", ondelete="CASCADE"))
    comment_id = Column(BigInteger, ForeignKey("Comment.id", ondelete="CASCADE"))
    is_active = Column(Boolean, default=True)
    created = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    user = relationship("Users")
    comment = relationship("Comment")
    
    __table_args__ = (
        UniqueConstraint('user_id', 'comment_id', name='uq_comment_like'),
    )
