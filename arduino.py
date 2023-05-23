import serial as s
import time as t
ser = s.Serial('COM5', 9600, timeout=0)   # check your com port
t.sleep(2)
print(ser.name,"connected")
print("Enter 1 to ON MOTOR & 0 to OFF MOTOR")
while 1:
    input_data = input()
    print("you enterd", input_data)
    
    if (input_data == '1'):
        ser.write(b'1')
        print ("MOTOR ON")
    if (input_data == '0'):
        ser.write(b'0')    
        print ("MOTOR OFF")
    if (input_data == '3'):
        ser.close() 