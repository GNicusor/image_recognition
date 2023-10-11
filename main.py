import pyautogui
import time
# Locate and click on an image
def click_image(image_path):
    try:
        location = pyautogui.locateOnScreen(image_path)
        if location:
            x, y = pyautogui.center(location)
            pyautogui.click(x, y)
            return True
        else:
            return False
    except Exception as e:
        print("Error:", e)
        return False
initial_delay = 5  # Adjust this to the desired delay

print(f"Waiting for {initial_delay} seconds before starting...")
time.sleep(initial_delay)

exit_after_seconds = 60

# Example usage
image_paths = ["images/1.png", "images/2.png"]

for image_path in image_paths:
    print(f"Clicking on {image_path}...")
    if click_image(image_path):
        print(f"Clicked {image_path}.")
    else:
        print(f"{image_path} not found.")