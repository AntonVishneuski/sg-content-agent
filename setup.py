#!/usr/bin/env python3
"""
Solbeg Agent — Setup Script
Разворачивает агента в текущей папке.
Запуск: python setup.py
"""

import os
import sys
import shutil
import subprocess
import zipfile
import urllib.request
from pathlib import Path

REPO_URL = "https://github.com/YOUR_USERNAME/solbeg-content-agent/archive/refs/heads/main.zip"
REPO_DIR_NAME = "solbeg-content-agent-main"

SKILLS = [
    "it-post-generator",
    "youtube-search",
    "linkedin-news-search",
    "linkedin-post-adapter",
    "medium-news-search",
    "medium-post-adapter",
    "reddit-news-search",
    "reddit-post-adapter",
]

def log(msg):
    print(f"  {msg}")

def step(msg):
    print(f"\n▶ {msg}")

def ok(msg):
    print(f"  ✓ {msg}")

def warn(msg):
    print(f"  ⚠ {msg}")


def check_python():
    step("Проверка Python")
    version = sys.version_info
    if version.major < 3:
        print("✗ Нужен Python 3+")
        sys.exit(1)
    ok(f"Python {version.major}.{version.minor}")


def install_yt_dlp():
    step("Установка yt-dlp")
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", "yt-dlp", "--quiet"],
            capture_output=True, text=True
        )
        if result.returncode == 0:
            ok("yt-dlp установлен")
        else:
            # Попробуем с --break-system-packages (Linux)
            result2 = subprocess.run(
                [sys.executable, "-m", "pip", "install", "yt-dlp", "--quiet", "--break-system-packages"],
                capture_output=True, text=True
            )
            if result2.returncode == 0:
                ok("yt-dlp установлен")
            else:
                warn("yt-dlp не удалось установить автоматически. Запусти: pip install yt-dlp")
    except Exception as e:
        warn(f"yt-dlp: {e}")


def download_repo(vault_root: Path) -> Path:
    step("Скачиваю репозиторий")
    zip_path = vault_root / "_agent_setup.zip"
    extract_path = vault_root / "_agent_extract"

    log(f"URL: {REPO_URL}")
    try:
        urllib.request.urlretrieve(REPO_URL, zip_path)
        ok("Загружено")
    except Exception as e:
        print(f"✗ Ошибка загрузки: {e}")
        print("  Убедись что URL репозитория правильный в setup.py (строка REPO_URL)")
        sys.exit(1)

    step("Распаковываю")
    if extract_path.exists():
        shutil.rmtree(extract_path)
    with zipfile.ZipFile(zip_path, 'r') as z:
        z.extractall(extract_path)
    ok("Распаковано")

    zip_path.unlink()
    return extract_path / REPO_DIR_NAME


def create_structure(vault_root: Path):
    step("Создаю структуру папок")
    folders = [
        ".claude/skills",
        "03-Resources/Selling Post Guidebook",
        "03-Resources/solbeg/Posts",
        "00-Inbox",
        "01-Projects",
        "02-Areas",
        "04-Archive",
    ]
    for folder in folders:
        (vault_root / folder).mkdir(parents=True, exist_ok=True)
        ok(folder)


def copy_skills(repo_root: Path, vault_root: Path):
    step("Копирую скилы в .claude/skills/")
    skills_src = repo_root / "skills"
    skills_dst = vault_root / ".claude" / "skills"

    for skill in SKILLS:
        src = skills_src / skill
        dst = skills_dst / skill
        if src.exists():
            if dst.exists():
                shutil.rmtree(dst)
            shutil.copytree(src, dst)
            ok(skill)
        else:
            warn(f"{skill} — не найден в репозитории")


def copy_guidebooks(repo_root: Path, vault_root: Path):
    step("Копирую гайдбуки в 03-Resources/Selling Post Guidebook/")
    src = repo_root / "guidebooks"
    dst = vault_root / "03-Resources" / "Selling Post Guidebook"
    if src.exists():
        for f in src.glob("*.md"):
            shutil.copy2(f, dst / f.name)
            ok(f.name)
    else:
        warn("Папка guidebooks не найдена в репозитории")


def copy_solbeg(repo_root: Path, vault_root: Path):
    step("Копирую контекст компании в 03-Resources/solbeg/")
    src = repo_root / "solbeg"
    dst = vault_root / "03-Resources" / "solbeg"

    if not src.exists():
        warn("Папка solbeg не найдена в репозитории")
        return

    # Корневые файлы
    for f in src.glob("*.md"):
        shutil.copy2(f, dst / f.name)
        ok(f.name)

    # Posts
    posts_src = src / "Posts"
    posts_dst = dst / "Posts"
    if posts_src.exists():
        for f in posts_src.glob("*.md"):
            shutil.copy2(f, posts_dst / f.name)
        ok(f"Posts/ ({len(list(posts_src.glob('*.md')))} файлов)")


def copy_claude_md(repo_root: Path, vault_root: Path):
    step("Копирую CLAUDE.md")
    src = repo_root / "CLAUDE.md"
    dst = vault_root / "CLAUDE.md"
    if src.exists():
        shutil.copy2(src, dst)
        ok("CLAUDE.md")
    else:
        warn("CLAUDE.md не найден в репозитории")


def cleanup(vault_root: Path):
    extract = vault_root / "_agent_extract"
    if extract.exists():
        shutil.rmtree(extract)


def verify(vault_root: Path):
    step("Проверка установки")
    skills_dir = vault_root / ".claude" / "skills"
    installed = [d.name for d in skills_dir.iterdir() if d.is_dir()] if skills_dir.exists() else []
    ok(f"Скилов установлено: {len(installed)}/{len(SKILLS)}")
    for skill in SKILLS:
        status = "✓" if skill in installed else "✗"
        log(f"  {status} {skill}")

    company = vault_root / "03-Resources" / "solbeg" / "Solbeg - Company Summary.md"
    ok(f"Company Summary: {'найден' if company.exists() else 'НЕ НАЙДЕН'}")

    guidebooks = list((vault_root / "03-Resources" / "Selling Post Guidebook").glob("*.md"))
    ok(f"Гайдбуки: {len(guidebooks)} файлов")


def main():
    print("\n" + "="*50)
    print("  Solbeg Agent — Setup")
    print("="*50)

    vault_root = Path.cwd()
    log(f"Папка: {vault_root}")

    check_python()
    install_yt_dlp()
    repo_root = download_repo(vault_root)
    create_structure(vault_root)
    copy_skills(repo_root, vault_root)
    copy_guidebooks(repo_root, vault_root)
    copy_solbeg(repo_root, vault_root)
    copy_claude_md(repo_root, vault_root)
    cleanup(vault_root)
    verify(vault_root)

    print("\n" + "="*50)
    print("  ✅ Агент готов к работе!")
    print("  Открой Claude Code в этой папке и напиши:")
    print('  "напиши пост"')
    print("="*50 + "\n")


if __name__ == "__main__":
    main()
