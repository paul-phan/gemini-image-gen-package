#!/bin/bash
# Quick install script for Gemini Image Generation Skill
# This script installs the skill to ~/clawd/skills/

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_DIR="$HOME/clawd/skills/gemini-image-gen"

echo "🎨 Installing Gemini Image Generation Skill..."
echo ""

# Create skills directory
mkdir -p "$HOME/clawd/skills"

# Copy skill files
echo "📁 Copying skill files to $SKILL_DIR..."
cp -r "$SCRIPT_DIR/skill" "$SKILL_DIR"

# Make scripts executable
chmod +x "$SKILL_DIR/generate_image.py"
chmod +x "$SKILL_DIR/gemini-image"

# Create output directory
mkdir -p "$HOME/clawd/tmp"

echo "✅ Installation complete!"
echo ""
echo "🚀 Quick Start:"
echo ""
echo "1. Ensure CLIProxyAPI is running:"
echo "   curl http://127.0.0.1:8317/v1/models"
echo ""
echo "2. Generate an image:"
echo "   ~/clawd/skills/gemini-image-gen/gemini-image \"A cute robot\""
echo ""
echo "3. With reference image:"
echo "   ~/clawd/skills/gemini-image-gen/gemini-image \\"
echo "     -r ./photo.jpg \\"
echo "     \"Change background to office setting\""
echo ""
echo "📖 For CLIProxyAPI setup, see SETUP.md"
echo "📖 For skill usage, see skill/SKILL.md"
