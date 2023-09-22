from PIL import Image

Dither = Image.Dither

feedback_loop = Image.open('008_regret/regret_screenshot.png').convert(mode='1', dither=Dither.FLOYDSTEINBERG)

feedback_fs = feedback_loop.save("008_regret/regret_fs.png")

