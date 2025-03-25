// #include <Arduino.h>
// char myChar;
// boolean isNew;


// // before you compile this make sure you set everything to the pin you want to send a value with;
// // lets say you want pin 8 to send value 1 then you would set pin1 to 8; 
// uint8_t pin1 = 2;
// uint8_t pin2 = 3;
// uint8_t pin4 = 4;
// uint8_t pin8 = 5;
// uint8_t pin16 = 6;
// uint8_t pin32 = 7;
// uint8_t pin64 = 8;
// uint8_t pin128 = 9;
// uint8_t pin256 = 10;
// bool pin1Value = false;
// bool pin2Value = false;
// bool pin4Value = false;
// bool pin8Value = false;
// bool pin16Value = false;
// bool pin32Value = false;
// bool pin64Value = false;
// bool pin128Value = false;
// bool pin256Value = false;

// // all of the pins for ease of access
// uint8_t pins[] = {
//   pin1,
//   pin2,
//   pin4,
//   pin8,
//   pin16,
//   pin32,
//   pin64,
//   pin128,
//   pin256,
// };



// // put function declarations here:
// void enableCharacterLight(int character);

// void setup() {
//   // put your setup code here, to run once:
//   Serial.begin(9600);

//   int length = sizeof(pins) / sizeof(pins[0]);
//   Serial.println(length);
//   for (uint8_t i = 0; length > i; i++) {
//     // Serial.println("changing pin to output");
//     Serial.println(i);
//     pinMode(pins[i],OUTPUT);
//     digitalWrite(pins[i],HIGH);
//     delay(500);
//     digitalWrite(pins[i],LOW);
//   }

//   Serial.println("Ready");

// }

// void loop() {
//   // put your main code here, to run repeatedly:
//   // Serial.println(myChar);
//   if (isNew) {
//     //invalid conversion from char to char* this happens because its pointing to a LL and not a char
//     int *character;
//     *character = myChar;
//     // Serial.println(*character); // Serial.println dereferenced character
//     enableCharacterLight(*character);
//     isNew = false;
//   }

//   if (Serial.available() > 0) {
//     myChar = Serial.read();
//     isNew = true;
//   }
// }

// // put function definitions here:
// void enableCharacterLight(int character) {
//   // Serial.println(character == 97);
//   Serial.println(character);
//   if (character == 97) {
    
//     // Serial.println(pin1Value);
//       if (!pin1Value) {
//         digitalWrite(pin1,HIGH);
//         pin1Value = true;
//       }
//       else {
//         digitalWrite(pin1,LOW);
//         pin1Value = false;
//       }
//   }
//   else if (character == 98) {
//     if (!pin2Value) {
//         digitalWrite(pin2,HIGH);
//         pin2Value = true;
//       }
//       else {
//         digitalWrite(pin2,LOW);
//         pin2Value = false;
//       }
//   }
//   else if (character == 99) {
//     if (!pin4Value) {
//         digitalWrite(pin4,HIGH);
//         pin4Value = true;
//       }
//       else {
//         digitalWrite(pin4,LOW);
//         pin4Value = false;
//       }
//   }
//   else if (character == 100) {
//     if (!pin8Value) {
//         digitalWrite(pin8,HIGH);
//         pin8Value = true;
//       }
//       else {
//         digitalWrite(pin8,LOW);
//         pin8Value = false;
//       }
//   }
//   else if (character == 101) {
//     if (!pin16Value) {
//         digitalWrite(pin16,HIGH);
//         pin16Value = true;
//       }
//       else {
//         digitalWrite(pin16,LOW);
//         pin16Value = false;
//       }
//   }
//   else if (character == 102) {
//     if (!pin32Value) {
//         digitalWrite(pin32,HIGH);
//         pin32Value = true;
//       }
//       else {
//         digitalWrite(pin32,LOW);
//         pin32Value = false;
//       }
//   }
//   else if (character == 103) {
//     if (!pin64Value) {
//         digitalWrite(pin64,HIGH);
//         pin64Value = true;
//       }
//       else {
//         digitalWrite(pin64,LOW);
//         pin64Value = false;
//       }
//   }
//   else if (character == 104) {
//     if (!pin128Value) {
//         digitalWrite(pin128,HIGH);
//         pin128Value = true;
//       }
//       else {
//         digitalWrite(pin128,LOW);
//         pin128Value = false;
//       }
//   }
//   else if (character == 105) {
//     if (!pin256Value) {
//         digitalWrite(pin256,HIGH);
//         pin256Value = true;
//       }
//       else {
//         digitalWrite(pin256,LOW);
//         pin256Value = false;
//       }
//   }
// }
// // 3/7/25 ts compiles thank the lord

// //PID 2341