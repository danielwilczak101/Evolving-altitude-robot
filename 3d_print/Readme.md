## 3D Printing and assembly can be found here.

### STL Files for printing:
All the required 3D printed parts are located in one zipped file on the Thingverse linked below, download, unzip and import into your slicer software to 3D print
<table>
<thead>
<tr>
<th><strong>3D Printed Part</strong></th>
<th align="right"><strong>Quantity</strong></th>
<th><strong>URL</strong></th>
<th><strong>Material</strong></th>
<th><strong>Supports</strong></th>
<th><strong>Print Time</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>GA Front Test Stand</td>
<td align="right">1</td>
<td><a href="https://www.thingiverse.com/thing:4819932">Thingiverse</a></td>
<td>PLA</td>
<td>Yes: Touching Build Plate Only</td>
<td>10-12 hours</td>
</tr>
<tr>
<td>GA Front Back Stand</td>
<td align="right">1</td>
<td><a href="https://www.thingiverse.com/thing:4819932">Thingiverse</a></td>
<td>PLA</td>
<td>None</td>
<td>10-12 hours</td>
</tr>
<tr>
<td>EDF Holder</td>
<td align="right">1</td>
<td><a href="https://www.thingiverse.com/thing:4819932">Thingiverse</a></td>
<td>PLA</td>
<td>None</td>
<td>6-8 hours</td>
</tr>
<tr>
<td>Hole Guide</td>
<td align="right">1</td>
<td><a href="https://www.thingiverse.com/thing:4819932">Thingiverse</a></td>
<td>PLA</td>
<td>None</td>
<td>4-6 hours</td>
</tr>
</table>

### Assembly

This page details the hardware setup instructions for creating the quality GA Robot

## Tools Needed
To build the GA Robot you'll need the following tools

## **Electronics**
### Arduino Shield 

<a href="https://raw.githubusercontent.com/EREPPLab/Test_WIKI/media/Images/Arduino_Shield_Assembled.JPG">
<img  src="https://github.com/EREPPLab/Test_WIKI/blob/media/Images/Arduino_Shield_Assembled.JPG" height="240"></a>
&nbsp;
<a href="https://raw.githubusercontent.com/EREPPLab/Test_WIKI/media/Images/Arduino_Shield_Pin_Layout.JPG"><img  src="https://github.com/EREPPLab/Test_WIKI/blob/media/Images/Arduino_Shield_Pin_Layout.JPG" height="240"></a>

### Step 1 - Solder on connector pins to the Arduino Shield
1. Left side of the Arduino Shield 
    -  Top 7 pin male connector 
    -  Bottom 6 pin male connector
   
2. Right side of the Arduino Shield
    - 2x 8 pin male connectors 

3. Solder on Female JSD Connectors to the Arduino Shield
    - 4 Pin Female JSD connector facing the center of the Arduino Shield
    - 3 Pin Female JSD connector facing outward of the Arduino Shield


## Electrical 
### Wires

__(add images of wires and which connectors)__

1. Create 1 wire composed of 4 internal wires with male 4 pin JSD connector on each end
<a href="https://raw.githubusercontent.com/EREPPLab/Test_WIKI/media/Images/Arduino_Shield_Pin_Layout.JPG"><img  src="https://github.com/EREPPLab/Test_WIKI/blob/media/Images/Arduino_&_Ultrasonic_Wire_Layout_Zoom.JPG" height="240"></a>


2. Create 3 separate wires that run the length of carbon fiber tube to connect from the EDF to the ESC.
    - Each wire has one end with female 3.5mm bullet connectors and the other end with male 3.5mm bullet connectors
<a href="https://raw.githubusercontent.com/EREPPLab/Test_WIKI/media/Images/Tube_Wires_Layout.JPG">
<img  src="https://github.com/EREPPLab/Test_WIKI/blob/media/Images/Tube_Wires_Layout.JPG" height="240"></a>

<a href="https://raw.githubusercontent.com/EREPPLab/Test_WIKI/media/Images/Tube_Wires_Male_Connector.JPG">
<img  src="https://github.com/EREPPLab/Test_WIKI/blob/media/Images/Tube_Wires_Male_Connector.JPG" height="240"></a>

<a href="https://raw.githubusercontent.com/EREPPLab/Test_WIKI/media/Images/Tube_Wire_Female_Layout.JPG">
<img  src="https://github.com/EREPPLab/Test_WIKI/blob/media/Images/Tube_Wire_Female_Layout.JPG" height="240"></a>
 
<a href="https://raw.githubusercontent.com/EREPPLab/Test_WIKI/media/Images/Tube_&_Wires.JPG">
<img  src="https://github.com/EREPPLab/Test_WIKI/blob/media/Images/Tube_&_Wires.JPG" height="240"></a>


