import cv2

def visualize_yolo(image_path, yolo_annotation, class_names):
    image = cv2.imread(image_path)
    height, width, _ = image.shape

    with open(yolo_annotation, 'r') as f:
        for line in f:
            class_id, x_center, y_center, box_width, box_height = map(float, line.split())
            x_center *= width
            y_center *= height
            box_width *= width
            box_height *= height

            x_min = int(x_center - (box_width / 2))
            y_min = int(y_center - (box_height / 2))
            x_max = int(x_center + (box_width / 2))
            y_max = int(y_center + (box_height / 2))

            cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)
            cv2.putText(image, class_names[int(class_id)], (x_min, y_min - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow('YOLO Annotations', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

image_path = './data/images/005.jpg'
yolo_annotation = './data/labels/005.txt'

class_names = ['Buffalo', 'Elephant', 'Zebra']

visualize_yolo(image_path, yolo_annotation, class_names)
