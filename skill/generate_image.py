#!/usr/bin/env python3
"""
Gemini Image Generation via CLIProxyAPI
Generate images using Google Gemini models through CLIProxyAPI
Supports: text-to-image and image-to-image (with single or multiple references)
"""

import argparse
import base64
import json
import os
import sys
import urllib.request
import urllib.error
from pathlib import Path


def encode_image_to_base64(image_path: str) -> tuple:
    """Encode image to base64 and detect mime type"""
    with open(image_path, 'rb') as f:
        image_data = f.read()
    
    # Detect mime type from extension
    ext = Path(image_path).suffix.lower()
    mime_types = {
        '.png': 'image/png',
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.webp': 'image/webp',
        '.gif': 'image/gif'
    }
    mime_type = mime_types.get(ext, 'image/jpeg')
    
    return base64.b64encode(image_data).decode('utf-8'), mime_type


def generate_image(
    prompt: str,
    output_path: str,
    model: str = "gemini-3-pro-image",
    proxy_url: str = "http://127.0.0.1:8317",
    api_key: str = "local-api-key",
    reference_images: list = None
) -> str:
    """Generate image using CLIProxyAPI"""
    
    endpoint = f"{proxy_url}/v1beta/models/{model}:generateContent"
    
    # Build parts array
    parts = []
    
    # Add reference images if provided (supports multiple)
    if reference_images:
        for i, ref_image in enumerate(reference_images, 1):
            if not os.path.exists(ref_image):
                raise Exception(f"Reference image not found: {ref_image}")
            
            image_b64, mime_type = encode_image_to_base64(ref_image)
            parts.append({
                "inlineData": {
                    "mimeType": mime_type,
                    "data": image_b64
                }
            })
            print(f"📎 Reference {i}: {ref_image}")
    
    # Add text prompt
    parts.append({"text": prompt})
    
    payload = {
        "contents": [{
            "role": "user",
            "parts": parts
        }],
        "generationConfig": {
            "responseModalities": ["IMAGE", "TEXT"]
        }
    }
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    req = urllib.request.Request(
        endpoint,
        data=json.dumps(payload).encode('utf-8'),
        headers=headers,
        method='POST'
    )
    
    try:
        with urllib.request.urlopen(req, timeout=120) as response:
            result = json.loads(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        error_body = e.read().decode('utf-8')
        raise Exception(f"HTTP Error {e.code}: {error_body}")
    except Exception as e:
        raise Exception(f"Request failed: {e}")
    
    # Extract image from response
    if 'candidates' not in result or not result['candidates']:
        raise Exception("No candidates in response")
    
    candidate = result['candidates'][0]
    if 'content' not in candidate or 'parts' not in candidate['content']:
        raise Exception("No content parts in response")
    
    image_found = False
    text_response = ""
    
    for part in candidate['content']['parts']:
        if 'inlineData' in part:
            data = part['inlineData']['data']
            mime_type = part['inlineData'].get('mimeType', 'image/png')
            
            # Decode base64
            image_data = base64.b64decode(data)
            
            # Determine file extension
            ext = '.png' if 'png' in mime_type else '.jpg'
            if not output_path.endswith(('.png', '.jpg', '.jpeg')):
                output_path += ext
            
            # Save image
            with open(output_path, 'wb') as f:
                f.write(image_data)
            
            image_found = True
            
        elif 'text' in part:
            text_response = part['text']
    
    if not image_found:
        raise Exception(f"No image in response. Text: {text_response[:200]}")
    
    return output_path


DEFAULT_OUTPUT_DIR = os.path.expanduser("~/.openclaw/workspace/tmp")

def main():
    parser = argparse.ArgumentParser(
        description='Generate images using Gemini via CLIProxyAPI'
    )
    parser.add_argument(
        'prompt',
        help='Image generation prompt'
    )
    parser.add_argument(
        '-o', '--output',
        default=os.path.join(DEFAULT_OUTPUT_DIR, 'generated_image.png'),
        help='Output file path (default: ~/.openclaw/workspace/tmp/generated_image.png)'
    )
    parser.add_argument(
        '-m', '--model',
        default='gemini-3-pro-image',
        choices=['gemini-3-pro-image', 'gemini-2.5-flash-image'],
        help='Model to use (default: gemini-3-pro-image)'
    )
    parser.add_argument(
        '-r', '--ref',
        nargs='*',
        action='extend',
        default=[],
        help='Reference image path(s) for image-to-image generation. Can specify multiple: -r img1.png -r img2.png'
    )
    parser.add_argument(
        '--proxy-url',
        default='http://127.0.0.1:8317',
        help='CLIProxyAPI URL (default: http://127.0.0.1:8317)'
    )
    parser.add_argument(
        '--api-key',
        default='local-api-key',
        help='API key for CLIProxyAPI (default: local-api-key)'
    )
    
    args = parser.parse_args()
    
    print(f"🎨 Generating image with {args.model}...")
    print(f"📝 Prompt: {args.prompt[:80]}...")
    if args.ref:
        print(f"📎 References: {len(args.ref)} image(s)")
    
    try:
        output_file = generate_image(
            prompt=args.prompt,
            output_path=args.output,
            model=args.model,
            proxy_url=args.proxy_url,
            api_key=args.api_key,
            reference_images=args.ref if args.ref else None
        )
        print(f"✅ Image saved to: {output_file}")
        
        # Get file size
        size = os.path.getsize(output_file)
        print(f"📦 Size: {size / 1024:.1f} KB")
        
    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
