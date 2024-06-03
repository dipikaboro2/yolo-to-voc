import xml.etree.ElementTree as ET
import cv2

def visualize_voc(image_path, voc_annotation, class_names):
    image = cv2.imread(image_path)
    tree = ET.parse(voc_annotation)
    root = tree.getroot()

    for obj in root.findall('object'):
        class_name = obj.find('name').text
        bndbox = obj.find('bndbox')
        x_min = int(bndbox.find('xmin').text)
        y_min = int(bndbox.find('ymin').text)
        x_max = int(bndbox.find('xmax').text)
        y_max = int(bndbox.find('ymax').text)

        cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)
        cv2.putText(image, class_name, (x_min, y_min - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow('VOC Annotations', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


image_path = './data/images/229.jpg'
voc_annotation = './data/voc-labels/229.xml'

class_names = ['Buffalo', 'Elephant', 'Zebra']



visualize_voc(image_path, voc_annotation, class_names)
