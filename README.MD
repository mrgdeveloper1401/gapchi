# 🚀 Gapchi Social Media API

یک API اجتماعی مدرن و قدرتمند ساخته شده با **FastAPI** و **MSSQL** برای پلتفرم Gapchi.

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![MSSQL](https://img.shields.io/badge/Microsoft%20SQL%20Server-CC2927?style=for-the-badge&logo=microsoft%20sql%20server&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

## 📋 فهرست مطالب

- [ویژگی‌ها](#-ویژگیها)
- [ساختار پروژه](#-ساختار-پروژه)
- [پیش‌نیازها](#-پیشنیازها)
- [نصب و راه‌اندازی](#-نصب-و-راهاندازی)
- [پیکربندی](#-پیکربندی)
- [اجرا](#-اجرا)
- [API Endpoints](#-api-endpoints)
- [مدل‌های دیتابیس](#-مدلهای-دیتابیس)
- [توسعه](#-توسعه)

## ✨ ویژگی‌ها

- ✅ **احراز هویت کامل** (JWT Tokens)
- ✅ **مدیریت کاربران** و پروفایل‌ها
- ✅ **سیستم پست و کامنت**
- ✅ **سیستم پیام‌رسانی داخلی**
- ✅ **مدیریت فایل و آپلود**
- ✅ **موقعیت‌یابی جغرافیایی**
- ✅ **سیستم اطلاع‌رسانی**
- ✅ **پشتیبانی از MSSQL**
- ✅ **الگوی معماری مدرن**
<!-- - ✅ **مستندات خودکار API** (Swagger) -->
<!-- - ✅ **دسترسی‌های سطح‌بندی شده** -->

<!-- ## 🗂️ ساختار پروژه
gapchi-api/
├── app/
│ ├── api/
│ │ ├── endpoints/
│ │ │ ├── auth.py
│ │ │ ├── users.py
│ │ │ ├── posts.py
│ │ │ └── ...
│ │ └── init.py
│ ├── core/
│ │ ├── config.py
│ │ └── security.py
│ ├── crud/
│ │ ├── crud_user.py
│ │ ├── crud_post.py
│ │ └── ...
│ ├── database/
│ │ ├── connection.py
│ │ └── base.py
│ ├── models/
│ │ ├── models.py
│ │ └── init.py
│ ├── schemas/
│ │ ├── schemas.py
│ │ └── init.py
│ ├── services/
│ │ ├── auth_service.py
│ │ └── file_service.py
│ └── init.py
├── tests/
├── static/
├── uploads/
├── .env
├── requirements.txt
├── main.py
└── README.md -->


## ⚙️ پیش‌نیازها

### نرم‌افزارهای مورد نیاز
- **Python 3.8+**
- **POSTGRESQL** (17)
- **docker** for postgres
- **Git**

<!-- ### نصب ODBC Driver (linux)
    sudo apt install odbcinst1debian2 unixodbc unixodbc-dev -->

### clone project
    git clone https://github.com/your-username/gapchi-api.git
    cd gapchi-api

### create venv
    for linux --> python3 -m venv venv
    source venv/bin/activate

    for windows --> not suported :)

### install dependecies
    pip install -r requirements.txt


### configurate
    cp .env.example .env
