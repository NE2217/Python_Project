
import serial

ser = serial.Serial('COM3', 9600)
print(ser.name)         # check which port was really used
ser.write(b'hello')     # write a string
ser.close()             # close port

from datetime import datetime
now = datetime.now() 
current_time = now.strftime("%H:%M:%S") 
current_data = now.strftime("%d/%m/%Y") 
print("Current Time =", current_time)
print("Data =", current_data)

