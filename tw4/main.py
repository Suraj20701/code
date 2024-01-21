from serial import Serial
import time

arduino = Serial("COM4", baudrate=9600, timeout=1)
while True :
    ip =  input("Enter ON or OF : ")
    if ip == "ON" :
        arduino.write(bytes("1", "utf-8"))
        
    elif ip == "OF" :
        arduino.write(bytes("0", "utf-8"))
    else :
        print("Invalid option")

    rsp = arduino.readline()
    print(rsp.decode())
    
    
 

