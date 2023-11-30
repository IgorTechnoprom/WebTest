import pyautogui
import pygetwindow as gw
import time
import keyboard
import pyperclip
import re

# Function to find and manage the window
def manage_window(window_title_part):
    window = None
    
    # Try to find the window by a partial title match
    for candidate_window in gw.getAllTitles():
        if window_title_part in candidate_window:
            window = gw.getWindowsWithTitle(candidate_window)[0]
            break

    if window:
        if not window.isActive:
            window.activate()
            time.sleep(0.5)  # Sleep to allow the window to become active

        if not window.isMaximized:
            window.maximize()
        
        if window.isMinimized:
            window.restore()
        
        return window
    else:
        print(f"Window with title containing '{window_title_part}' not found.")
        return None

# Function to get the coordinates of the active window
def get_active_window_coordinates(window):
    if window:
        left, top, right, bottom = window.left, window.top, window.right, window.bottom
        width = right - left
        height = bottom - top
        center_x = left + width // 2
        center_y = top + height // 2
        return left, top, right, bottom, center_x, center_y
    else:
        return None

# Function to calculate the target click location
def calculate_click_location(left, right, bottom, center_x, window_fraction):
    min_y = bottom - (window_fraction * (bottom - top))
    max_y = bottom
    click_x = center_x
    click_y = center_y
    return click_x, click_y

# Set the desired window title part to match
window_title_part = "ChatGPT - Google Chrome"

# Find and manage the window
active_window = manage_window(window_title_part)

# If the window is active, proceed with the rest of the script
if active_window:
    # Get the active window coordinates
    left, top, right, bottom, center_x, center_y = get_active_window_coordinates(active_window)

    # Set the desired window fraction (adjust as needed)
    window_fraction = 0.8  # You can change this value between 0 and 1

    # Calculate the click location
    click_x, click_y = calculate_click_location(left, right, bottom, center_x, window_fraction)

    # Move the mouse and perform a click at the calculated location
    pyautogui.moveTo(click_x, click_y)
    pyautogui.click()
    pyautogui.moveTo(click_x, click_y)
    pyautogui.click()
    # Send CTRL+A to select all the content
    keyboard.press('ctrl')
    keyboard.press_and_release('a')
        
    # Wait for a brief moment
    time.sleep(1)

    # Send CTRL+C to copy the selected content to the clipboard
    keyboard.press_and_release('c')
    keyboard.release('ctrl')
        
    # Wait for a brief moment
    time.sleep(1)
       
    # Get the copied text content from the clipboard
    content = pyperclip.paste()

    # Remove double spaces, newline characters, and consecutive paragraph breaks
    cleaned_text = re.sub(r'  +', ' ', content)  # Remove double spaces
    cleaned_text = re.sub(r'\n', ' ', cleaned_text)  # Remove newline characters
    cleaned_text = re.sub(r'\n\n+', '\n\n', cleaned_text)  # Remove consecutive paragraph breaks

    # Insert paragraph breaks before "User" and "ChatGPT"
    cleaned_text = re.sub(r'User', '\n\nUser', cleaned_text)
    cleaned_text = re.sub(r'ChatGPT', '\n\nChatGPT', cleaned_text)

    # Create an HTML document with the cleaned text
    html_content = f"<html><body>{cleaned_text}</body></html>"

    # Write the HTML content to a file named 'respond.html'
    with open('respond.html', 'w', encoding='utf-8') as file:
        file.write(html_content)

    print("Text content copied from the active window and saved to 'respond.html'")

    print(f"Clicking at ({click_x}, {click_y}) within the active window.")
