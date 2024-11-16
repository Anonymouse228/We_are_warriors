import json
from pathlib import Path

__all__ = (
    'STOP_KEY',
    'FIGHT_INDICATOR_IMAGE_PATH',
    'ACTIVE_UNIT_INDICATOR_IMAGE_PATH',
    'COINS_COLLECTED_INDICATOR_IMAGE',
    'UPGRADE_MENU_BUTTON',
    'UPGRADE_BUTTONS_LOCATIONS',
    'BATTLE_MENU_BUTTON',
    'START_BATTLE_BUTTON',
    'BATTLE_UNITS',
    'EXIT_PAID_BATTLE_BUTTON',
    'PROGRAM_START_DELAY_TIME',
    'INITIAL_FOOD_PRODUCTION',
    'FOOD_PRODUCTION_UPGRADE_INCREMENT',
    'UNIT_AVAILABILITY_WAIT_TIME',
)

STOP_KEY = 'esc'

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / 'data'
IMAGES_PATH = DATA_PATH / 'images'
FIGHT_INDICATOR_IMAGE_PATH = IMAGES_PATH / 'fight_indicator_image.png'
ACTIVE_UNIT_INDICATOR_IMAGE_PATH = IMAGES_PATH / 'active_unit_indicator_image.png'
COINS_COLLECTED_INDICATOR_IMAGE = IMAGES_PATH / 'coins_collected_indicator_image.png'

MOUSE_POINTS_PATH = DATA_PATH / 'click_data.json'
with open(MOUSE_POINTS_PATH) as file:
    mouse_points = json.load(file)

UPGRADE_MENU_BUTTON = mouse_points['upgrade_menu_button']
UPGRADE_BUTTONS_LOCATIONS = mouse_points['upgrade_buttons_locations']
BATTLE_MENU_BUTTON = mouse_points['battle_menu_button']
START_BATTLE_BUTTON = mouse_points['start_battle_button']
BATTLE_UNITS = mouse_points['battle_units']
EXIT_PAID_BATTLE_BUTTON = mouse_points['exit_paid_battle_button']

PROGRAM_START_DELAY_TIME = 5
INITIAL_FOOD_PRODUCTION = 1.96
FOOD_PRODUCTION_UPGRADE_INCREMENT = 0.02

UNIT_AVAILABILITY_WAIT_TIME = 0.1
