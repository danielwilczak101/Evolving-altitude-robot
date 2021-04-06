import EasyGA
import serial
import time
import random
from connection_functions import send_chromosome

# Setup ardunio serial conneciton
arduino_comm_port = "/dev/ttyACM0"
ser = serial.Serial(arduino_comm_port, baudrate=9600, timeout=1)
# Allow the arduino to initialize
time.sleep(3)

def robot_fitness(chromosome):
    """The fitness function that calulates the fitness based
    on the robots findings."""

    fitness = 0
    target_height = 6

    # Send the chromosome and return list of heights.
    fitness_array = send_chromosome(chromosome)

    # Calculate the fitness from the list
    for height in fitness_array:
        # How far away is it from the target height
        fitness += abs(target_height - height)

    return fitness


# How many times it should repeat the run
number_trials = 5

for x in range(number_trials):
    # Create the genetic algorithm
    ga = EasyGA.GA()

    # Set the fitness
    ga.fitness_function_impl = robot_fitness

    ga.gene_impl = lambda: random.randint(1250, 1270)
    ga.generation_goal = 100
    ga.population_size = 15
    ga.chromosome_length = 10
    ga.target_fitness_type = 'min'
    # Evolve the genetic algorithm
    ga.evolve()

    # Print generation and population
    ga.print_generation()
    ga.print_population()
