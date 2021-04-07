def is_valid(sentString, recvString):
    """Check to see if the value recieved has the command inside of it.String
    is received directly from arduino.
    Rule: string must be in this format: [1,2,3]{4,5,6}
    """
    if sentString in recvString:
        return True
    else:
        return False

def height_str_to_int(heights):
    """Change a string of heights in a list of heights while also error checking"""

    # Max height the reader should read. Anything above this is an error
    max_height = 80
    heights_int = []

    for height_str in heights:
        try:
            # Convert height value
            add_height = float(height_str)
        except ValueError:
            # If the ardunio sends a wrong signal then set height manually
            add_height = 0
            print(f"ERROR: We got: { height_str }")

        # Add it to the list while also checking if its lower then the threshold
        heights_int.append(min(max_height, add_height))

    return heights_int


def send_chromosome(chromosome,ser):
    """Send the chromosome to the ardunio. This function takes in a chromosome
    parses it. Sends it to the ardunio via serial and then decodes the recieved
    values in the form [Commands list]{Fitness list}."""


    # Height were the reading is probably and error
    max_height = 160

    # Parse the chromosome object into a list
    chromosome = [gene.value for gene in chromosome.gene_list]

    # Encode chromosome into byte data to send to the ardunio
    chromosome_string = '[' + ','.join(map(str, chromosome)) + ']'
    encoded_chromosome = str.encode(chromosome_string)

    # Send the encoded chromosome to the ardunio
    ser.write(encoded_chromosome)

    # Wait and listin for the response from the ardunio
    what_i_just_read = ser.readline().decode()
    # Check to see if the data sent back in in the correct form: [1,2,3]{4,5,6}
    valid = is_valid(chromosome_string, what_i_just_read)

    # Check if its valid: Valid Format - [1252,1267,1248]{4,3,90}
    while not valid:
        # Waiting for correct signal
        what_i_just_read = ser.readline().decode()
        valid = is_valid(chromosome_string, what_i_just_read)

    # Parse the recieved string into a height list: Ex:[1,2,3]{1,2,3} - [1,2,3]
    heights = what_i_just_read.replace(chromosome_string, '')
    # Remove brackets and split the string useing the comma as a dilimiter
    heights = heights.replace('}','').replace('{','')
    heights = heights.split(',')
    # Parse and error check the heights
    heights_int = height_str_to_int(heights)

    return heights_int


