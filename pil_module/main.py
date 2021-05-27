from PIL import Image, ImageFilter
import os
# image = Image.open('bmw.jpg')

# print(image.size, image.mode)
# print(dir(image))
# new_image = image.convert(mode='L')
# new_image.save('./bmw_l_mode.jpg')

image = Image.open('bmw.jpg')




# image.putalpha(10)
# image.show()

# new_image = image.filter(ImageFilter.GaussianBlur(10))
# new_image.show()
# image2.thumbnail(image1.size)
# new_image = Image.blend(image1, image2, 0.5)
# new_image.show()

# for f in os.listdir('./'):
#     f_name, f_ext = os.path.splitext(f)
#     print(f_name, f_ext)
#     if f_ext == '.jpg':
#         image = Image.open(f)
#         new_image = image.rotate(90, expand=True)
#         new_image.save(f'rotated/{f}')
        
        # image = Image.open(f)
        # image.thumbnail((200,200))
        # image.save(f'new_images/{f}')
        # print(image.size)
        # new_image = image.resize((200,200))
        # new_image.save(f'new_size_images/{f}')
        # print(new_image.size)
        # new_image.rotate(90)

