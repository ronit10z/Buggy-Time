//SoftwareSerial library used to communicate with the XBee:
#include <SoftwareSerial.h>

#define DEBUG true


/**********************************************************************
 *                CONSTANT/MACRO/GLOBAL DEFINITIONS
 **********************************************************************/

// Digital pin definition for pressure sensor (debug purposes only)
#define SENSOR_DIGITAL 8
// Analog pin definition for pressure sensor
#define SENSOR 0

// Wait for difference between baseline and actual pressure reading to be greater than threshold before transmitting
#define THRESHOLD 100
// Baseline voltage reading from pressure sensors on startup
int baseline;

// Char buffer for message to be transmitted
char buffer[11];

// Wait for ready message before reading pressure sensor values
const char ready_message = 'a';
// Message to be transmitted back to coordinator when pressure sensor is depressed
const char line_crossed_message = 'b';
const char ping_start_message = 'c';

const char finish_ready_message = 'd';
const char finish_line_crossed_message = 'e';
const char ping_finish_message = 'f';



// XBee's DOUT (TX) is connected to pin 2 (Arduino's Software RX)
// XBee's DIN (RX) is connected to pin 3 (Arduino's Software TX)
SoftwareSerial XBee(2, 3); // RX, TX

char inData[20]; // Allocate some space for the string
char inChar=-1; // Where to store the character read
byte index = 0; // Index into array; where to store the character
/**********************************************************************
 *                             SETUP
 **********************************************************************/

void setup()
{
  // Set up XBee to run at 9600 baud
  XBee.begin(9600);
  Serial.begin(9600);

  // Initialize pressure sensors
  pinMode(SENSOR_DIGITAL, INPUT);
  baseline = analogRead(SENSOR);
}


/**********************************************************************
 *                             MAIN LOOP
 **********************************************************************/

void loop()
{
  if(DEBUG){
//    // Print voltage to serial monitor
//    int voltage = analogRead(SENSOR);
//    Serial.println(voltage);
//
//    //Transmit voltage to coordinator
//    sprintf(buffer, "%d\n", voltage);
//    XBee.write(buffer);
//
//    if (Serial.available()){ // If data comes in from serial monitor, send it out to XBee
//      XBee.write(Serial.read());
//    }
//    if (XBee.available()){ // If data comes in from XBee, send it out to serial monitor
//      Serial.write(XBee.read());
//    }
//
//    delay(100);
    wait_for_data();
    delay(1000);
    transmit_line_crossed();

    // wait_for_finish_ready();
    delay(1000);
    transmit_finish_line_crossed();
  }

  else{
    wait_for_data();
    wait_for_press();
    transmit_line_crossed();
  }
}


/**********************************************************************
 *                           HELPER FUNCTIONS
 **********************************************************************/

// Hang until ready signal is received from coordinator
void wait_for_data()
{
  Serial.println("waiting for ready");
  while(true){
    while (XBee.available()){
        char message = XBee.read();
        Serial.print("Recieved: ");
        Serial.println(message);
        switch (message){
            case finish_ready_message:
                return;
            case ping_finish_message:
                XBee.write(message);
                Serial.print("Sending: ");
                Serial.println(message);
                break;
            case ready_message:
            case ping_start_message:
            default:
                continue;
        }
    }
  }
}

// Hang until pressure sensor is pressed
void wait_for_press()
{
  while(true){
    Serial.println("loop");
    int voltage = analogRead(SENSOR);
    int difference = baseline - voltage;
    if (difference >= THRESHOLD) break;
  }
}

// Transmit line crossed message back to coordinator
void transmit_line_crossed()
{
  Serial.println(line_crossed_message);
  XBee.write(line_crossed_message);
}


void transmit_finish_line_crossed()
{
  Serial.println(finish_line_crossed_message);
  XBee.write(finish_line_crossed_message);
}
