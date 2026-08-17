#!/usr/bin/env python3
from pathlib import Path
from tempfile import TemporaryDirectory

from PIL import Image, ImageDraw

from cutout import remove_background


def test_enclosed_white_is_preserved() -> None:
    with TemporaryDirectory() as directory:
        source = Path(directory) / "source.png"
        output = Path(directory) / "output.png"
        image = Image.new("RGB", (32, 32), "white")
        ImageDraw.Draw(image).rectangle((8, 8, 23, 23), outline="black", width=2)
        image.save(source)

        remove_background(source, output)
        result = Image.open(output).convert("RGBA")
        assert result.getpixel((0, 0))[3] == 0
        assert result.getpixel((16, 16))[3] == 255


if __name__ == "__main__":
    test_enclosed_white_is_preserved()
    print("ok")
