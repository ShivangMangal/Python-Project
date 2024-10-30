import time
import pygame

def set_alarm(alarm_time):
    while True:
        current_time = time.strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Time to wake up!")
            play_alarm_sound()
            break
        time.sleep(1)

def play_alarm_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("alarm_sound.mp3")  # Provide path to your alarm sound file
    pygame.mixer.music.play()

def main():
    alarm_time = input("Enter the time for the alarm (format HH:MM:SS): ")
    set_alarm(alarm_time)

if __name__ == "__main__":
    main()
