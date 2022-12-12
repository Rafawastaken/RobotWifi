from modules_robot.motor_driver import MotorDriver
import machine
from time import sleep
import urequests as requests
import network
import json
import gc

"""
    D1(NodeMCU) = GPIO5(ESP8266) = PWM of Motor A
    D3(NodeMCU) = GPIO0(ESP8266) = DIR of Motor A
    D2(NodeMCU) = GPIO4(ESP8266) = PWM of Motor B
    D4(NodeMCU) = GPIO2(ESP8266) = DIR of Motor B
"""

# Initialize Board
def initialize_board():
    # Garbage Collector
    print("Initialize Garbage Collector")
    gc.collect() 
    
    # Connect to wifi
    print("Checking connection to network")
    station = network.WLAN(network.STA_IF)
    
    if not station.isconnected():
        print("Connecting to network...")
        station.active(True)
        station.connect("MEO-8974B0", "588d1b30e7")
        
        while not station.isconnected():
            pass
        
    print("Connected!")


def com_server():
    # Send request to server
    r = requests.get("http://192.168.1.75:5000/robot-com")
    
    # If response is OK
    if r.status_code == 200:
        return r.json()
    return False


def main():
    # Create motors
    motor_driver = MotorDriver(5, 0, 4, 2)
    initialize_board()
    server_response = com_server()
    
    print(server_response)
    
    for attr, value in server_response.items():
        if value:
            if attr == "forward": motor_driver.forward()
            elif attr == "backwards": motor_driver.backwards()
            elif attr == "left": motor_driver.left()
            elif attr == "right": motor_driver.right()
            elif attr == "stop": motor_driver.stop()

    
if __name__ == '__main__':
    main()
