# CLIProxyAPI Setup Guide

Complete guide to set up CLIProxyAPI for Google Gemini image generation.

## 📋 Prerequisites

- **Google AI Pro account** - Subscribe at [gemini.google.com](https://gemini.google.com)
- **Go 1.21+** - Install via `brew install go` (macOS) or [golang.org](https://golang.org)
- **Git** - For cloning the repository

## 🛠️ Installation

### Step 1: Clone CLIProxyAPI

```bash
cd ~/Workspace
git clone https://github.com/router-for-me/CLIProxyAPI.git
cd CLIProxyAPI
```

### Step 2: Build CLIProxyAPI

```bash
go build -o cliproxyapi cmd/server/main.go
```

Verify the build:
```bash
./cliproxyapi --help
```

### Step 3: Create Config File

Create `config.yaml` in the CLIProxyAPI directory:

```yaml
host: "127.0.0.1"
port: 8317

auth-dir: "~/.cli-proxy-api"

api-keys:
  - "local-api-key"

debug: false
```

### Step 4: Authenticate with Gemini

First, ensure you have Gemini CLI installed:

```bash
# macOS
brew install gemini-cli

# Or install from source
# See: https://github.com/google-gemini/gemini-cli
```

Then login with your Google AI Pro account:

```bash
gemini auth login
```

This will open a browser window. Complete the OAuth flow with your Google AI Pro account.

### Step 5: Start CLIProxyAPI

```bash
# Start in background
nohup ./cliproxyapi > /tmp/cliproxyapi.log 2>&1 &

# Or run in terminal for debugging
./cliproxyapi
```

### Step 6: Verify Installation

```bash
# Test API is running
curl http://127.0.0.1:8317/v1/models \
  -H "Authorization: Bearer local-api-key"

# Should return list of models including:
# - gemini-3-pro-image
# - gemini-2.5-flash-image
```

## 🎨 Image Generation Models

| Model | Resolution | Speed | Best For |
|-------|------------|-------|----------|
| `gemini-3-pro-image` | Up to 4K (4096×4096) | ~5-8s | High quality, text rendering |
| `gemini-2.5-flash-image` | 1024px | ~2-3s | Fast prototyping |

## 🔧 Troubleshooting

### "Connection refused" Error

```bash
# Check if CLIProxyAPI is running
ps aux | grep cliproxyapi

# Restart if needed
pkill -f cliproxyapi
cd ~/Workspace/CLIProxyAPI
nohup ./cliproxyapi > /tmp/cliproxyapi.log 2>&1 &
```

### "auth_unavailable" Error

Your Gemini CLI authentication may have expired:

```bash
# Re-authenticate
gemini auth login

# Or check auth status
gemini auth status
```

### "No capacity available" Error

The model is temporarily overloaded:

```bash
# Wait 30-60 seconds and retry
# Or switch to flash model for faster generation
```

### View Logs

```bash
# Real-time logs
tail -f /tmp/cliproxyapi.log
```

## 📁 File Locations

| Component | Default Location |
|-----------|------------------|
| CLIProxyAPI binary | `~/Workspace/CLIProxyAPI/cliproxyapi` |
| Config file | `~/Workspace/CLIProxyAPI/config.yaml` |
| Auth credentials | `~/.gemini/` |
| Generated images | `~/.openclaw/workspace/tmp/` |
| Logs | `/tmp/cliproxyapi.log` |

## 🔐 API Key

Default API key in this setup: `local-api-key`

To change it, edit `config.yaml`:
```yaml
api-keys:
  - "your-custom-key"
```

Then use it in requests:
```bash
curl http://127.0.0.1:8317/v1/models \
  -H "Authorization: Bearer your-custom-key"
```

## 🚀 Auto-start on Boot (Optional)

### macOS (launchd)

Create `~/Library/LaunchAgents/com.cliproxyapi.plist`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.cliproxyapi</string>
    <key>ProgramArguments</key>
    <array>
        <string>/Users/YOUR_USERNAME/Workspace/CLIProxyAPI/cliproxyapi</string>
    </array>
    <key>WorkingDirectory</key>
    <string>/Users/YOUR_USERNAME/Workspace/CLIProxyAPI</string>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
    <key>StandardOutPath</key>
    <string>/tmp/cliproxyapi.log</string>
    <key>StandardErrorPath</key>
    <string>/tmp/cliproxyapi.log</string>
</dict>
</plist>
```

Load the service:
```bash
launchctl load ~/Library/LaunchAgents/com.cliproxyapi.plist
```

## 📖 References

- [CLIProxyAPI GitHub](https://github.com/router-for-me/CLIProxyAPI)
- [CLIProxyAPI Docs](https://help.router-for.me/)
- [Gemini CLI GitHub](https://github.com/google-gemini/gemini-cli)
- [Google AI Pro](https://gemini.google.com/subscriptions/)

## ✅ Verification Checklist

- [ ] Go installed (`go version`)
- [ ] CLIProxyAPI cloned and built
- [ ] config.yaml created
- [ ] Gemini CLI installed (`gemini --version`)
- [ ] Authenticated with Google AI Pro (`gemini auth status`)
- [ ] CLIProxyAPI running (`curl http://127.0.0.1:8317/v1/models`)
- [ ] Image generation skill installed
- [ ] Test image generated successfully
