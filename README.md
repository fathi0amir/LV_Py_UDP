# LV_Py_UDP

I have been developing and imaging system that can monitor the brain activity 
at cellular level in a transgenic adult zebrafish brain. The imaging is done 
while the animal is swimming in an immersive virtual reality environment. 
The animal is head-fixed and forces are recoded with a load cell. With the 
sensors data I could get necessary metric to navigate in a 3D rendering 
environment. In our case, we used Panda3D which can be scripted in Python. The main 
challenge was how to send the meterics recorded in LabVIEW to the Python 
script. There are several ways to that, such as, Python node VI in LabVIEW, 
ActivX object, TCP and UDP. I chose UDP as I need fast (less than 10 ms) 
communication. ActiveX and Python node VI were not fast enough for my 
application. Although UDP is a lossy protocol, it is still suitable for my application. 

In this reporsitory I have uploaded 4 files. 
LV_UDP_SNDR -> PY_UDP_RCVR
PY_UDP_SNDR -> LV_UDP_RCVR

For reciever on the python side I have modified an UDP socket options, 
that limits the native buffer on the python side. This small project 
was put together to make sure Python and LabVIEW are in sync and in 
real-time. The important factor is to be in sync at all time therefore 
the data-point are not read from buffer on either sides. In my case, 
if any packet get lost, it's replaced by a previously knows value 
in the main program. All the senders and recievers are time-out to match 
my deisred sampling rate (100 Hz). 

I hope this can be of any use in someones projects or sparks some 
awesome idea somewhere, somehow. 
