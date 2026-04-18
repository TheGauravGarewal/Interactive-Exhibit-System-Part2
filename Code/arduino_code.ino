#define IR1 2
#define IR2 3

void setup() {
  pinMode(IR1, INPUT);
  pinMode(IR2, INPUT);
  Serial.begin(9600);
}

void loop() {
  if (digitalRead(IR1) == LOW && digitalRead(IR2) == LOW) {
    Serial.println("BOTH");
  } else {
    Serial.println("");
  }
  delay(200);
}
