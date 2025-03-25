#include <Arduino.h>

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

void pinSet(Pin& usrpin, uint8_t val) {
  Serial.print("setting value ");Serial.print(val);Serial.print(" from original value ");Serial.println( usrpin.pinNumber );
  usrpin.pinNumber = val;
}

// the input pins dont take away current
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

  for (uint8_t i = 0; length > i; i++) {
    // Serial.println("changing pin to output");
    Serial.println(pins[i]->pinNumber);
    pinMode(pins[i]->pinNumber,INPUT);
  }

  Serial.println("Ready");
}

void loop() {
  // put your main code here, to run repeatedly:
  char charsToSend[9];
  for (int i = 0; (sizeof(pins) / sizeof(pins[0])) > i; i++) {
      if (digitalRead(pins[i]->pinNumber) == HIGH) {
        charsToSend[i] += (char)(97+i);
      }
  }
  Serial.println(charsToSend);
  Serial.write(charsToSend);
  delay(1000);
}

