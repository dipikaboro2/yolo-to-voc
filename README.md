# YOLO to PASCAL VOC

Converting YOLO formats to Pascal VOC format.

### Sample images with bboxes
<table>
  <tr>
    <td> <img src="voc-annotation-images/VOC-elephants.png"  alt="voc-elephant" ></td>
    <td> <img src="voc-annotation-images/VOC-elephants.png" alt="yolo-elephants" ></td>
   </tr> 
   <tr>
      <td><i>Medford, MA: I-93, near Exit 21.</i> (https://maps.app.goo.gl/muLRTy4BFLoJyUoj7) </td>
      <td><i>Danvers, MA: I-93, near Exit 10.</i> (https://maps.app.goo.gl/j4ysifxbs8VmehxP6) </td>
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
