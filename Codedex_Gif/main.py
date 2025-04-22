import imageio.v3 as iio
filenames = ['nyan_cat1.png', 'nyan_cat2.png', 'nyan_cat3.png']
images = []
for filename in filenames:
    images.append(iio.imread(filename))
iio.imwrite('nyan.gif', images, duration = 100, loop = 0)