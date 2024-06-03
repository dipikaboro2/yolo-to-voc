import xml.etree.ElementTree as ET
import cv2

def validate_conversion(yolo_annotation, voc_annotation, image_width, image_height):
    with open(yolo_annotation, 'r') as f:
        yolo_boxes = [list(map(float, line.split())) for line in f.readlines()]

    tree = ET.parse(voc_annotation)
    root = tree.getroot()
    voc_boxes = []
    for obj in root.findall('object'):
        bndbox = obj.find('bndbox')
        xmin = int(bndbox.find('xmin').text)
        ymin = int(bndbox.find('ymin').text)
        xmax = int(bndbox.find('xmax').text)
        ymax = int(bndbox.find('ymax').text)
        class_name = obj.find('name').text
        voc_boxes.append([xmin, ymin, xmax, ymax, class_name])

    for yolo_box, voc_box in zip(yolo_boxes, voc_boxes):
        class_id, x_center, y_center, box_width, box_height = yolo_box
        x_center *= image_width
        y_center *= image_height
        box_width *= image_width
        box_height *= image_height

        yolo_xmin = int(x_center - (box_width / 2))
        yolo_ymin = int(y_center - (box_height / 2))
        yolo_xmax = int(x_center + (box_width / 2))
        yolo_ymax = int(y_center + (box_height / 2))

        voc_xmin, voc_ymin, voc_xmax, voc_ymax, class_name = voc_box

        assert yolo_xmin == voc_xmin and yolo_ymin == voc_ymin and yolo_xmax == voc_xmax and yolo_ymax == voc_ymax, "Mismatch found"
    print("All annotations match!")

yolo_annotation = "./data/labels/001.txt"
voc_annotation = "./data/voc-labels/001.xml"
image_width = 800 # Replace with the actual width of your image
image_height = 411  # Replace with the actual height of your image

validate_conversion(yolo_annotation, voc_annotation, image_width, image_height)
