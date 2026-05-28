#include <Wire.h>

void setup() {

    // Start serial communication
    Serial.begin(115200);

    // Initialize I2C communication
    Wire.begin();
}

void loop() {

    // Simulated distance value
    int distance = random(20, 200);

    // Print sensor reading
    Serial.println(distance);

    delay(500);
}
