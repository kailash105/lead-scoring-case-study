import pyautogui
import time

# Time to start the script, allowing you to focus on the input field
time.sleep(1) 
           

# Define the duration in seconds for how long the script should run
time_limit = 30  # for example, 30 seconds
start_time = time.time()

while time.time() - start_time < time_limit:
    pyautogui.typewrite("HI 😇")
    pyautogui.press("enter")
    time.sleep(1)  # Delay between messages to avoid spamming too quickly

print("Time limit reached. Script stopped.")
