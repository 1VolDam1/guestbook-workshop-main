# Changelog

Заметные изменения проекта.

## [Unreleased]

## [1.1.0] - 2026-10-29

### Added
- Добавлен адрес `GET /version`, который возвращает версию приложения.

## [1.0.0] - 2026-10-29

### Added
- Приложение и PostgreSQL запускаются через Docker Compose.
- Ruff и pytest автоматически проверяются в GitHub Actions.
- Docker-образы публикуются в GitHub Container Registry.
- Добавлены README и RUNBOOK с инструкциями запуска и отката.

### Security
- Секреты передаются через локальный `.env`, который исключён из Git.
