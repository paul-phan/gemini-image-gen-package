---
name: gemini-image-gen
description: Generate images using Google Gemini models via CLIProxyAPI
metadata:
  openclaw:
    emoji: 🎨
---

# Gemini Image Generation Skill

Generate high-quality images using Google Gemini models through CLIProxyAPI.

## Prerequisites

- CLIProxyAPI running locally (port 8317)
- Google AI Pro account authenticated with Gemini CLI

## Quick Start

### Generate an image (saved to ~/.openclaw/workspace/tmp/)

```bash
~/.openclaw/workspace/skills/gemini-image-gen/gemini-image "A cute robot eating a banana"
# Output: ~/.openclaw/workspace/tmp/generated_image.png
```

### Specify custom output file

```bash
~/.openclaw/workspace/skills/gemini-image-gen/gemini-image \
  "A serene Japanese garden" \
  ./my-garden.png
```

### Use different model (faster)

```bash
~/.openclaw/workspace/skills/gemini-image-gen/gemini-image \
  "Quick sketch of a cat" \
  -m gemini-2.5-flash-image
```

### Image-to-Image with Reference

```bash
# Single reference image
~/.openclaw/workspace/skills/gemini-image-gen/gemini-image \
  -r ./my-photo.jpg \
  "Change background to professional office setting"

# Multiple reference images (NEW!)
~/.openclaw/workspace/skills/gemini-image-gen/gemini-image \
  -r ./face.jpg -r ./outfit.jpg -r ./background.jpg \
  "Combine these into a cohesive portrait"

# Modify specific elements
~/.openclaw/workspace/skills/gemini-image-gen/gemini-image \
  -r ./portrait.png \
  "Add sunglasses and make it look like a movie poster"
```

## Image-to-Image (Reference Mode)

Use the `-r` flag to provide reference image(s) for editing or style transfer:

```bash
# Basic usage with single reference
python3 generate_image.py \
  -r ./my-photo.jpg \
  "Change background to beach sunset"

# Multiple reference images (NEW!)
python3 generate_image.py \
  -r ./face.jpg -r ./outfit.jpg -r ./background.jpg \
  "Combine these references into a cohesive portrait"

# Style transfer
python3 generate_image.py \
  -r ./photo.jpg \
  "Transform into oil painting style"
```

**Supported formats:** PNG, JPG, JPEG, WEBP, GIF

**Tips for best results:**
- Use clear, high-quality reference images
- Be specific about what you want to change
- Reference image + prompt work together

## Available Models

| Model | Quality | Speed | Resolution | Best For |
|-------|---------|-------|------------|----------|
| `gemini-3-pro-image` | 🏆 Highest | ~5-8s | **Up to 4K (4096×4096)** | Production assets, text rendering |
| `gemini-2.5-flash-image` | ⚡ Good | ~2-3s | 1024px | Rapid prototyping, drafts |

## Image Resolution

- **gemini-3-pro-image**: Native 4K support (up to 4096×4096 pixels)
  - Perfect for professional print, marketing materials
  - Superior text rendering in images
  - Higher quality but takes longer
  
- **gemini-2.5-flash-image**: Standard 1024px
  - Fast generation for quick iterations
  - Good for drafts and prototyping

## Default Output Location

Images are saved to `~/.openclaw/workspace/tmp/` by default. You can change this with `-o` flag.

## Usage

```
python3 generate_image.py [OPTIONS] PROMPT

Options:
  -o, --output PATH     Output file path (default: generated_image.png)
  -m, --model MODEL     Model to use (default: gemini-3-pro-image)
  -r, --ref PATH        Reference image for image-to-image generation
  --proxy-url URL       CLIProxyAPI URL (default: http://127.0.0.1:8317)
  --api-key KEY         API key (default: local-api-key)

Examples:
  # Basic usage
  python3 generate_image.py "A futuristic city at sunset"

  # With custom output
  python3 generate_image.py "Abstract art" -o ./artwork.png

  # Fast generation
  python3 generate_image.py "Sketch" -m gemini-2.5-flash-image -o ./sketch.jpg
```

## Prompt Tips

Use this formula for best results:

```
[Style] [Subject] [Composition] [Context/Atmosphere]
```

**Examples:**
- `Minimalist 3D illustration of abstract geometric shapes floating in space, soft gradient background`
- `Photorealistic portrait of a cyberpunk hacker with neon lighting, cinematic composition`
- `Watercolor painting of a peaceful mountain landscape at dawn, misty atmosphere`

## Troubleshooting

### "Connection refused" error
- Ensure CLIProxyAPI is running: `curl http://127.0.0.1:8317/v1/models`
- Check if port 8317 is correct in your config

### "No image in response" error
- Try a different prompt
- Check if model name is correct
- Ensure your Google AI Pro account has image generation quota

### Timeout errors
- Image generation takes 2-8 seconds depending on model
- Check CLIProxyAPI logs: `tail -f /tmp/cliproxyapi.log`

## Configuration

Set default values via environment variables:

```bash
export GEMINI_PROXY_URL="http://127.0.0.1:8317"
export GEMINI_API_KEY="local-api-key"
export GEMINI_DEFAULT_MODEL="gemini-3-pro-image"
```

## Integration with OpenClaw

Use in OpenClaw sessions:

```python
# Generate image for a project
!python3 ~/.openclaw/workspace/skills/gemini-image-gen/generate_image.py \
  "Hero image for tech startup website, modern minimalist style" \
  -o ./assets/hero.png
```

## License

MIT - Free for personal and commercial use
