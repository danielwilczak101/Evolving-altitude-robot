## Evolving Altitude Robot

<img width="600px" src="https://github.com/danielwilczak101/Genetic-Algorithm-Robot/blob/media/images/two_robots.jpg">


# Instructions

1. [Assemble Robot](#). 
2. [Upload Ardunio Code](https://github.com/danielwilczak101/Genetic-Algorithm-Robot/blob/main/arduino.ino). 
3. [Run Python Code](https://github.com/danielwilczak101/Genetic-Algorithm-Robot/blob/main/fitness.py). 

The purpose of the present study was to design a flight control system with no pre-determined mathematical model, but instead using a genetic algorithm to maintain the optimal altitude. The study is done through a quantitative empirical research method. In the process of conducting the research, we found that programming a genetic algorithm was cumbersome for novice users to implement. Due to this, we created and released an open source Python package called EasyGA.

An initial population of 15 chromosomes and 100 generations were used during the trial. The throttle value of the device had an associated gene value of 1 second. When the trial of hundred generations was completed, machine learning was achieved. Please refer to the graph for greater understanding. Preliminary results showed that optimizing a one DOF device, in real-time, is possible without using a pre-determined mathematical model. 


#### Data from experiments:

# Linda:
Total generation fitness for all trials.
<img width="900px"  src="https://github.com/danielwilczak101/Evolving-altitude-robot/blob/main/graphs/Linda/Generation_data.png">

Lowest value chromosome for each generation of all trial runs.
<img width="900px"  src="https://github.com/danielwilczak101/Evolving-altitude-robot/blob/main/graphs/Linda/Lowest_chromsome.png">


# Kyle:
Total generation fitness for all trials.
<img width="900px"  src="https://github.com/danielwilczak101/Evolving-altitude-robot/blob/main/graphs/Kyle/Generation_data.png">

Lowest value chromosome for each generation of all trial runs.
<img width="900px"  src="https://github.com/danielwilczak101/Evolving-altitude-robot/blob/main/graphs/Kyle/Lowest_chromosome.png">


# Jeff:

Total generation fitness for all trials.
<img width="900px"  src="https://github.com/danielwilczak101/Evolving-altitude-robot/blob/main/graphs/Jeff/generation_data.png">

Lowest value chromosome for each generation of all trial runs.
<img width="900px"  src="https://github.com/danielwilczak101/Evolving-altitude-robot/blob/main/graphs/Jeff/lowest_chromosome.png">
