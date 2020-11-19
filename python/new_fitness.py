import EasyGA
import serial
import time
import random
# Create the genetic algorithm
ga = EasyGA.GA()

ga.gene_impl = lambda: random.randint(1240, 1280)
ga.generation_goal = 1
ga.population_size = 4
ga.chromosome_length = 10


# Setup ardunio serial conneciton
arduino_comm_port = "/dev/ttyACM0"
ser = serial.Serial(arduino_comm_port, baudrate=9600, timeout=1)
# Allow the arduino to initialize
time.sleep(3)


def is_valid(sentString, recvString):
        if sentString in recvString:
            return True
        else:
            return False
        # string must be in this format: [1,2,3]{4,5,6}
        # string is received directly from arduino

def get_fitness(input_value):
    
    chromosome = []
    
    for gene in input_value.gene_list:
        chromosome.append(gene.value)
    
    # Goal Attributes
    max_height = 160
    target_height = 6
    fitness = 0

    # Encode chromosome into byte data to send to the ardunio
    string = '[' + ','.join(map(str, chromosome)) + ']'
    
    print("starting")
    encoded = str.encode(string)
    ser.write(encoded)
    print()
    print("Sending:")
    print("\t" + str(string))

    what_i_just_read = ser.readline().decode()  # Send command
    print(what_i_just_read)
    valid = is_valid(string, what_i_just_read)
    # [1,2,3]{4,5,6}

    while not valid:
        what_i_just_read = ser.readline().decode()
        # Valid Format - [1252,1267,1248,1264,1242,1249,1267,1265,1263,1267]{4,3,90,3,15,3,3,76,15,15}
        valid = is_valid(string, what_i_just_read)  # Waiting for correct signal

    print("Receiving:")
    print("\t" + str(what_i_just_read))

    heights = what_i_just_read.replace(string, '')  # {4,3,90,3,15,3,3,76,15,15}
    heights = heights.replace('{', '')  # 4,3,90,3,15,3,3,76,15,15}
    heights = heights.replace('}', '')  # 4,3,90,3,15,3,3,76,15,15
    # split by comma and make an int array
    heights = heights.split(',')  # 4,3,90,3,15,3,3,76,15,15 an array of strings
    heights_int = []
    for height_str in heights:
        try:
            add_height = int(height_str)
        except ValueError:
            # If the ardunio sends a wrong signal then set height manually
            add_height = 16
            print('ERROR: We got {' + height_str + '} from' + str(what_i_just_read))

        heights_int.append(min(max_height, add_height))

    fitness = 0
    for height in heights_int:
        fitness += abs(target_height - height)
    fitness /= len(chromosome) # get avg fitness for all heights

    print("\tFitness = " + str(fitness))

    return fitness


ga.fitness_function_impl = get_fitness
# Evolve the genetic algorithm
ga.evolve()

ga.print_generation()
ga.print_population()

