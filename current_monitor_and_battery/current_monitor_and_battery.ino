 /*
  DC-Current-Voltage-Sensor-Module using INA219

  based on Adafruit Example and Amir Mohammad Shojaei  article:
  https://electropeak.com/learn/interfacing-ina219-current-sensor-module-with-arduino/

  Battery voltage level using Voltage Sensor
  https://how2electronics.com/interfacing-0-25v-dc-voltage-sensor-with-arduino/

  Code addapted by Alvaro-c: https://github.com/Alvaro-c
*/

// INA219 config
#include <Wire.h>
#include <Adafruit_INA219.h>
Adafruit_INA219 ina219;


// Voltage Sensor config
// Define analog input
#define ANALOG_IN_PIN A1
// Floats for ADC voltage & Input voltage
float adc_voltage = 0.0;
float in_voltage = 0.0;
// Floats for resistor values in divider (in ohms)
float R1 = 30000.0;
float R2 = 7500.0;
// Float for Reference Voltage
float ref_voltage = 5.0;
// Integer for ADC value
int adc_value = 0;

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
  // Amper and Voltage powe production
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

  // Voltage from battery
  // Read the Analog Input
   adc_value = analogRead(ANALOG_IN_PIN);
   // Determine voltage at ADC input
   adc_voltage  = (adc_value * ref_voltage) / 1024.0;
   // Calculate voltage at divider input
   in_voltage = adc_voltage / (R2/(R1+R2)) ;

  // Print results

  Serial.print(busvoltage);Serial.print(";");
  Serial.print(shuntvoltage);Serial.print(";");
  Serial.print(loadvoltage);Serial.print(";");
  Serial.print(current_mA);Serial.print(";");
  Serial.print(power_mW);Serial.print(";");
  Serial.print(in_voltage, 2);Serial.println(";"); // 2 decimal places

  delay(5000);
}
