import RPi.GPIO as GPIO
import serial
import time


ser = serial.Serial('/dev/ttyS0',115200)
ser.flushInput()
power_key = 23
rec_buff = ''

class eg25(object):
    def __init__(self,power_key):
        self.power_key = power_key
        self.ser = serial.Serial('/dev/ttyS0',115200)
        self.ser.flushInput()
        
    def power_on(self,power_key):
        print('SIM7600X is starting:')
        self.GPIO.setmode(GPIO.BCM)
        self.GPIO.setwarnings(False)
        self.GPIO.setup(power_key,self.GPIO.OUT)
        time.sleep(0.1)
        self.GPIO.output(power_key,self.GPIO.HIGH)
        time.sleep(2)
        self.GPIO.output(power_key,self.GPIO.LOW)
        time.sleep(20)
        self.ser.flushInput()
        print('SIM7600X is ready')

    def power_down(self,power_key):
        print('SIM7600X is loging off:')
        GPIO.output(power_key,GPIO.HIGH)
        time.sleep(3)
        GPIO.output(power_key,GPIO.LOW)
        time.sleep(18)
        print('Good bye')
'''
    try:
        power_on(power_key)
        print('Sending Short Message Test:')
        SendMessage(phone_number,text_message)
        print('Receive Short Message Test:\n')
        print('Please send message to phone ' + phone_number)
        #ReceiveMessage()
        #power_down(power_key)
    except :
        if ser != None:
            ser.close()
        GPIO.cleanup()   
'''

    def send_at(self,command,back,timeout):
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
        if 1 == answer:
            self.ser.write(text_message.encode())
            self.ser.write(b'\x1A')
            self.answer = self.send_at('','OK',20)
        if 1 == answer:
            print('send successfully')
        else:
            print('error')
        else:
            print('error%d'%answer)

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


    def Call(self, phone_number,time):
        self.power_on(power_key)
        self.send_at('ATD'+phone_number+';','OK',1)
        time.sleep(time)
        self.ser.write('AT+CHUP\r\n'.encode())
        print('Call disconnected')
        
    def TCP(self):
        self.power_on(power_key)
        self.send_at('AT+CSQ','OK',1)
        self.send_at('AT+CREG?','+CREG: 0,1',1)
        self.send_at('AT+CPSI?','OK',1)
        self.send_at('AT+CGREG?','+CGREG: 0,1',0.5)
        self.send_at('AT+CGSOCKCONT=1,\"IP\",\"'+APN+'\"','OK',1)
        self.send_at('AT+CSOCKSETPN=1', 'OK', 1)
        self.send_at('AT+CIPMODE=0', 'OK', 1)
        self.send_at('AT+NETOPEN', '+NETOPEN: 0',5)
        self.send_at('AT+IPADDR', '+IPADDR:', 1)
        self.send_at('AT+CIPOPEN=0,\"TCP\",\"'+ServerIP+'\",'+Port,'+CIPOPEN: 0,0', 5)
        self.send_at('AT+CIPSEND=0,', '>', 2)#If not sure the message number,write the command like this: AT+CIPSEND=0, (end with 1A(hex))
        self.ser.write(Message.encode())
        if 1 == send_at(b'\x1a'.decode(),'OK',5):
            print('send message successfully!')
            self.send_at('AT+CIPCLOSE=0','+CIPCLOSE: 0,0',15)
            self.send_at('AT+NETCLOSE', '+NETCLOSE: 0', 1)

 
    def gps_positioning(self):
        self.power_on(power_key)
        rec_null = True
        self.answer = 0
        print('Start GPS session...')
        rec_buff = ''
        self.send_at('AT+CGPS=1,1','OK',1)
        time.sleep(2)
        while rec_null:
            
            answer = self.send_at('AT+CGPSINFO','+CGPSINFO: ',1)
            if 1 == self.answer:
                self.answer = 0
                if ',,,,,,' in rec_buff:
                    print('GPS is not ready')
                    rec_null = False
                    time.sleep(1)
            else:
                print('error %d'%self.answer)
                rec_buff = ''
                self.send_at('AT+CGPS=0','OK',1)
                return False
                time.sleep(1.5)

        
   
