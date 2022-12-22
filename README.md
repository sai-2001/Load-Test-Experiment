# LOAD-TEST-on-single-phase-transformer

***The Load test on single phase transformer generally consists of various electrical components like a rheostat, transformer, voltage sensor, etc. as shown in the fig.79. In this
experiment the direct load test is used to determine the performance of the transformer at
various loads.***

## Motivation

This is an electrical experiment. The idea behind building this experiment is to make
engineering level electrical experiments available to students through remote labs so that
they can access and control setups remotely from anywhere over internet.And also this
experiment involves characteristics which may not be clear to students when they perform
the experiment once in their labs, so as remote labs is accessible to students 24/7 they can
always revise which helps in better understanding of concepts.

## Therotical Aspects
### Project objectives

1. To provide web-based practical experience to students and allow them to perform
experiments over the internet.
2. To be able to provide an interactive user experience via the dashboard.
3. To conduct the load test on the given single phase transformer for finding the efficiency and its regulation.

## Theory

The main theory behind the experiment can be summarized as:
• The transformer is a device which transfers energy from one electrical circuit to
another electrical circuit through magnetic field coupling medium.
• It works on the basic principle of electromagnetic induction and has a very high
efficiency.
• When primary winding of transformer is energized with source of voltage V1 an
e.m.f. E2 is induced across the secondary winding and it is also equal to secondary
winding and it is also equal to secondary terminal voltage V2 till there is no load
across secondary winding.
• As soon as load is applied across the secondary winding the terminal voltage is decreased from E2 and V2 this phenomenon of changing the voltage is called ”voltage
regulation”.
• The formulas used are
``` percentage requlation=Vo2-v2/vo2*100```
Where V02 = Secondary voltage on no load
V0 = Secondary voltage at a particular load
``` Efficiency=P2/P1*100```
Where P2= Output Power
P1= Input Power
```P2=P1-PL```
Where PL= Losses
P2= Output Power
P1= Input Power


Now the direct load test performs on the single-phase transformer to determine the
voltage regulation and efficiency of transformer.

### Hardware Implementation

The load test is performed on a single phase transformer, to find out its efficiency and
regulation. In this method, a resistive load is connected to the transformer and it’s loaded
up to the rated current. This is direct loading method and can be applied to transformers
with a rating less than 5kVA. 
The Hardware setup is built using hardwood and cardboard. A support has been built
for placing rheostat on the cardboard. The rod is inserted into the rheostat holder and it is
screwed to the bottom part of the support as shown in the fig.88, and the rheostat holder is
coupled with the sliding contact of the rheostat. NEMA17 stepper motor has been attached
and it drives the mechanically driven chain of the Rod which moves the rheostat holder
to different positions. Single phase transformer has been placed on the cardboard for easy
understanding of experiment. The components are coupled with the PCB board and placed
at the bottom of the cardboard and the Pi cam is placed at a particular distance from the
setup for better visuals of the experiment.
### Procedure
PZEM module turns on as soon as the supply voltage is received. The module is used
to measure power, current, power factor readings and sends the readings to primary side
of the transformer. These readings can only be passed to the transformer when the relay
module is turned on by the raspberry pi. Then the signals are passed from the transformer
to voltage sensor to measure voltage reading and provides voltage reading to the rheostat
when relay is turned on by the raspberry pi. A4988 motor driver receives the required
signals from raspberry pi to actuate stepper motor. Raspberry pi camera module captures
the working and sends action data to raspberry pi which processes video data to YouTube
live streaming.The connections shown in the circuit diagram in fig.90 are designed using Fritzing software. the circuit is designed such that all the components are interfaced together with the
raspberry pi. Here, the NEMA17 motor works based on the signal transmitted from the
motor driver. A limit switch is connected to control the movement of the rheostat when
required.
An external 230volts AC supply is provided to the PZEM module which is connected
to the serial communication device and it is connected to the raspi. NodeMCU which is
included and connected to the voltage sensor. power bridge diodes and the capacitor are
connected to the terminals of the voltage sensor. primary relay is connected to the transformer’s primary side and PZEM module. secondary relay is connected to the transformer’s
secondary side and resistive load.
