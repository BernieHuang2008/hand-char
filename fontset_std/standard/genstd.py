import yaml
from PIL import Image, ImageDraw, ImageFont

path = "fontset_std/"


def generate_image(
    id, character, font_path=path + "standard/u3000.woff2", font_size=150
):
    # Create a blank image with white background
    image = Image.new("RGB", (256, 256), "white")
    draw = ImageDraw.Draw(image)

    # Specify the font and size
    font = ImageFont.truetype(font_path, font_size)

    # Get text size
    _, _, text_width, text_height = draw.textbbox((0, 0), character, font=font)

    # Calculate position to center the text
    position = ((256 - text_width) / 2, (256 - text_height) / 2)

    # Draw the character
    draw.text(position, character, fill="black", font=font)

    # Save or display the image
    image.save(path + f"src/{id}.jpg")


def main():
    # load
    with open(path + "standard/standard.yaml", "r") as f:
        fontset = yaml.safe_load(f)

    # character -> jpg(256x256)
    for id in fontset["mapping"]["character"].keys():
        character = fontset["mapping"]["character"][id]

        if character == "":
            continue

        print(id, character)
        # generate image
        generate_image(id, character)


if __name__ == "__main__":
    main()
