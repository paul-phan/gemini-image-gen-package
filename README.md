# Gemini Image Generation Package

Generate AI images using Google Gemini via CLIProxyAPI - includes text-to-image and image-to-image editing.

## 📦 Package Contents

```
gemini-image-gen-package/
├── skill/                    # The image generation skill
│   ├── generate_image.py     # Main Python script
│   ├── gemini-image          # Shell wrapper
│   └── SKILL.md              # Skill documentation
├── SETUP.md                  # Detailed setup guide
├── README.md                 # This file
└── install.sh                # Quick install script
```

## 🚀 Quick Start

### Step 1: Install CLIProxyAPI

See [SETUP.md](SETUP.md) for detailed instructions.

**TL;DR:**
```bash
git clone https://github.com/router-for-me/CLIProxyAPI.git
cd CLIProxyAPI
go build -o cliproxyapi cmd/server/main.go
./cliproxyapi
```

### Step 2: Configure CLIProxyAPI

Create `config.yaml`:
```yaml
host: "127.0.0.1"
port: 8317
auth-dir: "~/.cli-proxy-api"
api-keys:
  - "local-api-key"
debug: false
```

### Step 3: Authenticate

```bash
# Login with your Google AI Pro account
gemini auth login
# Follow the browser flow to authenticate
```

### Step 4: Use the Skill

```bash
# Copy skill to your workspace
cp -r skill ~/clawd/skills/gemini-image-gen

# Generate image
~/clawd/skills/gemini-image-gen/gemini-image "A cute robot"

# With reference image
~/clawd/skills/gemini-image-gen/gemini-image \
  -r ./logo.png \
  "Create a hero banner with this logo"
```

## 🎯 Features

- **Text-to-Image:** Generate images from text prompts
- **Image-to-Image:** Edit images using reference photos
- **Multiple Models:** gemini-3-pro-image (4K) & gemini-2.5-flash-image (fast)
- **Default Output:** Saves to `~/clawd/tmp/`

## 📖 Documentation

- [SETUP.md](SETUP.md) - Complete setup guide for CLIProxyAPI
- [skill/SKILL.md](skill/SKILL.md) - Skill usage documentation

## 🛠️ Requirements

- Go 1.21+ (for building CLIProxyAPI)
- Python 3.8+ (for the skill)
- Google AI Pro account
- macOS/Linux

## 📄 License

MIT - Free for personal and commercial use
