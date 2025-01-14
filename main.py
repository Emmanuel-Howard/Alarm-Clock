# An alarm clock program that plays music at the end

# Import 3 necessary modules
import datetime
import time
import pygame

# Main alarm function
def set_alarm(alarm_time):
    print(f"Alarm set for: {alarm_time}")   # Based on User input
    sound_file = r"C:\Users\Emmanuel\Desktop\Triage\CodingFiles\HelloWorld\That's the One - Ryan McCaffrey_Go By Ocean.mp3"
    is_running = True   # Set the program as running

    while is_running:   # While the program is running
        current_time = datetime.datetime.now().strftime("%H:%M:%S")   # Determine the current time
        print(current_time)

        if current_time == alarm_time:   # Once the current time reaches the alarm time
            print("WAKE UP!⏰ ")         # Print "WAKE UP!"

            # Initialize, load, and play sound effect
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            # Sets .get_busy(), playing the entire music file
            while pygame.mixer.music.get_busy():
                time.sleep(1)    # Checks the status (busy/not) every 1 second

            is_running = False   # Terminates the program

        # Waits one second between each print
        time.sleep(1)

# Main alarm program if name == main
if __name__ == "__main__":
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)