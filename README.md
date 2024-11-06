# OzSec: Kansas
This repo contains MicroPython code for the OzSec 2024: Adventure badge. This is a new codebase/firmware for our beloved Kansas shaped badge. 

Note that this readme is in dire need of fleshing out. 

## Setting up development environment

- Install Python 3.12+ for your system
- Install PIP
- Install VS Code
- `pip install esptool`
- Clone this repo (or download it) and open it in VS Code. It should suggest/recommend the VS Code Extensions Python and Pymakr, install those.

## Setting up a badge

You will need to flash your OzSec 2024: Adventure badge with the firmware located in the firmware folder. This is MicroPython built for the ESP32-S3-WROOM-1-N8R8.

First you will need to install `esptool.py` if you haven't already with `pip install esptool`. Of course, you will also need Python. 

Use the following command to flash this firmware. Note that it should auto-detect your esp32 device, but if it doesn't you will need to specify `--port <com port>`.
- First, wipe your badge:
`esptool.py erase_flash`
- Flash the firmware:
`esptool.py --chip esp32s3 write_flash -z 0x0 ESP32_GENERIC_S3-SPIRAM_OCT-20241025-v1.24.0.bin`