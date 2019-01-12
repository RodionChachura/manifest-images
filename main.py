from PIL import Image
import json

from resizeimage import resizeimage

START = 1024

SIZES = [
  48,
  72,
  76,
  96,
  120,
  144,
  152,
  180,
  192,
  512
]

get_src = lambda size: 'images/{0}x{0}.png'.format(size)

# with open('images/{0}x{0}.png'.format(START), 'r+b') as f:
#   with Image.open(f) as image:
#     for size in SIZES:
#       cover = resizeimage.resize_cover(image, [size, size])
#       cover.save(get_src(size), image.format)

sizes_for_manifest = SIZES + [START]
icons_for_manifest = [
  {
    'src': 'favicon.ico',
    'sizes': '64x64 32x32 24x24 16x16',
    'type': 'image/x-icon'
  },
]
for size in sizes_for_manifest:
  icons_for_manifest.append({
    'src': get_src(size),
    'sizes': '{0}x{0}'.format(size),
    'type': 'image/png'
  })

print(json.dumps(icons_for_manifest, indent=4))