from pathlib import Path
from PIL import Image, ImageOps, ImageFilter, ImageEnhance, ImageDraw

images_dir = Path('/Users/moc/repos/all_things_coding/2026/croc/src/assets/images')
files = sorted(
    [
        p
        for p in images_dir.iterdir()
        if p.suffix.lower() in {'.jpg', '.jpeg', '.png'}
        and p.name not in {'collage_croc.png', 'hero_collage_croc.jpg', 'fb_cover.png'}
    ]
)

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
    (0, 0, 920, 700),
    (920, 0, 640, 470),
    (1560, 0, 640, 470),
    (920, 470, 420, 460),
    (1340, 470, 420, 460),
    (1760, 470, 440, 460),
    (0, 700, 560, 700),
    (560, 700, 620, 700),
    (1180, 930, 500, 470),
    (1680, 930, 520, 470),
]

def cover_crop(img, size):
    img = ImageOps.exif_transpose(img)
    if img.mode != 'RGB':
        img = img.convert('RGB')
    return ImageOps.fit(img, size, method=Image.Resampling.LANCZOS, centering=(0.5, 0.5))

for idx, rect in enumerate(placements[: len(files)]):
    x, y, w, h = rect
    tile = cover_crop(Image.open(files[idx]), (w, h))
    tile = ImageEnhance.Color(tile).enhance(1.02)
    tile = ImageEnhance.Contrast(tile).enhance(1.03)
    tile = tile.filter(ImageFilter.GaussianBlur(radius=0.2))
    canvas.paste(tile, (x, y))

overlay = Image.new('RGBA', (canvas_w, canvas_h), (0, 0, 0, 0))
draw = ImageDraw.Draw(overlay)
for x, y, w, h in placements[: len(files)]:
    draw.rounded_rectangle(
        (x + 6, y + 6, x + w - 6, y + h - 6),
        radius=18,
        outline=(245, 237, 247, 190),
        width=3,
    )
canvas = Image.alpha_composite(canvas.convert('RGBA'), overlay)

shade = Image.new('RGBA', (canvas_w, canvas_h), (0, 0, 0, 0))
shade_draw = ImageDraw.Draw(shade)
shade_draw.rectangle((0, 0, canvas_w, canvas_h), fill=(46, 26, 68, 26))
shade_draw.rectangle((0, int(canvas_h * 0.52), canvas_w, canvas_h), fill=(16, 20, 25, 78))
canvas = Image.alpha_composite(canvas, shade).convert('RGB')

out = images_dir / 'hero_collage_croc.jpg'
canvas.save(out, quality=84, optimize=True, progressive=True)
print(f'optimised {len(files)} images and created {out.name}')
