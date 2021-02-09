## Evolving Altitude Robot

<img width="600px" src="https://github.com/danielwilczak101/Genetic-Algorithm-Robot/blob/media/images/two_robots.jpg">


# Instructions

1. [Assemble Robot](#). 
2. [Upload Ardunio Code](https://github.com/danielwilczak101/Genetic-Algorithm-Robot/blob/main/arduino.ino). 
3. [Run Python Code](https://github.com/danielwilczak101/Genetic-Algorithm-Robot/blob/main/fitness.py). 

The purpose of the present study was to design a flight control system with no pre-determined mathematical model, but instead using a genetic algorithm to maintain the optimal altitude. The study is done through a quantitative empirical research method. In the process of conducting the research, we found that programming a genetic algorithm was cumbersome for novice users to implement. Due to this, we created and released an open source Python package called EasyGA.

An initial population of 15 chromosomes and 100 generations were used during the trial. The throttle value of the device had an associated gene value of 1 second. When the trial of hundred generations was completed, machine learning was achieved. Please refer to the graph for greater understanding. Preliminary results showed that optimizing a one DOF device, in real-time, is possible without using a pre-determined mathematical model. 


#### Example Graphs:

Total generation fitness per generation using 5 separate trials.
<img  src="https://github.com/danielwilczak101/Genetic-Algorithm-Robot/blob/media/images/kyle_total.png">

Lowest/best fitness of each generation using 5 separate trials.
<img  src="https://github.com/danielwilczak101/Genetic-Algorithm-Robot/blob/media/images/kyle_lowest.png">
