import time
import pyautogui
import keyboard

# Biến cờ để kiểm tra xem chương trình có tiếp tục hay không
continue_program = True

# Define function to pause script when Z is pressed
def pause_script(event):
    global continue_program
    if event.name == 'z':
        continue_program = False

# Register the pause_script function to listen for Z key press
keyboard.on_press(pause_script)

# Wait for 5 seconds to switch to the browser window
time.sleep(5)

# Coordinates of the input field
input_field_x = 850
input_field_y = 770

# Coordinates of the "Submit" button
submit_button_x = 850
submit_button_y = 845

# Loop through from 0000 to 9999 while continue_program is True
code = 0
while code < 10000 and continue_program:
    pyautogui.click(input_field_x, input_field_y)
    pyautogui.hotkey('ctrl', 'a')
    code_str = str(code).zfill(4)
    pyautogui.typewrite(code_str, interval=0.00005)  # Giảm thời gian chờ giữa các ký tự
    pyautogui.click(submit_button_x, submit_button_y)
    code += 1
    time.sleep(0.0005)  # Giảm thời gian chờ sau mỗi lần nhấn nút "Submit"
