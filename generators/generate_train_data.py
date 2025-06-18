import os
import random
from PIL import Image, ImageDraw, ImageFont
from typing import List

# Configuration
DIGITS = ['6', '7', '8', '9']
ROTATIONS = [0, 90, 180, 270]
FONT_PATH = "/System/Library/Fonts/Supplemental/Arial.ttf"  # Use a valid font path on your system
FONT_SIZE = 80
IMAGE_SIZE = (128, 128)
OUTPUT_DIR = "train_digits"
NUM_SAMPLES_PER_LABEL = 100  # e.g. 100 images per final label (after rotation)

# Colors
BACKGROUND_COLOR = 255  # white
DIGIT_COLOR = 0         # black

def get_label(digit: str, rotation: int) -> str:
    if digit == '6' and rotation == 180:
        return '9'
    elif digit == '9' and rotation == 180:
        return '6'
    else:
        return digit

def generate_digit_image(digit: str, rotation: int, font: ImageFont.FreeTypeFont) -> Image.Image:
    img = Image.new('L', IMAGE_SIZE, color=BACKGROUND_COLOR)
    draw = ImageDraw.Draw(img)
    bbox = draw.textbbox((0, 0), digit, font=font)
    w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]

    # Slight random positioning jitter
    dx = random.randint(-5, 5)
    dy = random.randint(-5, 5)
    position = ((IMAGE_SIZE[0] - w) // 2 + dx, (IMAGE_SIZE[1] - h) // 2 + dy)
    
    draw.text(position, digit, font=font, fill=DIGIT_COLOR)
    return img.rotate(rotation)

def save_image(img: Image.Image, digit: str, rotation: int, label: str, count: int):
    label_dir = os.path.join(OUTPUT_DIR, label)
    os.makedirs(label_dir, exist_ok=True)
    filename = f"digit_{digit}_rot{rotation}_label{label}_{count}.png"
    img.save(os.path.join(label_dir, filename))


def generate_training_data( ):
    font = ImageFont.truetype(FONT_PATH, FONT_SIZE)

    label_counts = {label: 0 for label in DIGITS}

    while any(count < NUM_SAMPLES_PER_LABEL for count in label_counts.values()):
        digit = random.choice(DIGITS)
        rotation = random.choice(ROTATIONS)
        label = get_label(digit, rotation)

        if label_counts[label] >= NUM_SAMPLES_PER_LABEL:
            continue

        img = generate_digit_image(digit, rotation, font)
        save_image(img, digit, rotation, label, label_counts[label])

        label_counts[label] += 1

    print(f"Training data created in: {OUTPUT_DIR}")

if __name__ == "__main__":
    generate_training_data()
