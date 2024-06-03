import os
import cv2
from xml.dom.minidom import parseString
import xml.etree.ElementTree as ET
import numpy as np
from os.path import join


YOLO_CLASSES = class_names = ['Buffalo', 'Elephant', 'Zebra']

def unconvert(class_id, width, height, x, y, w, h):

    xmax = int((x*width) + (w * width)/2.0)
    xmin = int((x*width) - (w * width)/2.0)
    ymax = int((y*height) + (h * height)/2.0)
    ymin = int((y*height) - (h * height)/2.0)
    class_id = int(class_id)
    return (class_id, xmin, xmax, ymin, ymax)

ROOT = 'data'


def xml_transform(root, classes):  
    class_path  = join(root, 'labels')
    ids = list()
    l=os.listdir(class_path)
    
    check = '.DS_Store' in l
    if check == True:
        l.remove('.DS_Store')
        
    ids=[x.split('.')[0] for x in l]   

    anno_path = join(root, 'labels', '%s.txt')
    img_path = join(root, 'images', '%s.jpg')
    
    os.makedirs(join(root, 'voc-labels'), exist_ok=True)
    outpath = join(root, 'voc-labels', '%s.xml')

    for i in range(len(ids)):
        img_id = ids[i] 
        if img_id == "classes":
            continue
        if os.path.exists(outpath % img_id):
            continue
        print(img_path % img_id)
        img= cv2.imread(img_path % img_id)
        print(img.shape)
        height, width, channels = img.shape

        node_root = ET.Element('annotation')
        node_folder = ET.SubElement(node_root, 'folder')
        node_folder.text = ''
        img_name = img_id + '.jpg'
        node_filename = ET.SubElement(node_root, 'filename')
        node_filename.text = img_name
        node_source= ET.SubElement(node_root, 'source')
        node_database = ET.SubElement(node_source, 'database')
        node_database.text = ''
        node_size = ET.SubElement(node_root, 'size')
        node_width = ET.SubElement(node_size, 'width')
        node_width.text = str(width)
        node_height = ET.SubElement(node_size, 'height')
        node_height.text = str(height)
        node_depth = ET.SubElement(node_size, 'depth')
        node_depth.text = str(channels)
        node_segmented = ET.SubElement(node_root, 'segmented')
        node_segmented.text = '0'

        target = (anno_path % img_id)
        if os.path.exists(target):
            label_norm= np.loadtxt(target).reshape(-1, 5)

            for i in range(len(label_norm)):
                labels_conv = label_norm[i]
                new_label = unconvert(labels_conv[0], width, height, labels_conv[1], labels_conv[2], labels_conv[3], labels_conv[4])
                node_object = ET.SubElement(node_root, 'object')
                node_name = ET.SubElement(node_object, 'name')
                node_name.text = classes[new_label[0]]
                node_pose = ET.SubElement(node_object, 'pose')
                node_pose.text = 'Unspecified'
                node_truncated = ET.SubElement(node_object, 'truncated')
                node_truncated.text = '0'
                node_difficult = ET.SubElement(node_object, 'difficult')
                node_difficult.text = '0'
                node_bndbox = ET.SubElement(node_object, 'bndbox')
                node_xmin = ET.SubElement(node_bndbox, 'xmin')
                node_xmin.text = str(new_label[1])
                node_ymin = ET.SubElement(node_bndbox, 'ymin')
                node_ymin.text = str(new_label[3])
                node_xmax = ET.SubElement(node_bndbox, 'xmax')
                node_xmax.text =  str(new_label[2])
                node_ymax = ET.SubElement(node_bndbox, 'ymax')
                node_ymax.text = str(new_label[4])
                xml = ET.tostring(node_root)  
                dom = parseString(xml)

        print(xml)  
        f =  open(outpath % img_id, "wb")
        f.write(xml)
        f.close()     
       

xml_transform(ROOT, YOLO_CLASSES)
