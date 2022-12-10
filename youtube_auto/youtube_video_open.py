import pyautogui

pyautogui.press("win")
pyautogui.write("google chrome")
pyautogui.press("enter")

pyautogui.moveTo(300,58,duration=2,
                 tween=pyautogui.easeInOutQuad)
pyautogui.click()

pyautogui.write("youtube.com"
)
pyautogui.press("enter")

pyautogui.moveTo(600, 163, duration=4,
                 tween=pyautogui.easeInOutQuad)
pyautogui.click()
pyautogui.write("müslüm gürses affet")
pyautogui.press("enter")

pyautogui.moveTo(600, 500, duration=4,
                 tween=pyautogui.easeInOutQuad)
pyautogui.click()

 




