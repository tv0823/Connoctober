# Create Buttons: helper, seeker
from Button import Button
from constants import *

seeker_button = Button(SEEKER_BUTTON_X_POS,
                     SEEKER_BUTTON_Y_POS,
                     SEEKER_BUTTON_WIDTH,
                     SEEKER_BUTTON_HEIGHT,
                       "Seeker", YELLOW, WHITE)

helper_button = Button(HELPER_BUTTON_X_POS,
                     HELPER_BUTTON_Y_POS,
                     HELPER_BUTTON_WIDTH,
                     HELPER_BUTTON_HEIGHT,
                       "Helper", YELLOW, WHITE)