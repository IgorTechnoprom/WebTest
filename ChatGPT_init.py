import pyautogui
import pygetwindow as gw
import time

# Function to find and manage the window
def manage_window(window_title_part):
    window = None
    
    # Try to find the window by a partial title match
    for candidate_window in gw.getAllTitles():
        if window_title_part in candidate_window:
            window = gw.getWindowsWithTitle(candidate_window)[0]
            break

    if window:
        try:
            if not window.isActive:
                window.activate()
                time.sleep(0.5)  # Sleep to allow the window to become active

            if not window.isMaximized:
                window.maximize()

            if window.isMinimized:
                window.restore()

            return window, True
        except Exception as e:
            return None, False
    else:
        print(f"Window with title containing '{window_title_part}' not found.")
        return None, False

# Function to get the coordinates of the active window
def get_active_window_coordinates(window):
    if window:
        try:
            left, top, right, bottom = window.left, window.top, window.right, window.bottom
            width = right - left
            height = bottom - top
            center_x = left + width // 2
            center_y = top + height // 2
            return left, top, right, bottom, center_x, center_y, True
        except Exception as e:
            return None, None, False
    else:
        return None, None, False

# Function to calculate the target click location
def calculate_click_location(left, right, bottom, center_x, window_fraction):
    try:
        min_y = bottom - (window_fraction * (bottom - top))
        max_y = bottom
        click_x = center_x
        click_y = max_y - 150
        return click_x, click_y, True
    except Exception as e:
        return None, None, False

# Set the desired window title part to match
window_title_part = "ChatGPT - Google Chrome"

# Initialize success flag
success = True

# Find and manage the window
active_window, success = manage_window(window_title_part)

# If the window is active, proceed with the rest of the script
if success:
    # Get the active window coordinates
    left, top, right, bottom, center_x, center_y, success = get_active_window_coordinates(active_window)

    # If we have valid coordinates, proceed with the rest of the script
    if success:
        # Set the desired window fraction (adjust as needed)
        window_fraction = 0.8  # You can change this value between 0 and 1

        # Calculate the click location
        click_x, click_y, success = calculate_click_location(left, right, bottom, center_x, window_fraction)

        # If we have a valid click location, proceed with the clicks
        if success:
            # Move the mouse and perform a click at the calculated location
            try:
                pyautogui.moveTo(click_x, click_y)
                pyautogui.click()
                pyautogui.moveTo(click_x, click_y)
                pyautogui.click()
                pyautogui.moveTo(click_x, click_y)
                pyautogui.click()

                print(f"Clicking at ({click_x}, {click_y}) within the active window.")
            except Exception as e:
                success = False
                print(f"An error occurred while clicking: {str(e)}")
        else:
            print("Error calculating click location.")
    else:
        print("Error getting window coordinates.")
else:
    print("Error finding and managing the window.")

# Display success or error message
if success:
    print("Script executed successfully.")
else:
    print("Script encountered an error.")
