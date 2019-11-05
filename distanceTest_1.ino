//First Ultrasonic sensor
const int pingPin = 7; // Trigger Pin of Ultrasonic Sensor
const int echoPin = 10; // Echo Pin of Ultrasonic Sensor

//Second Ultrasonic sensor
const int pingPin2 = 12; // Trigger Pin of Ultrasonic Sensor
const int echoPin2 = 11; // Echo Pin of Ultrasonic Sensor

void setup() {
   Serial.begin(9600); // Starting Serial Terminal
}

void loop() {
  //////////////////////////////////////////////   
   //Code for first ultrasonic sensor
   double duration, inches, cm;
   pinMode(pingPin, OUTPUT);
   digitalWrite(pingPin, LOW);
   delayMicroseconds(2);
   digitalWrite(pingPin, HIGH);
   delayMicroseconds(10);
   digitalWrite(pingPin, LOW);
   pinMode(echoPin, INPUT);
   duration = pulseIn(echoPin, HIGH);
   inches = microsecondsToInches(duration);   //Distance in inches for first sensor
   cm = microsecondsToCentimeters(duration);  //Distance in cm for first sensor

  //////////////////////////////////////////////
   //Code for second ultrasonic sensor
   double duration2, inches2, cm2;
   pinMode(pingPin2, OUTPUT);
   digitalWrite(pingPin2, LOW);
   delayMicroseconds(2);
   digitalWrite(pingPin2, HIGH);
   delayMicroseconds(10);
   digitalWrite(pingPin2, LOW);
   pinMode(echoPin2, INPUT);
   duration2 = pulseIn(echoPin2, HIGH);
   inches2 = microsecondsToInches(duration2); //Distance in inches for first sensor
   cm2 = microsecondsToCentimeters(duration2); //Distance in centimeters for first sensor

   
   Serial.print(inches);
   Serial.print("in, ");
   Serial.print(inches2);
   Serial.print("in, ");
   //Serial.print(cm2);
   //Serial.print("cm");
   Serial.println();
   delay(100);
   if(inches == inches2){
      Serial.print("EQUAL");
      Serial.println();
   }
}

double microsecondsToInches(double microseconds) {
   return microseconds / 74 / 2;
}

double microsecondsToCentimeters(double microseconds) {
   return microseconds / 29 / 2;
}
