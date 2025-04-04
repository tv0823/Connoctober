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

go_back_button = Button(GO_BACK_BUTTON_X_POS,
                     GO_BACK_BUTTON_Y_POS,
                     GO_BACK_BUTTON_WIDTH,
                     GO_BACK_BUTTON_HEIGHT,
                       "Back", YELLOW, WHITE)

seek_help_button_lst = []
seek_help_button_lst.append(Button(SEEK_HELP_BUTTON_X_POS,
                                   SEEK_HELP_BUTTON_Y_POS + (SEEK_HELP_BUTTON_HEIGHT + 10) * (len(seek_help_button_lst) + 1),
                                   SEEK_HELP_BUTTON_WIDTH,
                                   SEEKER_BUTTON_HEIGHT,
                                   "Groceries shopping", YELLOW, WHITE))
seek_help_button_lst.append(Button(SEEK_HELP_BUTTON_X_POS,
                                   SEEK_HELP_BUTTON_Y_POS + (SEEK_HELP_BUTTON_HEIGHT + 10) * (len(seek_help_button_lst) + 1),
                                   SEEK_HELP_BUTTON_WIDTH,
                                   SEEKER_BUTTON_HEIGHT,
                                   "Doing laundry", YELLOW, WHITE))
seek_help_button_lst.append(Button(SEEK_HELP_BUTTON_X_POS,
                                   SEEK_HELP_BUTTON_Y_POS + (SEEK_HELP_BUTTON_HEIGHT + 10) * (len(seek_help_button_lst) + 1),
                                   SEEK_HELP_BUTTON_WIDTH,
                                   SEEKER_BUTTON_HEIGHT,
                                   "Walk dog", YELLOW, WHITE))
seek_help_button_lst.append(Button(SEEK_HELP_BUTTON_X_POS,
                                   SEEK_HELP_BUTTON_Y_POS + (SEEK_HELP_BUTTON_HEIGHT + 10) * (len(seek_help_button_lst) + 1),
                                   SEEK_HELP_BUTTON_WIDTH,
                                   SEEKER_BUTTON_HEIGHT,
                                   "Get medication", YELLOW, WHITE))