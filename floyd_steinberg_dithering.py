from PIL import Image

Dither = Image.Dither

img_bp = Image.open('000_loop/breakpoint.png').convert(mode='1', dither=Dither.FLOYDSTEINBERG)


bp_fs = img_bp.save("bp_fs.png")
img_loop = Image.open('000_loop/loop.png').convert(mode='1', dither=Dither.FLOYDSTEINBERG)



loop_fs = img_loop.save("loop_fs.png")


feedback_loop = Image.open('000_loop/feedback_loop.png').convert(mode='1', dither=Dither.FLOYDSTEINBERG)

feedback_fs = feedback_loop.save("feedback_fs.png")

