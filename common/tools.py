import requests

def convert_temp(temp):
    temp = temp - 273.15
    return temp

def convert_wind_speed(speed):
    speed = speed * 3.6
    return speed