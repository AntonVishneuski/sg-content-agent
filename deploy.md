# Solbeg Agent — Deploy

You are deploying the Solbeg IT Post Generator agent into the current working directory.
Execute all steps below in order. Adapt commands to the user's OS automatically.

---

## Step 1 — Check prerequisites

Check if Python 3 is installed:
```bash
python3 --version || python --version
```

If not installed, tell the user to install Python 3 from https://python.org and stop.

---

## Step 2 — Download the repository

Download and extract the repository into the current directory.

**macOS / Linux:**
```bash
curl -L https://github.com/YOUR_USERNAME/solbeg-content-agent/archive/refs/heads/main.zip -o /tmp/solbeg-content-agent.zip
unzip -q /tmp/solbeg-content-agent.zip -d /tmp/solbeg-extract
cp -r /tmp/solbeg-extract/solbeg-content-agent-main/. .
rm -rf /tmp/solbeg-content-agent.zip /tmp/solbeg-extract
```

**Windows (PowerShell):**
```powershell
Invoke-WebRequest -Uri "https://github.com/YOUR_USERNAME/solbeg-content-agent/archive/refs/heads/main.zip" -OutFile "$env:TEMP\solbeg-content-agent.zip"
Expand-Archive -Path "$env:TEMP\solbeg-content-agent.zip" -DestinationPath "$env:TEMP\solbeg-extract" -Force
Copy-Item -Path "$env:TEMP\solbeg-extract\solbeg-content-agent-main\*" -Destination "." -Recurse -Force
Remove-Item "$env:TEMP\solbeg-content-agent.zip","$env:TEMP\solbeg-extract" -Recurse -Force
```

---

## Step 3 — Run the setup script

```bash
python3 setup.py
```

or on Windows:
```bash
python setup.py
```

The script will:
- Create all required folders
- Copy skills to `.claude/skills/`
- Copy guidebooks to `03-Resources/Selling Post Guidebook/`
- Copy company context to `03-Resources/solbeg/`
- Copy `CLAUDE.md` to the vault root
- Install `yt-dlp`

---

## Step 4 — Verify

After setup.py completes, confirm:
1. `.claude/skills/` contains 8 skill folders
2. `03-Resources/solbeg/Solbeg - Company Summary.md` exists
3. `03-Resources/Selling Post Guidebook/` contains guidebook files

If any are missing, report the issue to the user.

---

## Step 5 — Report success

Tell the user:

> ✅ **Агент развёрнут и готов к работе!**
>
> Установлено скилов: 8
> Гайдбуки: ✓
> Контекст компании: ✓
> yt-dlp: ✓
>
> Напиши **"напиши пост"** — и агент начнёт работу.
