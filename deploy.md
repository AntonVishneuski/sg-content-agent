# Solbeg Content Agent — Deploy

You are deploying the Solbeg IT Post Generator agent into the current working directory.
Execute all steps below in order. Detect the user's OS automatically and use the appropriate commands.

---

## Step 1 — Detect OS

Detect the operating system:
```bash
uname -s 2>/dev/null || echo "Windows"
```

- `Darwin` → macOS
- `Linux` → Linux
- anything else / error → Windows

Keep this in context for all subsequent steps.

---

## Step 2 — Download and extract the repository

**macOS / Linux:**
```bash
curl -L https://github.com/YOUR_USERNAME/solbeg-content-agent/archive/refs/heads/main.zip -o /tmp/sca.zip
unzip -q /tmp/sca.zip -d /tmp/sca-extract
cp -r "/tmp/sca-extract/solbeg-content-agent-main/." .
rm -rf /tmp/sca.zip /tmp/sca-extract
```

**Windows (PowerShell):**
```powershell
Invoke-WebRequest -Uri "https://github.com/YOUR_USERNAME/solbeg-content-agent/archive/refs/heads/main.zip" -OutFile "$env:TEMP\sca.zip"
Expand-Archive -Path "$env:TEMP\sca.zip" -DestinationPath "$env:TEMP\sca-extract" -Force
Copy-Item -Path "$env:TEMP\sca-extract\solbeg-content-agent-main\*" -Destination "." -Recurse -Force
Remove-Item "$env:TEMP\sca.zip","$env:TEMP\sca-extract" -Recurse -Force
```

---

## Step 3 — Create folder structure

**macOS / Linux:**
```bash
mkdir -p .claude/skills
mkdir -p "03-Resources/Selling Post Guidebook"
mkdir -p "03-Resources/solbeg/Posts"
mkdir -p 00-Inbox 01-Projects 02-Areas 04-Archive
```

**Windows:**
```powershell
New-Item -ItemType Directory -Force -Path ".claude\skills","03-Resources\Selling Post Guidebook","03-Resources\solbeg\Posts","00-Inbox","01-Projects","02-Areas","04-Archive"
```

---

## Step 4 — Copy skills

**macOS / Linux:**
```bash
cp -r skills/. .claude/skills/
```

**Windows:**
```powershell
Copy-Item -Path "skills\*" -Destination ".claude\skills\" -Recurse -Force
```

---

## Step 5 — Copy guidebooks and company context

**macOS / Linux:**
```bash
cp -r guidebooks/. "03-Resources/Selling Post Guidebook/"
cp -r solbeg/. "03-Resources/solbeg/"
```

**Windows:**
```powershell
Copy-Item -Path "guidebooks\*" -Destination "03-Resources\Selling Post Guidebook\" -Recurse -Force
Copy-Item -Path "solbeg\*" -Destination "03-Resources\solbeg\" -Recurse -Force
```

---

## Step 6 — Install yt-dlp

Try each method in order, stop at first success:

**Method 1 — pip (if Python is installed):**
```bash
pip install yt-dlp --quiet 2>/dev/null || pip3 install yt-dlp --quiet 2>/dev/null || pip install yt-dlp --quiet --break-system-packages 2>/dev/null
```

**Method 2 — Homebrew (macOS):**
```bash
brew install yt-dlp 2>/dev/null
```

**Method 3 — winget (Windows):**
```powershell
winget install yt-dlp 2>$null
```

**Method 4 — standalone binary (macOS/Linux, no Python needed):**
```bash
# macOS
curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp_macos -o /usr/local/bin/yt-dlp && chmod +x /usr/local/bin/yt-dlp

# Linux
curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -o /usr/local/bin/yt-dlp && chmod +x /usr/local/bin/yt-dlp
```

**Method 5 — standalone binary (Windows, no Python needed):**
```powershell
Invoke-WebRequest -Uri "https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.exe" -OutFile "$env:LOCALAPPDATA\Microsoft\WindowsApps\yt-dlp.exe"
```

If all methods fail — skip silently. yt-dlp is only needed for YouTube search. The agent works without it, YouTube search skill will be unavailable.

---

## Step 7 — Clean up repo files (optional)

Remove source folders that were copied and are no longer needed at the root:
```bash
rm -rf skills guidebooks solbeg setup.py deploy.md
```

Windows:
```powershell
Remove-Item -Recurse -Force skills,guidebooks,solbeg,setup.py,deploy.md -ErrorAction SilentlyContinue
```

---

## Step 8 — Verify

Check that the following exist:
- `.claude/skills/` — should contain 8 folders
- `03-Resources/solbeg/Solbeg - Company Summary.md`
- `03-Resources/Selling Post Guidebook/` — should contain .md files
- `CLAUDE.md` in the current directory

Report what was found and what (if anything) is missing.

---

## Step 9 — Report to user

Tell the user:

> ✅ **Agent deployed and ready!**
>
> Skills installed: 8
> Guidebooks: ✓
> Company context: ✓
> yt-dlp: ✓ (or: ⚠ not installed — YouTube search unavailable)
>
> Type **"write a post"** to get started.
