import os
from PIL import Image, ImageDraw, ImageFont
from typing import List, Tuple

DIGITS = ['6', '7', '8', '9']
ROTATIONS = [0, 90, 180, 270]
IMAGE_SIZE = (128, 128)
FONT_PATH = "/System/Library/Fonts/Supplemental/Arial.ttf"

FONT_SIZE = 80
OUTPUT_DIR = "controlled_digits"
BACKGROUND_COLOR = 255
DIGIT_COLOR = 0

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
    draw.text(((IMAGE_SIZE[0] - w) / 2, (IMAGE_SIZE[1] - h) / 2), digit, font=font, fill=DIGIT_COLOR)
    return img.rotate(rotation)


def save_image(img: Image.Image, digit: str, rotation: int, label: str, output_dir: str):
    filename = f"{digit}_rot{rotation}_label{label}.png"
    filepath = os.path.join(output_dir, filename)
    img.save(filepath)

def generate_dataset(digits: List[str], rotations: List[int], output_dir: str):
    os.makedirs(output_dir, exist_ok=True)
    font = ImageFont.truetype(FONT_PATH, FONT_SIZE)

    for digit in digits:
        for rotation in rotations:
            label = get_label(digit, rotation)
            img = generate_digit_image(digit, rotation, font)
            save_image(img, digit, rotation, label, output_dir)

    print(f"Dataset successfully created in: {output_dir}")

if __name__ == "__main__":
    generate_dataset(DIGITS, ROTATIONS, OUTPUT_DIR)
