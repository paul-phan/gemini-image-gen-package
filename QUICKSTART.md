# 🚀 Gemini Image Gen - Quick Start for Colleagues

## What You Get

Generate AI images using your Google AI Pro account via CLIProxyAPI:
- ✅ Text-to-image generation
- ✅ Image-to-image editing (with reference photos)
- ✅ Up to 4K resolution
- ✅ Works on macOS/Linux

## ⚡ 5-Minute Setup

### 1. Install Prerequisites

```bash
# Install Go (macOS)
brew install go

# Install Gemini CLI
brew install gemini-cli
```

### 2. Setup CLIProxyAPI

```bash
# Clone and build
cd ~/Workspace
git clone https://github.com/router-for-me/CLIProxyAPI.git
cd CLIProxyAPI
go build -o cliproxyapi cmd/server/main.go

# Create config
cat > config.yaml << 'EOF'
host: "127.0.0.1"
port: 8317
auth-dir: "~/.cli-proxy-api"
api-keys:
  - "local-api-key"
debug: false
EOF
```

### 3. Authenticate

```bash
# Login with your Google AI Pro account
gemini auth login
# Follow browser flow
```

### 4. Start CLIProxyAPI

```bash
# Start in background
nohup ./cliproxyapi > /tmp/cliproxyapi.log 2>&1 &

# Test it's working
curl http://127.0.0.1:8317/v1/models \
  -H "Authorization: Bearer local-api-key"
```

### 5. Install This Skill

```bash
cd /path/to/gemini-image-gen-package
./install.sh
```

## 🎨 Usage

### Generate Image

```bash
~/clawd/skills/gemini-image-gen/gemini-image "A futuristic city"
# Output: ~/clawd/tmp/generated_image.png
```

### With Reference Image

```bash
~/clawd/skills/gemini-image-gen/gemini-image \
  -r ./my-logo.png \
  "Create a hero banner with this logo"
```

### Custom Output

```bash
~/clawd/skills/gemini-image-gen/gemini-image \
  "A serene landscape" \
  ./my-landscape.png
```

## 📦 Package Contents

```
gemini-image-gen-package/
├── skill/              # The image generation scripts
├── README.md           # Overview
├── SETUP.md            # Detailed setup guide
└── install.sh          # Quick install script
```

## 🆘 Troubleshooting

| Issue | Solution |
|-------|----------|
| "Connection refused" | Restart CLIProxyAPI: `pkill -f cliproxyapi && ./cliproxyapi` |
| "auth_unavailable" | Re-authenticate: `gemini auth login` |
| "No capacity" | Wait 30s and retry, or use `-m gemini-2.5-flash-image` |

## 📖 Full Documentation

- **SETUP.md** - Complete CLIProxyAPI setup guide
- **skill/SKILL.md** - Detailed skill usage

## 💡 Pro Tips

1. **Default output:** `~/clawd/tmp/`
2. **Best quality:** Use `gemini-3-pro-image` (default)
3. **Fastest:** Use `-m gemini-2.5-flash-image`
4. **Reference images:** Works with PNG, JPG, WEBP

## ✅ Check It's Working

```bash
# Test generation
~/clawd/skills/gemini-image-gen/gemini-image "A cute cat"

# Should output:
# 🎨 Generating image with gemini-3-pro-image...
# 📝 Prompt: A cute cat...
# ✅ Image saved to: /Users/YOU/clawd/tmp/generated_image.png
# 📦 Size: XXX.X KB
```

---

**Need help?** Check SETUP.md for detailed troubleshooting.
