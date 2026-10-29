# Changelog

Заметные изменения проекта.

## [Unreleased]

## [1.0.0] - 2026-10-29

### Added
- Контейнеризация приложения и PostgreSQL через Docker Compose.
- Автоматические проверки Ruff и pytest в GitHub Actions.
- Публикация Docker-образа по тегам версий.
- README и RUNBOOK с инструкциями запуска и отката.

### Security
- Секреты передаются через локальный `.env`, который исключён из Git.
