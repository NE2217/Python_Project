
from datetime import datetime
now = datetime.now() 
current_time = now.strftime("%H:%M:%S") 
current_data = now.strftime("%d/%m/%Y")
time=[ 
        int(now.strftime("%Y"))-2000,
        int(now.strftime("%m")),
        int(now.strftime("%d")), 
        int(now.strftime("%H")),
        int(now.strftime("%M")),
        int(now.strftime("%S")),
        now.weekday()+1,
     ]
        
time_bt=[time[i].to_bytes(1, 'big') for i in range(7)]  

print("Current Time =", current_time)
print("Data =", current_data)

print("send =",  time_bt)
import serial

ser = serial.Serial('COM3', 9600)
for i in range(7):
    ser.write(time_bt[i])    # write a string
ser.write(b'\xFF')    
ser.close()           # close port