from pathlib import Path
from PIL import Image, ImageOps, ImageFilter, ImageEnhance, ImageDraw

images_dir = Path('/Users/moc/repos/all_things_coding/2026/croc/src/assets/images')
ordered_names = [
    'croc8.jpeg',
    'croc4.jpeg',
    'croc1.jpeg',
    'croc5.jpeg',
    'croc2.JPG',
    'croc3.jpeg',
    'croc6.jpeg',
    'croc4.jpeg',
]
files = [images_dir / name for name in ordered_names if (images_dir / name).exists()]

for path in files:
    img = Image.open(path)
    img = ImageOps.exif_transpose(img)
    if img.mode not in ('RGB', 'RGBA'):
        img = img.convert('RGB')
    img.thumbnail((1800, 1800), Image.Resampling.LANCZOS)
    save_kwargs = {'optimize': True}
    if path.suffix.lower() in {'.jpg', '.jpeg'}:
        if img.mode == 'RGBA':
            img = img.convert('RGB')
        save_kwargs.update({'quality': 82, 'progressive': True})
    else:
        save_kwargs.update({'compress_level': 9})
    img.save(path, **save_kwargs)

canvas_w, canvas_h = 2200, 1400
canvas = Image.new('RGB', (canvas_w, canvas_h), '#e8d3ef')
placements = [
    (0, 0, 1180, 860),
    (1180, 0, 540, 430),
    (1720, 0, 480, 430),
    (1180, 430, 540, 430),
    (1720, 430, 480, 430),
    (0, 860, 700, 540),
    (700, 860, 720, 540),
    (1420, 860, 780, 540),
]

def cover_crop(img, size):
    img = ImageOps.exif_transpose(img)
    if img.mode != 'RGB':
        img = img.convert('RGB')
    return ImageOps.fit(img, size, method=Image.Resampling.LANCZOS, centering=(0.5, 0.5))

for idx, rect in enumerate(placements[: len(files)]):
    x, y, w, h = rect
    tile = cover_crop(Image.open(files[idx]), (w, h))
    tile = ImageEnhance.Color(tile).enhance(1.03)
    tile = ImageEnhance.Contrast(tile).enhance(1.04)
    tile = tile.filter(ImageFilter.GaussianBlur(radius=0.12))
    canvas.paste(tile, (x, y))

overlay = Image.new('RGBA', (canvas_w, canvas_h), (0, 0, 0, 0))
draw = ImageDraw.Draw(overlay)
for i, (x, y, w, h) in enumerate(placements[: len(files)]):
    outline = (245, 237, 247, 220) if i == 0 else (245, 237, 247, 175)
    width = 5 if i == 0 else 3
    draw.rounded_rectangle(
        (x + 6, y + 6, x + w - 6, y + h - 6),
        radius=20,
        outline=outline,
        width=width,
    )
canvas = Image.alpha_composite(canvas.convert('RGBA'), overlay)

shade = Image.new('RGBA', (canvas_w, canvas_h), (0, 0, 0, 0))
shade_draw = ImageDraw.Draw(shade)
shade_draw.rectangle((0, 0, canvas_w, canvas_h), fill=(46, 26, 68, 18))
shade_draw.rectangle((0, int(canvas_h * 0.5), canvas_w, canvas_h), fill=(16, 20, 25, 86))
canvas = Image.alpha_composite(canvas, shade).convert('RGB')

out = images_dir / 'hero_collage_croc.jpg'
canvas.save(out, quality=84, optimize=True, progressive=True)
print(f'created weighted collage with croc8 as hero: {out.name}')
