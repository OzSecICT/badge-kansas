import time
import random
import neopixel
from machine import Pin, PWM

def rgb_on(r = 255, g = 0, b = 0, brightness = 0.1):
    brightness = max(0.0, min(1.0, brightness))
    r = int(r * brightness)
    g = int(g * brightness)
    b = int(b * brightness)
    rgb_pixel[0] = (r, g, b)
    rgb_pixel.write()

def rgb_off():
    rgb_pixel[0] = (0, 0, 0)
    rgb_pixel.write()

def fade_on(pwm_obj):
    pwm = pwm_obj['pwm']
    pwm_obj['state'] = 1
    for i in range(0, max_brightness):
        pwm.duty(i)
        time.sleep(fade_delay)

def fade_off(pwm_obj):
    pwm = pwm_obj['pwm']
    pwm_obj['state'] = 0
    for i in range(max_brightness, -1, -1):
        pwm.duty(i)
        time.sleep(fade_delay)

def toggle_led(pwm_obj):
    if pwm_obj['state'] == 0:
        fade_on(pwm_obj)
    else:
        fade_off(pwm_obj)

max_brightness = 10  # Maximum brightness level
fade_delay = 0.1  # Delay between brightness steps

# LED GPIO pins
led_pins = [3, 46, 18, 8, 13, 12, 9, 11]

# RGB
rgb_pin = 10
num_pixels = 1

# Initialize NeoPixel strip
rgb_pixel = neopixel.NeoPixel(Pin(rgb_pin), num_pixels)

# Initialize PWM for each LED pin
pwm_leds = []
for pin in led_pins:
    while True:
        try:
            pwm = PWM(Pin(pin))
            pwm.duty(0)  # Start with LEDs off
            pwm.freq(1000)  # Set the PWM frequency to 1kHz
            pwm_leds.append({'pwm': pwm, 'state': 0})
            time.sleep(3)  # Wait for 3 seconds
            break
        except ValueError as e:
            print(f"Error initializing PWM on pin {pin}, retrying: {e}")
            time.sleep(5)


if __name__ == '__main__':
    # Turn on the RGB LED
    rgb_on()
    while True:
        pwm = random.choice(pwm_leds)  # Randomly select an LED
        toggle_led(pwm)  # Flash the selected LED
        time.sleep(random.uniform(0.1, 0.5))  # Random delay between flashes