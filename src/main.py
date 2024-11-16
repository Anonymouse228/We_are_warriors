from time import sleep as wait
from typing import Iterable

import keyboard
import pyautogui

from settings import *


def wait_before_run(time=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            wait(time)
            return func(*args, **kwargs)
        return wrapper
    return decorator


def strategy_1_spaceship_2_troopers():
    return 18.71, '3', '2', '2'


def strategy_1_warrior():
    return 18.5, '2'


@wait_before_run(2)
def upgrade_food_production_then_base_health():
    pyautogui.click(*UPGRADE_MENU_BUTTON)

    for _ in range(1):
        pyautogui.click(*UPGRADE_BUTTONS_LOCATIONS['food_production'])

    for _ in range(1):
        pyautogui.click(*UPGRADE_BUTTONS_LOCATIONS['base_health'])

    pyautogui.click(*BATTLE_MENU_BUTTON)


# def delete_unavailable_units(unit_order: Iterable) -> Iterable:
#     pyautogui.locateAllOnScreen()


def perform_battle(initial_wait_time: float, unit_order: Iterable) -> None:
    pyautogui.click(*START_BATTLE_BUTTON)
    # unit_order = delete_unavailable_units(unit_order)

    wait(initial_wait_time)
    while battle_is_going_on():
        for unit in unit_order:
            buy_unit(unit)
    else:
        go_to_home_page_after_battle()


def battle_is_going_on() -> bool:
    try:
        pyautogui.locateOnScreen(str(FIGHT_INDICATOR_IMAGE_PATH))
        return True
    except pyautogui.ImageNotFoundException:
        return False


@wait_before_run(1)
def go_to_home_page_after_battle() -> None:
    try:
        pyautogui.locateOnScreen(str(COINS_COLLECTED_INDICATOR_IMAGE))
        pyautogui.click(*EXIT_PAID_BATTLE_BUTTON)
    except pyautogui.ImageNotFoundException:
        pass


def buy_unit(number: str) -> None:
    unit = BATTLE_UNITS[number]
    while battle_is_going_on():
        try:
            pyautogui.locateOnScreen(str(ACTIVE_UNIT_INDICATOR_IMAGE_PATH), region=unit['active_indicator_region'])
            pyautogui.click(*unit['click_point'])
            break
        except pyautogui.ImageNotFoundException:
            wait(UNIT_AVAILABILITY_WAIT_TIME)


if __name__ == '__main__':
    food_production = INITIAL_FOOD_PRODUCTION
    initial_wait_time, *unit_order = strategy_1_warrior()
    make_upgrades = upgrade_food_production_then_base_health

    wait(PROGRAM_START_DELAY_TIME)
    while not keyboard.is_pressed(STOP_KEY):
        perform_battle(initial_wait_time, unit_order)
        make_upgrades()
