from PIL import Image, ImageFilter, JpegPresets

image = Image.open('./Image/astro.jpg')
filtered_img = image.filter(ImageFilter.BLUR)
filtered_img.save("astro_blur.png", 'png')
fi