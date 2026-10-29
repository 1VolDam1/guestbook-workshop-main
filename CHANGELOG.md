# Changelog

Заметные изменения проекта документируются здесь. Формат основан на Keep a Changelog; версии следуют SemVer.

## [Unreleased]

### Added
- Контейнеризация FastAPI-приложения и PostgreSQL через Docker Compose.
- CI с Ruff и pytest для push и pull request.
- Публикация `latest` из `main` и версионированных Docker-образов по SemVer-тегам в GHCR.
- README и runbook с инструкциями запуска, проверки и отката.

### Security
- Настройки и пароль PostgreSQL передаются через переменные окружения; `.env` исключён из git и Docker-образа.

<!-- Перед первым релизом перенесите пункты из Unreleased в раздел
     ## [1.0.0] - YYYY-MM-DD, закоммитьте, затем поставьте тег v1.0.0. -->
