import pyautogui
import time

# Tìm chorme icon
coors = pyautogui.locateOnScreen('chorme.png', grayscale=True,confidence=0.7 )
coors_center = pyautogui.center(coors)
pyautogui.click((coors_center.x), (coors_center.y))

# Gõ facebook
pyautogui.hotkey('alt', 'd')
pyautogui.write("facebook.com")
pyautogui.press('enter')
time.sleep(3)

# Chọn thanh gõ
coors = pyautogui.locateOnScreen('search.png', grayscale=True,confidence=0.7 )
coors_center = pyautogui.center(coors)
pyautogui.click((coors_center.x), (coors_center.y))
time.sleep(3)       
pyautogui.write('Hello world!', interval=0)
time.sleep(3)
# Nhấn vào nút đăng
coors = pyautogui.locateOnScreen('dang.png', grayscale=True,confidence=0.7 )
coors_center = pyautogui.center(coors)
pyautogui.click((coors_center.x), (coors_center.y))