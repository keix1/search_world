import pyautogui


def shot_cursor():
    print(pyautogui.position())
    position = pyautogui.position()

    x1 = position[0] - 20
    y1 = position[1] + 400
    x2 = 1200
    y2 = 300

    if x1 < 0:
        x1 = 0
    if y1 < 0:
        y1 = 0

    print(x1, y1, x2, y2)

    s = pyautogui.screenshot(
        region=(x1, y1, x2, y2)
    )
    s.save('screen.png')
