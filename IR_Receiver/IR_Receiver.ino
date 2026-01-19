#include <IRremote.h>

#define IR_IN_PIN 11
#define DEBOUNCE_TIME 100

unsigned long debounceTime;
String lastValue;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  debounceTime = millis();
  IrReceiver.begin(IR_IN_PIN, ENABLE_LED_FEEDBACK);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (IrReceiver.decode()) {
    String decodeValue = decodeKeyValue(IrReceiver.decodedIRData.command);
    if (decodeValue != "ERR" && ((millis() - debounceTime > DEBOUNCE_TIME) || (decodeValue != lastValue))) {
      debounceTime = millis();
      lastValue = decodeValue;
      Serial.println(decodeValue);
      
    }
    IrReceiver.resume();
  }
}
