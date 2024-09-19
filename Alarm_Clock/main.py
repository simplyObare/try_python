import  datetime
import time
import pygame

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = "Burlesque - National Sweetheart.mp3"

if __name__ == "__main__":
    alarm_time = input("Set alarm (HH:MM:SS): ")
    set_alarm(alarm_time)