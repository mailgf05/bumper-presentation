#!/usr/bin/env python3
"""
Encode all images from /tmp/bumper-pptx/images/ to base64 format.
Output will be embedded directly in the HTML presentation.
"""

import os
import base64
import json
from pathlib import Path

def encode_image_to_base64(image_path):
    """Encode an image file to base64 string."""
    try:
        with open(image_path, "rb") as image_file:
            encoded = base64.b64encode(image_file.read()).decode('utf-8')
            return encoded
    except Exception as e:
        print(f"Error encoding {image_path}: {e}")
        return None

def get_mime_type(file_path):
    """Get MIME type based on file extension."""
    ext = Path(file_path).suffix.lower()
    mime_types = {
        '.png': 'image/png',
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.gif': 'image/gif',
        '.webp': 'image/webp',
        '.svg': 'image/svg+xml'
    }
    return mime_types.get(ext, 'image/png')

def main():
    source_dir = "/tmp/bumper-pptx/images/"
    output_file = "/tmp/bumper-slides/image_data.json"

    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    image_data = {}

    # Process all image files
    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)

        # Skip if not a file
        if not os.path.isfile(file_path):
            continue

        # Get file extension and check if it's an image
        ext = Path(filename).suffix.lower()
        if ext not in ['.png', '.jpg', '.jpeg', '.gif', '.webp', '.svg']:
            continue

        print(f"Encoding: {filename}")

        # Encode image
        base64_data = encode_image_to_base64(file_path)
        if base64_data:
            mime_type = get_mime_type(file_path)
            # Remove extension for the key name
            key_name = Path(filename).stem
            image_data[key_name] = {
                'mime': mime_type,
                'data': base64_data
            }

    # Save to JSON file
    with open(output_file, 'w') as f:
        json.dump(image_data, f)

    print(f"\n✓ Encoded {len(image_data)} images")
    print(f"✓ Saved to {output_file}")
    print(f"✓ Total size: {sum(len(v['data']) for v in image_data.values()) // 1024 // 1024} MB")

if __name__ == "__main__":
    main()