//from serial port input (via serial monitor)
//serial monitor if desired
// * is used as the data string delimiter
// , is used to delimit individual data

#include <Servo.h>
#include <MemoryFree.h>
Servo myservo;  // create servo object to control a servo

// PIN SETUP
int pin = 11; // FAN - PWM pin

const int trigPin = 10;  // Sensor - TRIG Pin
const int echoPin = 9; // Sensor - ECHO Pin

String string = "";
int throttleDelayValue = 250; // in ms, between each individual throttle value
int commandDelayValue = 3000; // in ms, between entire commands of getFitness from python

int getNumElements(String string)
{
  // Count number of elements by counting number of commas+1.
  int numCommas = 0;
  for(int i = 0; i < string.length(); i++)
  {
    char c = string.charAt(i);
    if(c == ',')
    {
      numCommas += 1;
    }
  }
  int numElements = numCommas + 1; // "12, 2, 3" => 2 commas => 3 elements
  return numElements;
}

int* parseString(String string)
{
  // Returns an integer array parsed
  // I.e, input = "[1, 2, 3]"
  // should output int array with [1, 2, 3]

  int arraySize = getNumElements(string);
  int* arr = new int[arraySize];
  String temp = "";
  int arrayIndex = 0;
  for(int i = 0; i < string.length(); i++)
  {
    char c = string.charAt(i);
    if(c == '[')
    {
      // Skip the start/end delimiters
      continue;
    }

    if(c == ',' || c == ']')
    {
      // If its a comma, we finished parsing 1 number, lets cast it to an int and add it the array
      int casted = temp.toInt();
      arr[arrayIndex] = casted;
      temp = "";
      arrayIndex += 1;
    }
    else
    {
      // If its not comma, then its a digit (so add it to a temporary string so we can read numbers)
      temp += c;
    }
  }

  return arr;
}

int execute(int throttleValue) // returns the height from this execution
{
  myservo.write(throttleValue);
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  long duration = pulseIn(echoPin, HIGH);
  int distance = round(10.0 * duration * 0.034 / 2.0);
  return distance;
}

int height;
String reply;


void setup() {
  // Serial Communication
  Serial.begin(9600);

  // Setup the pin to command
  myservo.attach(pin);  // attaches the servo on pin 9 to the servo object

  // For the distance sensor.
  pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoPin, INPUT); // Sets the echoPin as an Input
}

void loop() {
  myservo.writeMicroseconds(1100);
  
  if (Serial.available() > 0)  {
    char c = Serial.read();  //gets one byte from serial buffer
    if(c == '[')
    {
      // Start of transmission!
      string = "[";
    }
    else if(c == ']')
    {
      string += "]";
      // End of transmission!
      //Serial.println(string);  // Echo back what we read (testing)
      
      // String string (command) = "[1270,1270,1272,1270,1268,1268,1272,1272,1269,1272]";
      // Parse
      // int[] myValues = new int[1270,1270,1272,1270,1268,1268,1272,1272,1269,1272];
      // Execute myvalues
      // Record Heights
      // int[] heights = [1, 2, 5, 10, 3, 6, 7, 3, 2];
      // Send back command+heights

      myservo.writeMicroseconds(1100);
      
      // Parse the string into an array of integers
      int* parsedArray = parseString(string);
      int arraySize = getNumElements(string);
      
      // And then, execute those values
      int* heights = new int[arraySize];
      for(int i = 0; i < arraySize; i++)
      {
        int throttleValue = parsedArray[i];
        int height = execute(throttleValue);
        heights[i] = height;
        delay(throttleDelayValue);
      }
      
      // Then send back the heights for each value executed.
      reply = string;
      reply += "{";
      // [1270, 1271]{1, 3}
      for(int i = 0; i < arraySize; i++)
      {
        height = heights[i];
        reply += String(height);
        if(i != arraySize-1) // if not the last, add a comma
        {
          reply += ",";
        }
      }

      // Free memory
      delete parsedArray;
      delete heights;
      
      reply += "}";
      myservo.writeMicroseconds(1100);
      delay(commandDelayValue);
      Serial.println(reply);
      //Serial.println(freeMemory());
      //Serial.println(sizeof(parsedArray) / sizeof(parsedArray[0]));
      //Serial.println(arraySize);
      //Serial.println(sizeof(reply));
      //Serial.println(sizeof(c));
      string="";
    }
    else
    {
      // Reading the incoming chromosome, 1 character (byte) at a time
      string += c;  
    }
  }
}
