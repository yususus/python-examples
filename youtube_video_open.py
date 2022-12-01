import pyautogui

pyautogui.press("win")
pyautogui.write("google chrome", interval=0.1)
pyautogui.press("enter")

pyautogui.moveTo(300,58,duration=2,
                 tween=pyautogui.easeInOutQuad)
pyautogui.click()

pyautogui.write("youtube.com", interval= 0.1)
pyautogui.press("enter")

pyautogui.moveTo(600, 163, duration=4,
                 tween=pyautogui.easeInOutQuad)
pyautogui.click()
pyautogui.write("müslüm gürses affet")
pyautogui.press("enter")

pyautogui.moveTo(600, 500, duration=4,
                 tween=pyautogui.easeInOutQuad)
pyautogui.click()

 




