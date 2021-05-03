## Evolving Altitude Robot
<img src="https://github.com/danielwilczak101/Evolving-altitude-robot/blob/media/images/banner_logo.jpg">

### Instructions
1. [Print and Assemble Robot](https://github.com/danielwilczak101/Evolving-altitude-robot/tree/main/3d_print_assembly). 
2. [Upload Ardunio Code](https://github.com/danielwilczak101/Evolving-altitude-robot/blob/main/arduino/arduino.ino). 
3. [Run Python Code](https://github.com/danielwilczak101/Evolving-altitude-robot/tree/main/python). 

The purpose of the present study was to design a flight control system with no pre-determined mathematical model, but instead using a genetic algorithm to maintain the optimal altitude. The study is done through a quantitative empirical research method. In the process of conducting the research, we found that programming a genetic algorithm was cumbersome for novice users to implement. Due to this, we created and released an open source Python package called [EasyGA](https://github.com/danielwilczak101/EasyGA/wiki).

An initial population of 15 chromosomes and 100 generations were used during the trial. The throttle value of the device had an associated gene value of 1 second. When the expirement of three separate robots each with a minimum of 30 trials of hundred generations was completed, machine learning was achieved. Please refer to the graph for greater understanding. Results showed that optimizing a one DOF device, in real-time, is possible without using a pre-determined mathematical model. 

### Youtube Video
Part 1(Assembly):https://www.youtube.com/watch?v=vMUrqwaEUfU  
Part 2(Code): Coming soon.  
Part 3(Results): Coming soon.  

### Experiment Data
All data is in the form of a sqlite3 database. 
1. [Kyle](https://github.com/danielwilczak101/Evolving-altitude-robot/tree/main/data). 
2. [Linda](https://github.com/danielwilczak101/Evolving-altitude-robot/tree/main/data). 
3. [Jeff](https://github.com/danielwilczak101/Evolving-altitude-robot/tree/main/data). 

## Graphs from Data:

<img width="900px"  src="https://github.com/danielwilczak101/Evolving-altitude-robot/blob/media/images/all_data.png">
Left: Average of all trials lowest chromosome. Right: All trials lowest chromosome.

