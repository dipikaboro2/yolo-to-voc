# YOLO to PASCAL VOC

Converting YOLO formats to Pascal VOC format.

### Sample images with bboxes
<table>
  <tr>
    <td> <img src="yolo-annotation-images/YOLO Annotations_zebras.png" alt="yolo-elephants" ></td>
    <td> <img src="voc-annotation-images/VOC-zebras.png"  alt="voc-elephant" ></td>
   </tr> 
   <tr>
      <td> <p align="center"> YOLO annotation </p> </td>
      <td> <p align="center"> PASCAL VOC annotation </p> </td>
  </tr>
</table>

### Programs

For converting YOLO annotations to PASCAL VOC format
```
python yolo-to-voc.py
```
To visualize your YOLO annotation's bounding box
```
python yolo-visualize.py
```
To visualize your PASCAL VOC annotation's bounding box
```
python voc-visualize.py
```
To just validate your conversion:
```
python validate-conversion.py
```
