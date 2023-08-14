
from datetime import datetime

def f_makePackage(Data, DataSize):
  step=Size=8*(DataSize+1)
  leng=Data<<8
  CRC=0

  while step<=Size: 
    if step == 8:
      CRC=leng >> DataSize*8 
      break 
    else:  
      if (leng >> (Size-1)) & 1 == 1:
        leng=(leng << 1) ^ ((213+256) << (Size-8))
      else:
        leng=(leng << 1)
    step=step-1
    
  Pac=[
        ('{'),
        Data.to_bytes(DataSize, 'big'), 
        CRC.to_bytes(1, 'big'),  
        ('}') 
      ]
      
  return Pac
   
#def Func(data: int)->bool:

now = datetime.now() 
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

import serial
ser = serial.Serial('COM3', 9600)   #init and open port

for i in range(7):
    ser.write(time_bt[i])           # write a string
ser.write(b'\xFF')    
ser.close()                         # close port

DataSize=1
Data=123

step=Size=8*(DataSize+1)
leng=Data<<8

'''
print("Leng= ", str(leng))

while step<=Size: 
  if step == 8:
    CRC=leng >> DataSize*8
    print("CRC= ", str(CRC)) 
    break 
  else:  
    if (leng >> (Size-1)) & 1 == 1:
      leng=(leng << 1) ^ ((213+256) << (Size-8))
      step=step-1
      print("1S",str(step),"= ", str(Size)) 
      print(" Leng= ", str(leng)) 
    else:
      leng=(leng << 1)
      step=step-1
      print("0S",str(step),"= ", str(Size))
      print(" Leng= ", str(leng))  
'''
#PR=f_makePackage(time_bt, 7)

#print ('pac=', str(PR))
    