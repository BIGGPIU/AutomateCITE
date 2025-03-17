#include <Arduino.h>

int valToSend;
int valToMultiply;

uint8_t pin1;
uint8_t pin2;
uint8_t pin4;
uint8_t pin8;
uint8_t pin16;
uint8_t pin32;
uint8_t pin64;
uint8_t pin128;
uint8_t pin256;

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



void setup() {
  // put your setup code here, to run once:
  for (int i = 0; (sizeof(pins) / sizeof(pins[0])) > i; i++) {
    pinMode(pins[i],OUTPUT);
  }

  Serial.begin(9600);
  Serial.println("Ready");
}

void loop() {
  // put your main code here, to run repeatedly:
  valToSend = 0;
  for (int i = 0; (sizeof(pins) / sizeof(pins[0])) > i; i++) {
    valToMultiply = i*2;
      if (digitalRead(pins[i]) == HIGH) {
          if ( i == 0) {
            valToSend++;
          }
          else {
            valToSend += valToMultiply;
          }
      }
      else {
          // do absolutely nothing
      }
  }


  Serial.println(valToSend);
  delay(1000);
}

