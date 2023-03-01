/*


 * Written on July 26, 2020 by Ahmad Shamshiri in Ajax, Ontario, Canada
 * www. Robojax.com
  Robojax course on Udemy.com http://robojax.com/L/?id=62
  Robojax Patreon http://robojax.com/L/?id=63
  Robojax PayPal http://robojax.com/L/?id=64
  GNU General Public License <https://www.gnu.org/licenses/>.

*/
#include <Wire.h> 
#include <Robojax_WCS.h>
#define MODEL 12 //see list above
#define SENSOR_PIN A1 //pin for reading sensor
#define SENSOR_VCC_PIN 8 //pin for powring up the sensor
#define ZERO_CURRENT_LED_PIN 2 //zero current LED pin

#define ZERO_CURRENT_WAIT_TIME 5000 //wait for 5 seconds to allow zero current measurement
#define CORRECTION_VLALUE 164 //mA
#define MEASUREMENT_ITERATION 100
#define VOLTAGE_REFERENCE  5000.0 //5000mv is for 5V
#define BIT_RESOLUTION 10
#define DEBUT_ONCE true


Robojax_WCS sensor(
          MODEL, SENSOR_PIN, SENSOR_VCC_PIN, 
          ZERO_CURRENT_WAIT_TIME, ZERO_CURRENT_LED_PIN,
          CORRECTION_VLALUE, MEASUREMENT_ITERATION, VOLTAGE_REFERENCE,
          BIT_RESOLUTION, DEBUT_ONCE           
          );

void setup()
{

  sensor.start();
  Serial.begin(9600);
}

void loop()
{ 
  // sensor.readCurrent();//this must be inside loop
  // sensor.printCurrent();
  Serial.println(sensor.getCurrent());

  delay(1000);
	//sensor.printDebug();
}