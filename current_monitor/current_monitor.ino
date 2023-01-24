 /*
  DC-Current-Voltage-Sensor-Module using INA219
  
  based on Adafruit Example and Amir Mohammad Shojaei  article:
  https://electropeak.com/learn/interfacing-ina219-current-sensor-module-with-arduino/
*/

#include <Wire.h>
#include <Adafruit_INA219.h>

Adafruit_INA219 ina219;

void setup(void) 
{
  Serial.begin(9600);
  while (!Serial) {
      // will pause Zero, Leonardo, etc until serial console opens
      delay(1);
  }

  uint32_t currentFrequency;
    

  if (! ina219.begin()) {
    Serial.println("Failed to find INA219 chip");
    while (1) { delay(10); }
  }

}

void loop(void) 
{
  float shuntvoltage = 0;
  float busvoltage = 0;
  float current_mA = 0;
  float loadvoltage = 0;
  float power_mW = 0;

  shuntvoltage = ina219.getShuntVoltage_mV();
  busvoltage = ina219.getBusVoltage_V();
  current_mA = ina219.getCurrent_mA();
  power_mW = ina219.getPower_mW();
  loadvoltage = busvoltage + (shuntvoltage / 1000);

  Serial.print(busvoltage);Serial.print(";");
  Serial.print(shuntvoltage);Serial.print(";");
  Serial.print(loadvoltage);Serial.print(";");
  Serial.print(current_mA);Serial.print(";");
  Serial.print(power_mW);Serial.println(";");

  delay(5000);
}
