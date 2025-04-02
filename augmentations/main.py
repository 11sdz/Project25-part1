import asyncio
import random


from utils import *
from augmentations import *

folder="../frames\\"
output_folder= "../augmented\\"

if __name__ == '__main__':
    data_path = "../frames"
    data = list_all_files(data_path)

    count_h=0
    count_v=0
    count_b=0
    count_z=0

    for i in range(len(data[0])):
        p=random.random()
        if p < 0.5:
            count_z+=1
            continue
        image_name = data[0][i]
        label_name = data[1][i]

        if p < 0.6:
            asyncio.run(process_flip_operations(folder, image_name, label_name, output_folder, i))
            count_b+=1
            continue
        if p < 0.8:
            asyncio.run(flip_horizontally(folder + image_name, folder + label_name))
            count_h+=1
            continue
        if p <=1:
            asyncio.run(flip_vertically(folder + image_name, folder + label_name))
            count_v+=1

    print("v and h=",count_b)
    print("z=",count_z)
    print("v=",count_v)
    print("h=",count_h)

    print("sum",count_b+count_z+count_v+count_h)