import json
import cv2
import os
import base64


folder="..\\frames\\"
output_dir= "..\\augmented\\"


def list_all_files(directory):
    image_ext = ["png"]
    label_ext = ["json"]
    files = os.listdir(directory)

    labels = [f for f in files if any(f.endswith(ext) for ext in label_ext)]

    # Filter images that have a matching JSON file
    images = [f for f in files if any(f.endswith(ext) for ext in image_ext) and os.path.splitext(f)[0]+".json" in labels]

    return images, labels

async def label_flip_horizontal(label, width, image):
    # Open the JSON file and load its contents
    with open(label, 'r') as f:
        labelme_data = json.load(f)

    # Extract polygons from the LabelMe JSON data
    polygons = []
    for shape in labelme_data['shapes']:
        if shape['shape_type'] == 'polygon':
            polygons.append(shape['points'])

    # Manually flip the polygons horizontally
    flipped_polygons = []
    for poly in polygons:
        flipped_poly = [[width - x, y] for x, y in poly]  # Flip X-coordinates
        flipped_polygons.append(flipped_poly)

     # Update the JSON with flipped polygons
    for i, shape in enumerate(labelme_data['shapes']):
        if shape['shape_type'] == 'polygon':
            shape['points'] = flipped_polygons[i]

    filename = os.path.basename(label)
    labelme_data['imagePath'] = output_dir + "aug_" + filename

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Encode the flipped image back to base64
    _, img_encoded = cv2.imencode('.png', image)
    img_base64 = base64.b64encode(img_encoded).decode('utf-8')
    labelme_data['imageData'] = img_base64

    return labelme_data


async def label_flip_vertically(label,height,image):
    # Open the JSON file and load its contents
    with open(label, 'r') as f:
        labelme_data = json.load(f)

    # Extract polygons from the LabelMe JSON data
    polygons = []
    for shape in labelme_data['shapes']:
        if shape['shape_type'] == 'polygon':
            polygons.append(shape['points'])

    # Manually flip the polygons horizontally
    flipped_polygons = []
    for poly in polygons:
        flipped_poly = [[x, height - y] for x, y in poly]  # Flip X-coordinates
        flipped_polygons.append(flipped_poly)

    # Update the JSON with flipped polygons
    for i, shape in enumerate(labelme_data['shapes']):
        if shape['shape_type'] == 'polygon':
            shape['points'] = flipped_polygons[i]


    filename = os.path.basename(label)
    if filename.startswith("aug_"):
        filename = filename.replace("aug_", "")
    labelme_data['imagePath'] = output_dir + "aug_" + filename

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Encode the flipped image back to base64
    _, img_encoded = cv2.imencode('.png', image)
    img_base64 = base64.b64encode(img_encoded).decode('utf-8')
    labelme_data['imageData'] = img_base64

    return labelme_data


async def read_image(image_path):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image

async def save_image(image, image_name):
    cv2.imwrite(image_name, cv2.cvtColor(image, cv2.COLOR_RGB2BGR))

async def save_label(label, label_name):
    new_path = label_name
    with open(new_path, 'w') as f:
        json.dump(label, f , indent=4)



