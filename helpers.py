import pygame

from buttons import go_back_button
from constants import *

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)


def from_text_to_array(text):
    """
    the function get text and break it into sentences that fits the screen, in
    case the text too long to for one line
    :param text: string
        text to show on screen
    :return: list of sentences
    """
    text_array = []
    text_to_edit = text
    if len(text) > 20:
        while not (len(text_to_edit) <= 0):
            if len(text_to_edit) < LINE_MAX_LENGTH:
                text_array.append(text_to_edit)
                text_to_edit = ""
            else:
                temp = text_to_edit[0: LINE_MAX_LENGTH]
                text_to_edit = text_to_edit[LINE_MAX_LENGTH:]
                while not (temp[-1] == ' ') and not (temp[-1] == ','):
                    text_to_edit = temp[-1] + text_to_edit
                    temp_len = int(len(temp))
                    temp = temp[0: temp_len - 1]
                text_array.append(temp)
    else:
        text_array.append(text)
    return text_array


def mouse_in_button(button, mouse_pos):
    """
    The function get button and mouse press position on screen and return True
    if mouse click on button
    :param button: Button object
        button on screen
    :param mouse_pos: tuple
        the x and y position of the mouse cursor
    :return: boolean
        True if mouse click on button, else False
    """
    if button.x_pos + button.width > mouse_pos[0] > button.x_pos and \
            button.y_pos < mouse_pos[1] < button.y_pos + button.height:
        return True


def display_text(sen, size, y, x = None):
    # display sen on screen
    font = pygame.font.SysFont(None, size)
    text = font.render(sen, True, BROWN)

    if x == None: # places it in the middle of the screen
        x = (WINDOW_WIDTH - text.get_width()) // 2

    screen.blit(text, (x, y))

def get_text_input(X, Y, BOX_COLOR, CENTER):
    pressed_enter = False
    text = ""

    input_box_width = 200
    input_box_height = 40

    font = pygame.font.SysFont(None, 30)

    # places it in the middle of the screen
    if X is None:
        X = (WINDOW_WIDTH - input_box_width) // 2

    while not pressed_enter:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pressed_enter = True
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

        # Clear the previous text area only
        pygame.draw.rect(screen, BOX_COLOR, (X, Y, input_box_width, input_box_height))

        # Use your display_text function
        if(CENTER):
            display_text(text, 30, Y + 20)
        else:
            display_text(text, 30, Y, X)

        pygame.display.update()

    return text


def display_request_details(request, screen):
    requester, details, city, phone = request.openRequest()

    display_text(requester, 30, USER_DETAILS_Y, USER_DETAILS_X)
    display_text(details, 25, USER_DETAILS_Y + 50, USER_DETAILS_X)
    display_text(city, 25, USER_DETAILS_Y + 100, USER_DETAILS_X)
    display_text(phone, 25, USER_DETAILS_Y + 150, USER_DETAILS_X)
    go_back_button.draw(screen)

def handle_go_back_button(screen_mode):
    if screen_mode == "seeker_screen":
        return "log_in_screen"  # Go back to the login screen
    elif screen_mode == "helper_screen":
        return "log_in_screen"  # Go back to the login screen
    elif screen_mode == "request_details_screen":
        return "helper_screen" # Go back to the helper screen
    return screen_mode
