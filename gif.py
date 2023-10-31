import imageio
from PIL import Image


# filenames = ["2.png", "3.png", "4.png", "5.png", "6.png", "7.png", "8.png", "9.png", "10.png"]
# images = [Image.open(filename) for filename in filenames]
# imageio.mimsave('rotate.gif', images, fps=1, loop=0)

filenames = ["1.png", "12.png", "13.png", "14.png", "15.png", "16.png", "17.png", "18.png"]
images = [Image.open(filename) for filename in filenames]
imageio.mimsave('rotate2.gif', images, fps=2, loop=0)
