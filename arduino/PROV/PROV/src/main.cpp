#include <Arduino.h>
char myChar;
boolean isNew;


// before you compile this make sure you set everything to the pin you want to send a value with;
// lets say you want pin 8 to send value 1 then you would set pin1 to 8; 
uint8_t pin1 = 2;
uint8_t pin2;
uint8_t pin4;
uint8_t pin8;
uint8_t pin16;
uint8_t pin32;
uint8_t pin64;
uint8_t pin128;
uint8_t pin256;
bool pin1Value = false;
bool pin2Value = false;
bool pin4Value = false;
bool pin8Value = false;
bool pin16Value = false;
bool pin32Value = false;
bool pin64Value = false;
bool pin128Value = false;
bool pin256Value = false;

// all of the pins for ease of access
uint8_t pins[] = {
  pin1,
  pin2,
  pin4,
  pin8,
  pin16,
  pin32,
  pin64,
  pin128,
  pin256,
};


// put function declarations here:
void enableCharacterLight(int character);

void setup() {
  // put your setup code here, to run once:

  for (uint8_t i = 0; (sizeof(pins) / sizeof(pins[0])) > i; i++) {
    pinMode(pins[i],OUTPUT);
  }

  Serial.begin(9600);
  Serial.println("Ready");

}

void loop() {
  // put your main code here, to run repeatedly:

  if (isNew) {
    isNew = false;
  }



  if (Serial.available() > 0) {
      myChar = Serial.read();
      enableCharacterLight(myChar);
      Serial.println(myChar - 0);
      isNew = true;
  }
}

// put function definitions here:
void enableCharacterLight(int character) {
  Serial.println(character);
    if (character == 97) {
        if (pin1Value) {
          digitalWrite(pin1,HIGH);
        }
        else {
          digitalWrite(pin1,LOW);
        }
    }
    else if (character == 98) {
      if (pin2Value) {
        if (pin2Value) {
          digitalWrite(pin2,HIGH);
        }
        else {
          digitalWrite(pin2,LOW);
        }
      }
    }
}

// u2 M2 U2 M2 z u2 L2 R2' U2 L2 R2' L2 R2'