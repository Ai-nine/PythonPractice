# *************************************************************************
#
# @Time : 2022/9/23 11:18                                                 *
# @Author :       ________  ___  ___  ___      ___    ___ ___  ___        *
#                |\_____  \|\  \|\  \|\  \    |\  \  /  /|\  \|\  \       *
#                 \|___/  /\ \  \\\  \ \  \   \ \  \/  / | \  \\\  \      *
#                     /  / /\ \   __  \ \  \   \ \    / / \ \  \\\  \     *
#                    /  /_/__\ \  \ \  \ \  \   \/  /  /   \ \  \\\  \    *
#                   |\________\ \__\ \__\ \__\__/  / /      \ \_______\   *
#                    \|_______|\|__|\|__|\|__|\___/ /        \|_______|   *
#                                           \|___|/                       *
# base_api.py
#                                                                         *
# *************************************************************************

from PIL import Image, ImageDraw, ImageFont


def little_red_dot(imagepath, num):
    image = Image.open(fp=imagepath, mode='r')

    w, h = image.size
    font = ImageFont.truetype('fonts/Arial.ttf', size=int(h / 4.9))
    draw = ImageDraw.Draw(image)  # 创建画布

    draw.pieslice([(w / 3 * 2, 0), (w, h / 3)], start=0, end=360, fill='red')

    if 1 <= num <= 9:
        draw.text((w * 0.78, h * 0.05), f'{num}', fill='white', font=font)
    elif 10 <= num <= 99:
        draw.text((w * 0.73, h * 0.05), f'{num}', fill='white', font=font)
    else:
        draw.text((w * 0.68, h * 0.05), '99+', fill='white', font=font)

    image.save(f'outpictures/666.png')
    image.show()


if __name__ == '__main__':
    little_red_dot('pictures/b_d412.jpg', 51)
