#include <Arduino.h>
// #include "pin.h"
char myChar;
boolean isNew;

struct Pin {
    uint8_t pinNumber;
    bool pinValue = false;
};

// before you compile this make sure you set everything to the pin you want to send a value with;
// lets say you want pin 8 to send value 1 then you would set pin1 to 8; 
Pin pin1H;
Pin pin2H;
Pin pin4H;
Pin pin1M;
Pin pin2M;
Pin pin4M;
Pin pin8M;
Pin pin16M;
Pin pin32M;

// all of the pins for ease of access
Pin* pins[] = {
  &pin1H,
  &pin2H,
  &pin4H,
  &pin1M,
  &pin2M,
  &pin4M,
  &pin8M,
  &pin16M,
  &pin32M
};



// put function declarations here:
void enableCharacterLight(int character);

void pinSet(Pin& usrpin, uint8_t val) {
  Serial.print("setting value ");Serial.print(val);Serial.print(" from original value ");Serial.println( usrpin.pinNumber );
  usrpin.pinNumber = val;
}
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  int length = sizeof(pins) / sizeof(pins[0]);

  pin1H.pinNumber = 99;
  pinSet(pin1H,7);
  Serial.println(pin1H.pinNumber);
  pinSet(pin2H,8);
  Serial.println(pin2H.pinNumber);
  pinSet(pin4H,9);
  Serial.println(pin4H.pinNumber);
  pinSet(pin1M,2);
  Serial.println(pin1M.pinNumber);
  pinSet(pin2M,3);
  Serial.println(pin2M.pinNumber);
  pinSet(pin4M,4);
  Serial.println(pin4M.pinNumber);
  pinSet(pin8M,5);
  Serial.println(pin8M.pinNumber);
  pinSet(pin16M,6);
  Serial.println(pin16M.pinNumber);
  pinSet(pin32M,10);
  Serial.println(pin32M.pinNumber);

  Serial.println(length);
  for (uint8_t i = 0; length > i; i++) {
    // Serial.println("changing pin to output");
    Serial.println(i);
    Serial.println(pins[i]->pinNumber);
    pinMode(pins[i]->pinNumber,OUTPUT);
    digitalWrite(pins[i]->pinNumber,HIGH);
    delay(500);
    digitalWrite(pins[i]->pinNumber,LOW);
  }

  Serial.println("Ready");

}

void loop() {
  // put your main code here, to run repeatedly:
  // Serial.println(myChar);
  if (isNew) {
    //invalid conversion from char to char* this happens because its pointing to a LL and not a char
    int *character;
    *character = myChar;
    // Serial.println(*character); // Serial.println dereferenced character
    enableCharacterLight(*character);
    isNew = false;
  }

  if (Serial.available() > 0) {
    myChar = Serial.read();
    isNew = true;
  }
}

// put function definitions here:
void enableCharacterLight(int character) {
  // Serial.println(character == 97);
  static int ledsOn = 0; // says the amount of LEDS that are on. I am insulting your intelligence btw
  Serial.println(character);
  Serial.println(sizeof(pins)/sizeof(pins[0]));
  for (int i = 0; sizeof(pins)/sizeof(pins[0]) > i; i++) {
    // Serial.println(97+i);
     if ((97 + i) == character ) {
        
        if (!pins[i]->pinValue) {
            digitalWrite(pins[i]->pinNumber,HIGH);
            pins[i]->pinValue = true;
            ledsOn++;
        }
        else {
            digitalWrite(pins[i]->pinNumber,LOW);
            pins[i]->pinValue = false;
            ledsOn += -1;
        }

        
     }
  }
}
// 3/7/25 ts compiles thank the lord

//PID 2341