/*Desktop/RTL/loadtest.py*/

import RPi.GPIO as GPIO
import serial
import time
import json
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu
import BlynkLib
rel_pri=23
rel_sec=24
direction=16
step=20
enable=21
led=12
reset_sw=7
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(rel_pri,GPIO.OUT)
GPIO.setup(rel_sec,GPIO.OUT)
GPIO.setup(enable,GPIO.OUT)
GPIO.setup(reset_sw,GPIO.OUT)
GPIO.setup(led,GPIO.OUT)

GPIO.setup(step,GPIO.OUT)
GPIO.setup(direction,GPIO.OUT)
blynk_auth="4jXZwRH1qbIF0coYQpmR5gAQ5jRhKhEp"
blynk=BlynkLib.Blynk(blynk_auth)
ohm=[109,83,55,31.5,14]
slider_pos=[0,3.3,6.6,9.9,12]
i1=[12,16.22,22.25,25.32,32.10]
current_pos=0
status=0
l_status=0

@blynk.on("connected")
def connected():
    print("connected")

@blynk.on("disconnected")
def disconnected():
    blynk.connect()

def init():

    @blynk.on("V9")
    def supply_write_handler(value):
        global status
        status=int(float(value[0]))
        if( status==1):
            GPIO.output(rel_pri,GPIO.LOW)
            GPIO.output(led,GPIO.HIGH)
       
            print("primary relay on")
           
            nl_vol=secondary()
            print(nl_vol)
       
           
            blynk.virtual_write(8,nl_vol)
            blynk.virtual_write(4,1.7)
        else:
            GPIO.output(rel_pri,GPIO.HIGH)
            GPIO.output(rel_sec,GPIO.HIGH)
            GPIO.output(led,GPIO.LOW)
            recal()
            blynk.virtual_write(6,slider_pos[0])
            blynk.virtual_write(13,0)
           
            print("recal done")
       
           
@blynk.on("V13")
def load_write_handler(value):
       
    global status
    global l_status
    l_status=int(float(value[0]))
   

    if(status and  l_status == 1):
        GPIO.output(rel_sec,GPIO.LOW)
        print("secondray relay on")
   


def slider(value):
    global current_pos
    global new_pos
    global move
    global status
    global l_status
    GPIO.output(enable,GPIO.LOW)
    new_pos=slider_pos[value]
    move=new_pos-current_pos
    current_pos = new_pos

    if(status and l_status == 1):

        if( move<0.0):

            GPIO.output(direction,GPIO.HIGH)
        else:

            GPIO.output(direction,GPIO.LOW)
        move=int(move*1000)
        for i in range(0,abs(move)):

            GPIO.output(step,GPIO.HIGH)
            time.sleep(0.0001)
            GPIO.output(step,GPIO.LOW)
            time.sleep(0.0001)
        GPIO.output(enable,GPIO.HIGH)


def recal():
    global current_pos

    GPIO.output(enable,GPIO.LOW)
    GPIO.output(direction,GPIO.HIGH)
    current_pos=0
    print("recal loop")
    while(GPIO.input(reset_sw)==0):
        print("00")
        GPIO.output(step,GPIO.HIGH)
        time.sleep(0.0001)
        GPIO.output(step,GPIO.LOW)
        time.sleep(0.0001)
    for i in range(0,9):
        blynk.virtual_write(i,0)
    GPIO.output(enable,GPIO.HIGH)

@blynk.on("V6")
def s1_write_handler(value):
    i=int(float(value[0]))
    slider(i)
    blynk.virtual_write(7,ohm[i])
    blynk.virtual_write(1,i1[i])

def primary():

    primary=serial.Serial(
            port="/dev/ttyUSB0",
            baudrate=9600,
            bytesize=8,
            parity="N",
            stopbits=1,
            xonxoff=0)
    master=modbus_rtu.RtuMaster(primary)
    master.set_timeout(2.0)
    master.set_verbose(True)
    sensor_val=dict()

    data=master.execute(1,cst.READ_INPUT_REGISTERS,0,10)

    sensor_val["voltage"]=data[0]/10.0
    sensor_val["current"]=(data[1]+(data[2]<<16))/1000.0
    sensor_val["power"]=(data[3]+(data[4]<<16))/10.0
    sensor_val["powerfactor"]=data[8]/100.0
    p_volt=sensor_val["voltage"]
    p_curr=sensor_val["current"]
    p_pf=sensor_val["powerfactor"]
    w1=sensor_val["power"]


    blynk.virtual_write(0,p_volt)
   # blynk.virtual_write(1,p_curr)
    blynk.virtual_write(2,p_pf)
    blynk.virtual_write(3,w1)
    primary.close()
    return w1

def secondary():
    secondary=serial.Serial("/dev/ttyUSB1",9600,timeout=1)
    secondary.flush()
    vs=secondary.readline().decode("utf-8").rstrip()
    blynk.virtual_write(5,vs)
    secondary.close()
    return vs

def final():
    primary()
    time.sleep(0.5)
    secondary()

if __name__=="__main__":
    init()
   
    while True:
       
        final()
        blynk.run()
