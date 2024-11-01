import pyautogui as pg
import time

coordinates = [
    (1173, 479),
    (1107, 281),
    (639, 396),
    (1101, 519),
    (625, 640),
    (700, 695)
]

def perform_actions():
    pg.hotkey('alt', 'tab')
    time.sleep(0.5)
    
    for i in range(2, 15):
        pg.click(coordinates[0])
        time.sleep(0.5)  # Add a short delay

        pg.click(coordinates[1])
        time.sleep(0.5)

        # Mouse click at the third coordinate
        pg.click(coordinates[2])
        time.sleep(2.5)

        # Type "inputXX.txt" and press enter
        pg.typewrite(f"input{i:02}.txt")
        time.sleep(0.5)
        pg.press('enter')
        time.sleep(0.5)

        # Mouse click at the fourth coordinate
        pg.click(coordinates[3])
        time.sleep(0.5)

        # Mouse click at the fifth coordinate
        pg.click(coordinates[4])
        time.sleep(2.5)

        # Type "outputXX.txt" and press enter
        pg.typewrite(f"output{i:02}.txt")
        time.sleep(0.5)
        pg.press('enter')
        time.sleep(0.5)

        # Scroll down
        pg.scroll(-100)  # Adjust the scroll amount as needed
        time.sleep(0.5)

        # Mouse click at the sixth coordinate
        pg.click(coordinates[5])
        time.sleep(5)

        # Scroll up
        pg.scroll(5000)  # Adjust the scroll amount as needed
        time.sleep(0.5)

# Run the function
perform_actions()