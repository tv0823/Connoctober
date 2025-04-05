# Create Buttons: helper, seeker
from Button import Button
from constants import *

seeker_button = Button(SEEKER_BUTTON_X_POS,
                     SEEKER_BUTTON_Y_POS,
                     SEEKER_BUTTON_WIDTH,
                     SEEKER_BUTTON_HEIGHT,
                       "Seeker", WHITE, YELLOW)

helper_button = Button(HELPER_BUTTON_X_POS,
                     HELPER_BUTTON_Y_POS,
                     HELPER_BUTTON_WIDTH,
                     HELPER_BUTTON_HEIGHT,
                       "Helper", WHITE, YELLOW)


go_back_button = Button(GO_BACK_BUTTON_X_POS,
                     GO_BACK_BUTTON_Y_POS,
                     GO_BACK_BUTTON_WIDTH,
                     GO_BACK_BUTTON_HEIGHT,
                       "Back", WHITE, YELLOW)


get_name_button = Button(NAME_BUTTON_X_POS,
                     NAME_BUTTON_Y_POS,
                     NAME_BUTTON_WIDTH,
                     NAME_BUTTON_HEIGHT,
                       "Name:", WHITE, YELLOW)

get_city_button = Button(CITY_BUTTON_X_POS,
                     CITY_BUTTON_Y_POS,
                     CITY_BUTTON_WIDTH,
                     CITY_BUTTON_HEIGHT,
                       "City:", WHITE, YELLOW)

next_button = Button(NEXT_BUTTON_X_POS,
                     NEXT_BUTTON_Y_POS,
                     NEXT_BUTTON_WIDTH,
                     NEXT_BUTTON_HEIGHT,
                       "Next", WHITE, YELLOW)


seek_help_button_lst = []
seek_help_button_lst.append(Button(SEEK_HELP_BUTTON_X_POS,
                                   SEEK_HELP_BUTTON_Y_POS + (SEEK_HELP_BUTTON_HEIGHT + 10) * (len(seek_help_button_lst) + 0.5),
                                   SEEK_HELP_BUTTON_WIDTH,
                                   SEEKER_BUTTON_HEIGHT,
                                   "Groceries shopping", WHITE, YELLOW))
seek_help_button_lst.append(Button(SEEK_HELP_BUTTON_X_POS,
                                   SEEK_HELP_BUTTON_Y_POS + (SEEK_HELP_BUTTON_HEIGHT + 10) * (len(seek_help_button_lst) + 0.5),
                                   SEEK_HELP_BUTTON_WIDTH,
                                   SEEKER_BUTTON_HEIGHT,
                                   "Doing laundry", WHITE, YELLOW))
seek_help_button_lst.append(Button(SEEK_HELP_BUTTON_X_POS,
                                   SEEK_HELP_BUTTON_Y_POS + (SEEK_HELP_BUTTON_HEIGHT + 10) * (len(seek_help_button_lst) + 0.5),
                                   SEEK_HELP_BUTTON_WIDTH,
                                   SEEKER_BUTTON_HEIGHT,
                                   "Walking the dog", WHITE, YELLOW))
seek_help_button_lst.append(Button(SEEK_HELP_BUTTON_X_POS,
                                   SEEK_HELP_BUTTON_Y_POS + (SEEK_HELP_BUTTON_HEIGHT + 10) * (len(seek_help_button_lst) + 0.5),
                                   SEEK_HELP_BUTTON_WIDTH,
                                   SEEKER_BUTTON_HEIGHT,
                                   "Cleaning the house", WHITE, YELLOW))
seek_help_button_lst.append(Button(SEEK_HELP_BUTTON_X_POS,
                                   SEEK_HELP_BUTTON_Y_POS + (SEEK_HELP_BUTTON_HEIGHT + 10) * (len(seek_help_button_lst) + 0.5),
                                   SEEK_HELP_BUTTON_WIDTH,
                                   SEEKER_BUTTON_HEIGHT,
                                   "Personal request", YELLOW, WHITE))
seek_help_button_lst.append(Button(SEEK_HELP_BUTTON_X_POS,
                                   SEEK_HELP_BUTTON_Y_POS + (SEEK_HELP_BUTTON_HEIGHT + 8) * (len(seek_help_button_lst) + 1),
                                   SEEK_HELP_BUTTON_WIDTH,
                                   SEEKER_BUTTON_HEIGHT,
                                   "SEND", WHITE, YELLOW))