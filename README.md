# Pitalk 2G HAT 

<img src ="https://github.com/sbcshop/Pitalk_2G_HAT_Software/blob/main/images/Pitalk%202G%20front%20and%20back.png" />

The PiTalk 2G HAT is a handy, low-power Raspberry Pi HAT that features multi-communication functionalities such as GSM, GPRS, TCP, etc. It allows your Pi to easily make phone calls, send messages, connect to wireless networks, and so on. It is the most convenient IoT HAT that works with all variants of Raspberry Pi (model A, B and Zero). The users can also connect PiTalk with other iOS and Android devices as well. It is primarily designed to offer connection to your IoT projects and applications without requiring a Wi-Fi network or ethernet connections.

## Key Features Of SIM868:

* General
  * Quad-band 850/900/1800/1900MHz
  * GPRS multi-slot class 12/10
  * GPRS mobile station class B
  * Compliant to GSM phase 2/2+
  * Class 4 (2 W @ 850/900MHz)
  * Class 1 (1 W @ 1800/1900MHz)
  * Dimensions: 17.6*15.7*2.3mm
  * Weight: 1.5g
  * Control via AT commands (3GPP TS 27.007, 27.005 and SIMCom enhanced AT Commands)
  * Supply voltage range 5~18Vdc
  * Low power consumption
  * Operation temperature:-40℃ ~85℃

* SMS
  * Point to point MO and MT
  * SMS cell broadcast
  *Text and PDU mode
  
  
* GPRS
  *  GPRS data downlink transfer: max. 85.6 kbps
  * GPRS data uplink transfer: max. 85.6 kbps
  * Coding scheme: CS-1, CS-2, CS-3 and CS-4
  * PAP protocols for PPP connect
  * Integrate the TCP/IP protocol
  * Support Packet Broadcast Control Channel (PBCCH) 
  


<img src ="https://github.com/sbcshop/Pitalk_2G_HAT_Software/blob/main/images/PiTalk.png" /> 

## Setup PiTalk 2G HAT with RPi 

To Start working with our PiTalk 2G HAT, set-up your Raspberry Pi or RockPi by flashing their os file and boot it, for this [click here](https://rockpi.eu/Rockpi4/downloads).

* After setup your Pi board, attach the PiTalk 4G HAT on it and boot by providing compatible power supply.
* Now, open the command prompt and type the following command to clone the current repository in your Pi-board.
```
git clone .git https://github.com/sbcshop/Pitalk_2G_HAT_Software
```

* After, downloading this repository you will see two directory in it. One is of ***Example code*** and 2nd one is of ***Library*** file.
* Now, open the both Example and Library directory. To open these files make sure you have python installed in your Pi board.
* In examples Directory there are some example codes to use the different functionality of PiTalk HAT you have ***move out the example file*** which you want to run from the ***Examples directory*** and after that run the code by make some editing if require.


## Setup PiTalk 2G  Via USB


* You can command SIM868 also by providing the ***AT commands***  via USB com port. For this you have to connect PiTalk 2G HAT to your computer system by using micro usb cable as shon in below image:

<img src ="https://github.com/sbcshop/Pitalk_2G_HAT_Software/blob/main/images/PITALK%202G%20USB.jpg" />

* For using our PiTalk 2G HAT directly with the computer system, insert the sim card, attach the 2G antenna and connect it to your system. After that you will get a com port as shom as shon below:

<img src ="https://github.com/sbcshop/Pitalk_2G_HAT_Software/blob/main/images/Scr.png" />

* After getting ***COM port*** you can communicate our PiTalk 2G HAT by using any ***serial communication softwatre such as XCTU*** for sending ***AT Commands*** to operate it.




## Documentation

* [PiTalk-2G HAT Hardware](https://github.com/sbcshop/Pitalk_2G_HAT_Hardware)
* [SIM800 Series bluetooth](https://github.com/sbcshop/Pitalk_2G_HAT_Hardware/blob/main/Documents/SIM800_Series_Bluetooth.pdf)
* [SIM800 Series GSM](https://github.com/sbcshop/Pitalk_2G_HAT_Hardware/blob/main/Documents/SIM800_Series_GSM_Location.pdf)
* [SIM800 Series IP](https://github.com/sbcshop/Pitalk_2G_HAT_Hardware/blob/main/Documents/SIM800_Series_IP.pdf)
* [SIM800 Series MMS](https://github.com/sbcshop/Pitalk_2G_HAT_Hardware/blob/main/Documents/SIM800_Series_MMS.pdf)
* [SIM800 Series MQTT](https://github.com/sbcshop/Pitalk_2G_HAT_Hardware/blob/main/Documents/SIM800_Series_MQTT.pdf)
* [SIM800 Series NTP](https://github.com/sbcshop/Pitalk_2G_HAT_Hardware/blob/main/Documents/SIM800_Series_NTP.pdf)
* [SIM800 Series PCM](https://github.com/sbcshop/Pitalk_2G_HAT_Hardware/blob/main/Documents/SIM800_Series_PCM.pdf)
* [SIM800 Series SSL](https://github.com/sbcshop/Pitalk_2G_HAT_Hardware/blob/main/Documents/SIM800_Series_SSL.pdf)
* [SIM800 Series TCP IP](https://github.com/sbcshop/Pitalk_2G_HAT_Hardware/blob/main/Documents/SIM800_Series_TCPIP.pdf)
* [SIM800 Series GNSS](https://github.com/sbcshop/Pitalk_2G_HAT_Hardware/blob/main/Documents/SIM868_Series_GNSS.pdf)
* [Getting Started with Raspberry Pi](https://www.raspberrypi.com/documentation/computers/getting-started.html)
* [Raspberry Pi Pico Official website](https://www.raspberrypi.com/documentation/microcontrollers/)
* [Raspberry Pi Datasheet](https://www.raspberrypi.com/documentation/computers/compute-module.html)
* [Raspberry Hardware Design](https://www.raspberrypi.com/documentation/computers/compute-module.html)
* [Raspberry Pi](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html)

## Related Products

* [PiTalk](https://shop.sb-components.co.uk/products/pitalk-modular-smartphone-for-raspberry-pi?variant=12516562436179)

 ![PiTalk](https://cdn.shopify.com/s/files/1/1217/2104/products/PiTalk_-_Modular_SmartPhone_for_Raspberry_Pi_5.png?v=1528805795&width=400)
 
 *[USB Dongle 4G]()

 ![USB Dongle 4G]()
 
  *[PiTalk 4G]()

 ![PiTalk 4G]()
 

## Product License

This is ***open source*** product. Kindly check LICENSE.md file for more information.

Please contact support@sb-components.co.uk for technical support.
<p align="center">
  <img width="360" height="100" src="https://cdn.shopify.com/s/files/1/1217/2104/files/Logo_sb_component_3.png?v=1666086771&width=350">
</p>


