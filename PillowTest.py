from PIL import Image, ImageFilter

with Image.open('test.jpg') as im:
    # 如下是类型注解这样三方库就会有智能提示了
    # """:type : Image.Image"""
    assert isinstance(im, Image.Image)

    w, h = im.size
    print('Original image size: %sx%s' % (w, h))

    im.thumbnail((w / 2, h / 2))
    print('Resize image size: %sx%s' % (im.size[0], im.size[1]))
    im.save('thumbnail.jpg', 'jpeg')

    im2 = im.filter(ImageFilter.BLUR)
    im2.save('blur.jpg', 'jpeg')