### Electronic Speed Controller (ESC)

__(add images of wires and which connectors)__
<a href="https://github.com/EREPPLab/Test_WIKI/blob/media/Images/Back_Mount_ESC_Uninstalled_XT60.jpg">
<img  src="https://github.com/EREPPLab/Test_WIKI/blob/media/Images/Back_Mount_ESC_Uninstalled_XT60.jpg" height="240"></a>


1. Solder on XT60 female connector to power cables on ESC

2. Add on 3 pin male JSD connector to ESC 5V power output

### Ultrasonic Sensor

__(add images of wires and which connectors)__

1. Add 4 pin female JSD connector to ultrasonic sensor 


## **3D Prints**

### Visit the 3D printing page below if you have not already 3D printed your parts 
[3D Printing Page](https://github.com/EREPPLab/Test_WIKI/wiki/3d-printing)

### Carbon Fiber Tube and EDF Assembly 
__(add images of 3d prints, carbon fiber tube and how to insert EDF )__

<a href="https://github.com/EREPPLab/Test_WIKI/blob/media/Images/Tube_Alignment_Tool_Uninstalled.JPG">
<img  src="https://github.com/EREPPLab/Test_WIKI/blob/media/Images/Tube_Alignment_Tool_Uninstalled.JPG" height="240"></a>

<a href="https://github.com/EREPPLab/Test_WIKI/blob/media/Images/Tube_Hole_Alignment_Installed.JPG">
<img  src="https://github.com/EREPPLab/Test_WIKI/blob/media/Images/Tube_Hole_Alignment_Installed.JPG" height="240"></a>

1. Use the 3D printed Tube Hole Guide to drill a hole in the carbon fiber tube using a 5/32 drill bit
    - Push carbon fiber tube all the way into 3D printed Tube Hole Guide until you hit the wall and then drill hole  

2. Using pliers open up the 3D printed EDF Holder and slide in the EDF to lock in place feeding the wires below
    - Feed wires into the bottom hole on the 3D printed EDF Holder 

3. Feed the 3 wires that you created earlier through the carbon fiber tube
    - Male 3.5 mm bullet connectors opposite of the end of the hole
    - Female 3.5 mm bullet connectors on the same side as the hole you drilled

4. Connect the 3 EDF female 3.5 mm bullet connectors with the 3 male 3.5 mm bullet connectors of the extension wire

5. Slide the carbon fiber tube into the 3D printed EDF Holder tucking the wires nicely into the cut out



## **Hardware Assembly**

__(add images for all steps )__

### Step 1:  Snap in place the Arduino into 3D printed Back Mount
<a href="https://raw.githubusercontent.com/EREPPLab/Test_WIKI/media/Images/Back_Mount_Arduino_Uninstalled.JPG">
<img  src="https://github.com/EREPPLab/Test_WIKI/blob/media/Images/Back_Mount_Arduino_Uninstalled.JPG" height="240"></a>

<a href="https://raw.githubusercontent.com/EREPPLab/Test_WIKI/media/Images/Back_Mount_Arduino_part1_insert.JPG">
<img  src="https://github.com/EREPPLab/Test_WIKI/blob/media/Images/Back_Mount_Arduino_part1_insert.JPG" height="240"></a>

<a href="https://raw.githubusercontent.com/EREPPLab/Test_WIKI/media/Images/Back_Mount_Arduino_Installed.JPG">
<img  src="https://github.com/EREPPLab/Test_WIKI/blob/media/Images/Back_Mount_Arduino_Installed.JPG" height="240"></a>

<a href="https://raw.githubusercontent.com/EREPPLab/Test_WIKI/media/Images/Back_Mount_Arduino_Installed2.JPG">
<img  src="https://github.com/EREPPLab/Test_WIKI/blob/media/Images/Back_Mount_Arduino_Installed2.JPG" height="240"></a>


### Step 2:  Snap in place the Ultrasonic sensor into 3D printed Front Mount

<a href="https://raw.githubusercontent.com/EREPPLab/Test_WIKI/media/Images/Front_Mount_Ultrasonic_Outside.JPG">
<img  src="https://github.com/EREPPLab/Test_WIKI/blob/media/Images/Front_Mount_Ultrasonic_Outside.JPG" height="240"></a>

<a href="https://raw.githubusercontent.com/EREPPLab/Test_WIKI/media/Images/Front_Mount_Ultrasonic_Inserted.JPG">
<img  src="https://github.com/EREPPLab/Test_WIKI/blob/media/Images/Front_Mount_Ultrasonic_Inserted.JPG" height="240"></a>


### Step 3:  Slide the Front 3D printed Mount into the Back 3D printed Mount

<a href="https://raw.githubusercontent.com/EREPPLab/Test_WIKI/media/Images/Frount_Back_Mounts_Unassembled.JPG">
<img  src="https://github.com/EREPPLab/Test_WIKI/blob/media/Images/Frount_Back_Mounts_Unassembled.JPG" height="240"></a>

<a href="https://raw.githubusercontent.com/EREPPLab/Test_WIKI/media/Images/Front_Back_Mount_Wire_Connected.JPG">
<img  src="https://github.com/EREPPLab/Test_WIKI/blob/media/Images/Front_Back_Mount_Wire_Connected.JPG" height="240"></a>

### Step 4:  Connect the 4 pin JSD connector wire from the ultrasonic sensor to Arduino shield 4 pin Female JSD connector


### Step 5:  Insert the ESC into the 3D printed Back Mount 
    - 3.5 mm Bullet Connectors and XT60 connector stays sticking out the back
    - Only 3 pin JSD connector feeds through hole to connect to Arduino Shield
<a href="https://raw.githubusercontent.com/EREPPLab/Test_WIKI/media/Images/Back_Mount_ESC_Uninstalled.JPG">
<img  src="https://github.com/EREPPLab/Test_WIKI/blob/media/Images/Back_Mount_ESC_Uninstalled.JPG" height="240"></a>

<a href="https://raw.githubusercontent.com/EREPPLab/Test_WIKI/media/Images/Back_Mount_ESC_Installed.JPG">
<img  src="https://github.com/EREPPLab/Test_WIKI/blob/media/Images/Back_Mount_ESC_Installed.JPG" height="240"></a>

<a href="https://raw.githubusercontent.com/EREPPLab/Test_WIKI/media/Images/Back_Mount_ESC_Installed2.JPG">
<img  src="https://github.com/EREPPLab/Test_WIKI/blob/media/Images/Back_Mount_ESC_Installed2.JPG" height="240"></a>



### Step 6: Connect the ESC 3 pin male JSD connector to the Arduino Shield 3 pin female connector  

<a href="https://raw.githubusercontent.com/EREPPLab/Test_WIKI/media/Images/Back_Mount_ESC&Arduino_Installed.JPG">
<img  src="https://github.com/EREPPLab/Test_WIKI/blob/media/Images/Back_Mount_ESC&Arduino_Installed.JPG" height="240"></a>

<a href="https://raw.githubusercontent.com/EREPPLab/Test_WIKI/media/Images/Back_Mount_ESC_plugedin_Arduino.JPG">
<img  src="https://github.com/EREPPLab/Test_WIKI/blob/media/Images/Back_Mount_ESC_plugedin_Arduino.JPG" height="240"></a>


### Step 7: Line up the Carbon Fiber Drilled Hole with the hole on the Back Mount and insert screw to secure tube in place
    - Make sure to not to tighten bolt too tight allow the carbon fiber tube to easily pivot up and down

### Step 8: Connect the EDF extension wire 3.5 mm male bullet connectors to the ESC 3.5 mm female bullet connectors 
    - If the EDF is spinning the wrong direction swap one of these wires with another

<a href="https://raw.githubusercontent.com/EREPPLab/Test_WIKI/media/Images/Mount_&_Tube_ESC_wires_unconnected.JPG">
<img  src="https://github.com/EREPPLab/Test_WIKI/blob/media/Images/Mount_&_Tube_ESC_wires_unconnected.JPG" height="240"></a>

<a href="https://raw.githubusercontent.com/EREPPLab/Test_WIKI/media/Images/Mount_&_ESC_Wires_UnConnected_Zoom.JPG">
<img  src="https://github.com/EREPPLab/Test_WIKI/blob/media/Images/Mount_&_ESC_Wires_UnConnected_Zoom.JPG" height="240"></a>

<a href="https://raw.githubusercontent.com/EREPPLab/Test_WIKI/media/Images/Mount_&_ESC_Wires_Connected.JPG">
<img  src="https://github.com/EREPPLab/Test_WIKI/blob/media/Images/Mount_&_ESC_Wires_Connected.JPG" height="240"></a>

<a href="https://raw.githubusercontent.com/EREPPLab/Test_WIKI/media/Images/Mount_&_ESC_Wires_Connected_Zoom.JPG">
<img  src="https://github.com/EREPPLab/Test_WIKI/blob/media/Images/Mount_&_ESC_Wires_Connected_Zoom.JPG" height="240"></a>

### Congrats your done setting up the Hardware! 

