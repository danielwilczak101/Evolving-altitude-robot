
import EasyGA
import serial
import time
import random
from connection_functions import send_chromosome

# Setup ardunio serial conneciton
arduino_comm_port = "/dev/cu.usbmodem14201"
ser = serial.Serial(arduino_comm_port, baudrate=9600, timeout=1)
# Allow the arduino to initialize
time.sleep(3)

def robot_fitness(chromosome):
    """The fitness function that calulates the fitness based
    on the robots findings."""

    # Get the global serial communication variable.
    global ser

    fitness = 0
    target_height = 6

    # Send the chromosome and return list of heights.
    fitness_array = send_chromosome(chromosome,ser)

    # Calculate the fitness from the list
    for height in fitness_array:
        # How far away is it from the target height
        fitness += abs(target_height - height)

    return fitness



# Create the genetic algorithm
ga = EasyGA.GA()

    # Set the fitness
ga.fitness_function_impl = robot_fitness

ga.gene_impl = lambda: random.randint(1250, 1270)
ga.generation_goal = 100
ga.population_size = 10
ga.chromosome_length = 10
ga.target_fitness_type = 'min'

while ga.active():
    # Evolve only a certain number of generations
    ga.evolve(1)
    # Print the worst chromosome("Smallest") from that generations population
    ga.print_worst_chromosome()
    # If you want to show each population
    #ga.print_population()
    # To divide the print to make it easier to look at
    print('-'*75)

# Print the current generation
ga.print_generation()
ga.print_population()

ga.graph.lowest_value_chromosome()
ga.graph.show()
