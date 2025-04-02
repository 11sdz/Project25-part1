import time

import albumentations as A
from utils import *
import os

async def flip_horizontally(image_path,label_path):
    image = await read_image(image_path)

    height,width = image.shape[:2]

    transform = A.Compose([
        A.HorizontalFlip(p=1),
        A.MotionBlur(blur_limit=3, p=0.25),
        A.MedianBlur(blur_limit=3, p=0.25),
        A.RandomShadow(p=0.25),
    ])

    image = transform(image=image)['image']
    label = await label_flip_horizontal(label_path,width,image)

    json_filename = os.path.basename(label_path)
    png_filename = os.path.basename(image_path)

    await save_label(label, "..\\augmented\\" +"aug_"+json_filename)
    await save_image(image, "..\\augmented\\" +"aug_"+png_filename)




async def flip_vertically(image_path,label_path):
    image = await read_image(image_path)
    height,width = image.shape[:2]
    transform = A.Compose([
        A.VerticalFlip(p=1),
        A.ChannelShuffle(p=0.25),
    ])

    image = transform(image=image)['image']
    label = await label_flip_vertically(label_path,height,image)

    json_filename = os.path.basename(label_path)
    png_filename = os.path.basename(image_path)

    if (json_filename.startswith("aug_")):
        json_filename = json_filename.replace("aug_", "")
        png_filename = png_filename.replace("aug_", "")


    await save_label(label, "..\\augmented\\" +"aug_"+json_filename)
    await save_image(image, "..\\augmented\\" +"aug_"+png_filename)

async def process_flip_operations(folder, image_name, label_name, output_folder, i):
    # Flip horizontally first
    await flip_horizontally(folder + image_name, folder + label_name)
    # Then flip vertically
    await flip_vertically(output_folder + "aug_" + image_name, output_folder + "aug_" + label_name)
    print(image_name)