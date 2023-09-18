from PIL import Image

Dither = Image.Dither

feedback_loop = Image.open('003_ouroboros/ouroboros.png').convert(mode='1', dither=Dither.FLOYDSTEINBERG)

feedback_fs = feedback_loop.save("003_ouroboros/ouroboros_fs.png")

