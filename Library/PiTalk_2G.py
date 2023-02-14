'''
#------------------------------------------------------------------------
#
# This is a python Library code for PiTalk-2G HAT 
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

ser = serial.Serial('/dev/ttyS0',115200)
ser.flushInput()
power_key = 4
rec_buff = ''

class SIM868(object):
    def __init__(self):
        self.power_key = power_key
        self.ser = serial.Serial('/dev/ttyS0',115200)
        self.ser.flushInput()
        
    def power_on(self,power_key):
        print('SIM868 is starting:')
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(power_key,GPIO.OUT)
        time.sleep(0.1)
        GPIO.output(power_key,GPIO.HIGH)
        time.sleep(2)
        GPIO.output(power_key,GPIO.LOW)
        time.sleep(5)
        self.ser.flushInput()
        print('SIM868 is ready')

    def power_down(self,power_key):
        print('SIM868 is loging off:')
        GPIO.output(power_key,GPIO.HIGH)
        time.sleep(3)
        GPIO.output(power_key,GPIO.LOW)
        time.sleep(5)
        print('Good bye')

    def wait_resp_info(self,timeout=3000):
            self.prvmills = time.monotonic()
            info = b""
            while (time.monotonic()-self.prvmills) < (timeout/1000):
                if self.ser.in_waiting:
                    info = b"".join([info, self.ser.read(1)])
            print(info.decode())
            return info


    def send_at(self,command,back,timeout=1):
        rec_buff = ''
        self.ser.write((command+'\r\n').encode())
        time.sleep(timeout)
        if self.ser.inWaiting():
            time.sleep(0.01 )
            rec_buff = self.ser.read(self.ser.inWaiting())
        if back not in rec_buff.decode():
            print(command + ' ERROR')
            print(command + ' back:\t' + rec_buff.decode())
            return 0
        else:
            print(rec_buff.decode())
            return 1
    
    
    def SendSMessage(self,phone_number,text_message):
        self.power_on(power_key)
        print("Setting SMS mode...")
        self.send_at("AT+CMGF=1","OK",1)
        print("Sending Short Message")
        self.answer = self.send_at("AT+CMGS=\""+phone_number+"\"",">",2)
        if 1 == self.answer:
            self.ser.write(text_message.encode())
            self.ser.write(b'\x1A')
            self.answer = self.send_at('','OK',20)
            if 1 == self.answer:
                print('send successfully')
            else:
                print('error')
        else:
            print('error%d'%self.answer)

    def ReceiveMessage(self):
        self.power_on(power_key)
        rec_buff = ''
        print('Setting SMS mode...')
        self.send_at('AT+CMGF=1','OK',1)
        self.send_at('AT+CPMS=\"SM\",\"SM\",\"SM\"', 'OK', 1)
        self.answer = send_at('AT+CMGR=1','+CMGR:',2)
        if 1 == self.answer:
            self.answer = 0
        if 'OK' in rec_buff:
            self.answer = 1
            print(rec_buff)
        else:
            print('error%d'%self.answer)
            return False
        return True


    def Call(self, phone_number,time_1):
        self.power_on(power_key)
        self.send_at('ATD'+phone_number+';','OK',1)
        time.sleep(time_1)
        self.ser.write('AT+CHUP\r\n'.encode())
        print('Call disconnected')

  
    # TCP
    def tcp(self,info,ServerIP, Port, APN):
            self.power_on(power_key)
            self.send_at('AT+CIPSHUT', 'OK')
            self.send_at("AT+CSQ", "OK")
            self.send_at("AT+CREG?", "OK")
            self.send_at('AT+CGATT?', 'OK')
            self.send_at("AT+CSTT=\""+APN+"\"",'OK',5)
            self.send_at('AT+CIICR', 'OK')
            self.send_at('AT+CIFSR', 'OK')
            self.send_at('AT+CIPSTART=\"TCP\",\"'+ServerIP+'\",'+Port,'\"', 'OK')
            self.send_at('AT+CIPSEND', ">",5)
            self.self.ser.write(info.encode())
            self.ser.write(hexstr_to_str("1A").encode())

                     
    # HTTP GPS
    def gps(self):
        self.power_on(power_key)
        rec_null = True
        self.answer = 0
        print('Start GPS session...')
        rec_buff = ''
        self.send_at('AT+CGNSPWR=1,1','OK',1)
        time.sleep(2)
        for i in range(1, 10):
            self.ser.write(bytearray(b'AT+CGNSINF\r\n'))
            rec_buff = self.wait_resp_info()
            if ',,,,' in rec_buff.decode():
                print('GPS is not ready')
                #print(rec_buff.decode())
                if i >= 9:
                    print('GPS positioning failed, please check the GPS antenna!\r\n')
                    self.send_at('AT+CGNSPWR=0', 'OK')
                else:
                    time.sleep(2)
                    continue
            else:
                if count <= 3:
                    count += 1
                    print('GPS info:')
                    print(rec_buff.decode())
                else:
                    self.send_at('AT+CGNSPWR=0', 'OK')
                    break


    # HTTP GET 
    def http_get(self,get_server):
        self.power_on(power_key)
        self.send_at('AT+HTTPINIT', 'OK')
        self.send_at('AT+HTTPPARA=\"CID\",1', 'OK')
        self.send_at('AT+HTTPPARA=\"URL\",\"'+get_server[0]+get_server[1]+'\"', 'OK')
        if self.send_at('AT+HTTPACTION=0', '200', 5000):
            self.ser.write(bytearray(b'AT+HTTPREAD\r\n'))
            rec_buff = wait_resp_info(8000)
            print("resp is :", rec_buff.decode())
        else:
            print("Get HTTP failed, please check and try again\n")
        send_at('AT+HTTPTERM', 'OK')


    # HTTP POST 
    def http_post(self,post_server,post_data,content_type):
        self.power_on(power_key)
        self.send_at('AT+HTTPINIT', 'OK')
        self.send_at('AT+HTTPPARA=\"CID\",1', 'OK')
        self.send_at('AT+HTTPPARA=\"URL\",\"'+post_server[0]+post_server[1]+'\"', 'OK')
        self.send_at('AT+HTTPPARA=\"CONTENT\",\"' + content_type + '\"', 'OK')
        if self.send_at('AT+HTTPDATA=62,8000', 'DOWNLOAD', 3):
            self.ser.write(post_data.encode())
            time.sleep(10)
            rec_buff = self.wait_resp_info()
            if 'OK' in rec_buff.decode():
                print("UART data is read!\n")
            if self.send_at('AT+HTTPACTION=1', '200', 8):
                print("POST successfully!\n")
            else:
                print("POST failed\n")
            self.send_at('AT+HTTPTERM', 'OK')
        else:
            print("HTTP Post failed，please try again!\n")
        
   
