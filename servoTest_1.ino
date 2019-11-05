#include <Servo.h> 

Servo leftServo;
Servo rightServo;

void setup() 
{ 
  Serial.begin(9600);
    while (! Serial);
    Serial.println("Speed 0 to 180");
  leftServo.attach(5);
  rightServo.attach(6);
  leftServo.write(90);  // set servo to mid-point
  rightServo.write(90);  // set servo to mid-point
}

void loop() {
    if (Serial.available()) {
    int speed = Serial.parseInt();
      if (speed >= 1 && speed <= 180){
        Serial.println(speed);
        rightServo.write(speed); //sets speed of the right servo to the entered speed
      }
      if (speed <= -1 && speed >= -180){
        Serial.println(speed);
        leftServo.write(-1*speed);  //sets speed of the left servo to the entered speed
      }
   }
} 
