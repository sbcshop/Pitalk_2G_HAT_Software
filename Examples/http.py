'''
#------------------------------------------------------------------------
#
# This is a python Example code for PiTalk-2G HAT of TCP 
# Written by SB Components Ltd 
#
#==================================================================================
# Copyright (c) SB Components Ltd
#
# Permission is hereby granted, free of charge, to any person obtaining a copy 
# of this software and associated documentation files (the "Software"), to deal 
# in the Software without restriction, including without limitation the rights 
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
# copies of the Software, and to permit persons to whom the Software is 
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all 
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
# SOFTWARE.
#==================================================================================
'''

import RPi.GPIO as GPIO
import serial
import time
import sys
sys.path.insert(0,'/home/pi/Desktop/Pitalk_2G_HAT_Software-main/Library')
import PiTalk_2G

# HTTP Perameters
get_server = ["https://api.thingspeak.com/channels/1717340/status.json?api_key=HZEBV0TXO4Z8VEL9"]
post_server = "http://api.thingspeak.com/update"
post_data = 'api_key=2KWL4NUT0MEA8I97&field1=26.44&field2=57.16'
content_type = 'application/x-www-form-urlencoded'


                
HTTP  = PiTalk_2G.SIM868()
#HTTP.http_get(get_server) #Uncomment this code line to use funtionality of HTTP GET
HTTP.http_post(post_server,post_data,content_type) #Uncomment this code line to use funtionality of HTTP POST


