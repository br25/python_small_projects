"""
Linux Alarm Clock

This alarm clock script is intended for Linux users. It allows you to set an alarm in 12-hour format
with AM and PM support and plays an alarm sound when the alarm time is reached.

Author: Md Ashraful Islam Robin
"""
import time
import pygame

def set_alarm():
    try:
        # Prompt the user for the alarm time in HH:mm AM/PM format
        alarm_time = input("Enter HH:mm and AM/PM: ")
        
        # Split the input into time and period (AM/PM)
        time_components = alarm_time.split(" ")
        time = time_components[0]
        period = time_components[1].upper()

        # Extract the hours and minutes
        hours, minutes = map(int, time.split(":"))
        
        # Convert to 24-hour format
        if period == "PM" and hours < 12:
            hours += 12
        elif period == "AM" and hours == 12:
            hours = 0

        # Calculate the alarm time in seconds since midnight
        alarm_seconds = hours * 3600 + minutes * 60
        return alarm_seconds
    except ValueError:
        print("Invalid input format. Please use HH:mm AM/PM.")
        return set_alarm()

def set_sound():
    # Initialize the Pygame mixer for audio
    pygame.mixer.init()
    
    # Load the alarm sound
    pygame.mixer.music.load("./mixkit-warning-alarm-buzzer-991.wav")
    
    # Play the alarm sound
    pygame.mixer.music.play()
    
    # Delay for 8 seconds (adjust as needed)
    pygame.time.delay(8000)

def main():
    # Set the alarm time in seconds since midnight
    alarm_seconds = set_alarm()

    while True:
        # Get the current time
        current_time = time.localtime()
        
        # Calculate the current time in seconds since midnight
        current_seconds = current_time.tm_hour * 3600 + current_time.tm_min * 60 + current_time.tm_sec

        if current_seconds == alarm_seconds:
            # It's time to wake up
            print("Wake Up")
            set_sound()  # Play the alarm sound
            break
        else:
            time.sleep(1)  # Wait for 1 second before checking again

if __name__ == "__main__":
    main()
