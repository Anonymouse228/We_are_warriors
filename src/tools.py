import time
import keyboard
import pyautogui

# from settings import LOSE_IMAGE_PATH

#  Get mouse position script
#
while True:
    keyboard.wait('a')
    print(pyautogui.position())


# # Save 'Dealer Wins!' position as screenshot
# time.sleep(3)
# pyautogui.screenshot('data/images/lose_image.png', region=(743, 232, 400, 67))


# # Check 'pyautogui.locateOnScreen' function
# time.sleep(3)
# while True:
#     try:
#         pyautogui.locateOnScreen(LOSE_IMAGE)
#         print('yes')
#     except pyautogui.ImageNotFoundException:
#         print('no')


# # First version
# bet = 1
# bet_degree = 1.029
# attempts = 38
# win_coeff = 36
#
# expenses = 0
# for attempt in range(attempts):
#     print(f'{attempt + 1} bet = {bet}')
#     expenses += bet
#     bet *= bet_degree
#
# print(expenses + bet)
# print(bet)
# print(bet * win_coeff)
# print(bet * win_coeff / (expenses + bet))
