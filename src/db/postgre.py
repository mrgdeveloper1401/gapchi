from decouple import config


class Settings:
    PROJECT_NAME:str = "Gapchi"
    PROJECT_VERSION: str = "1.0.0"

    POSTGRES_USER : str = config("POSTGRES_USERNAME", cast=str)
    POSTGRES_PASSWORD = config("POSTGRES_PASSWORD", cast=str)
    POSTGRES_SERVER : str = config("POSTGRES_HOST", cast=str)
    POSTGRES_PORT : int = config("POSTGRES_PORT", cast=int) # default postgres port is 5432
    POSTGRES_DB : str = config("POSTGRES_DB_NAME", cast=str)
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

settings = Settings()
# print(settings.DATABASE_URL)