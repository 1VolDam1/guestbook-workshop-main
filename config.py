from urllib.parse import quote

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    postgres_user: str
    postgres_password: str
    postgres_db: str
    postgres_host: str = "localhost"
    postgres_port: int = 5432
    greeting: str = "Добро пожаловать в гостевую книгу!"

    @property
    def database_url(self) -> str:
        # URL-encode credentials so valid punctuation in passwords remains safe.
        password = quote(self.postgres_password, safe="")
        user = quote(self.postgres_user, safe="")
        database = quote(self.postgres_db, safe="")
        return (
            f"postgresql://{user}:{password}"
            f"@{self.postgres_host}:{self.postgres_port}/{database}"
        )


settings = Settings()
