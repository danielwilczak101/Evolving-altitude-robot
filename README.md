# Genetic Algorithm Fitness
We use the EasyGA python package and some ardunio code to use the robot. Check out the python [Fitness](https://github.com/danielwilczak101/Genetic-Algorithm-Robot/blob/main/python/new_fitness.py).

## Genetic-Algorithm-Robot

<img src="https://github.com/danielwilczak101/Genetic-Algorithm-Robot/blob/media/images/two_robots.jpg">


# Instructions

1.Assemble Robot
2. Upload ardunio
3. Run Python Code

### Python Code
```Python
import EasyGA
import serial
import time
import random

# Setup ardunio serial conneciton
arduino_comm_port = "/dev/ttyACM0"
ser = serial.Serial(arduino_comm_port, baudrate=9600, timeout=1)
# Allow the arduino to initialize
time.sleep(3)


# Create the genetic algorithm
ga = EasyGA.GA()

ga.gene_impl = lambda: random.randint(1240, 1280)
ga.generation_goal = 1
ga.population_size = 4
ga.chromosome_length = 10

def ga_robot_fitness(chromosome):
    """The fitness function that calulates the fitness based
    on the robots findings."""
    
    fitness = 0
    target_height = 6
    
    # Send the chromosome
    fitness_array = send_chromosome(chromosome)
    
    # Calculate the fitness from the list
    for height in fitness_array:
        fitness += abs(target_height - height)

    return fitness


# Set the fitness
ga.fitness_function_impl = ga_robot_fitness
# Evolve the genetic algorithm
ga.evolve()

# Print generation and population
ga.print_generation()
ga.print_population()

```

#### Ouput:
```bash
Output goes here
```
