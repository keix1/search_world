import pyautogui

print(pyautogui.position())
position = pyautogui.position()
x1 = position[0] - 20
y1 = position[1] + 120

if x1 < 0:
    x1 = 0
if y1 < 0:
    y1 = 0
x2 = 1200
y2 = 300

print(x1, y1, x2, y2)


s = pyautogui.screenshot(
#	imageFilename="screenshot.png",
    region=(x1, y1, x2, y2)
)
s.save('screen.png')
