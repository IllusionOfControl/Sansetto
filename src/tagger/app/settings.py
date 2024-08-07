from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class MinIOSettings(BaseSettings):
    endpoint: str = Field(examples=["minio", "minio:9000"], env="MINIO_HOST")
    access_key: str = Field(env="MINIO_ACCESS_KEY")
    secret_key: str = Field(env="MINIO_SECRET_KEY")
    bucket: str = Field(env="MINIO_BUCKET")
    secure: bool = Field(env="MINIO_SECURE")


class DatabaseSettings(BaseSettings):
    protocol: str
    host: str
    port: int
    username: str
    password: str
    database: str


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="uploader__",
        env_nested_delimiter="_",
        env_file_encoding="utf-8",
    )

    minio: MinIOSettings
    database: DatabaseSettings
