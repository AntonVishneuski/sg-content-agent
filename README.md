# Solbeg IT Post Generator — Agent

Агент для генерации IT-постов для Solbeg в социальных сетях (LinkedIn, Medium, Reddit).  
Работает в любой папке через Claude Code — Obsidian не требуется.

## Что умеет

- Находит актуальные IT-тренды (Web, YouTube, LinkedIn, Medium, Reddit)
- Предлагает темы на выбор, исключая уже написанные
- Пишет посты в стиле Solbeg по Selling Post Framework
- Адаптирует под LinkedIn, Medium, Reddit
- Сохраняет историю постов

## Быстрый старт

### 1. Создай папку для агента

```bash
mkdir solbeg-content-agent && cd solbeg-content-agent
```

### 2. Открой Claude Code в этой папке

```bash
claude
```

### 3. Введи одну команду

```
разверни агента https://gist.github.com/YOUR_USERNAME/GIST_ID
```

Claude сам скачает репозиторий, настроит структуру папок, установит зависимости и будет готов к работе.

### 4. Напиши пост

```
напиши пост
```

---

## Ручная установка (если нужно)

```bash
git clone https://github.com/YOUR_USERNAME/solbeg-content-agent.git
cd solbeg-content-agent
python setup.py
```

---

## Структура

```
.claude/skills/              ← Claude Code скилы (создаётся при деплое)
  it-post-generator/
  youtube-search/
  linkedin-news-search/
  linkedin-post-adapter/
  medium-news-search/
  medium-post-adapter/
  reddit-news-search/
  reddit-post-adapter/

03-Resources/                ← контент (создаётся при деплое)
  Selling Post Guidebook/    ← фреймворк написания постов
  solbeg/
    Solbeg - Company Summary.md
    posts-history.md
    Posts/

CLAUDE.md                    ← конфиг агента
```

## Зависимости

- Python 3
- `yt-dlp` — для поиска по YouTube (устанавливается автоматически)

## Скилы

| Скил | Описание |
|------|----------|
| `it-post-generator` | Главный оркестратор: тренды → тема → пост → сохранение |
| `youtube-search` | Поиск видео через yt-dlp |
| `linkedin-news-search` | Поиск трендов на LinkedIn |
| `linkedin-post-adapter` | Адаптация поста под LinkedIn |
| `medium-news-search` | Поиск статей на Medium |
| `medium-post-adapter` | Адаптация поста под Medium |
| `reddit-news-search` | Поиск обсуждений на Reddit |
| `reddit-post-adapter` | Адаптация поста под Reddit |
