import pygame
from buttons import *
from helpers import *
from Seeker import *
from Helper import *
from HelpRequest import *

def main():
    pygame.init()
    pygame.display.set_caption('Connoctober')
    clock = pygame.time.Clock()

    background = pygame.image.load('Images/background.png')
    background = pygame.transform.scale(background, (WINDOW_WIDTH, WINDOW_HEIGHT))

    seekers_lst = []
    helpers_lst = []

    selected_seeker = None
    seeker_rects = []
    selected_request = None  # Variable to hold the selected request

    seek_help_in = ""
    name = ""
    city = ""
    phone = ""

    screen_mode = "user_info_screen"

    running = True
    waiting_for_release = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and not waiting_for_release:
                pos = pygame.mouse.get_pos()

                if mouse_in_button(seeker_button, pos) and screen_mode == "log_in_screen":
                    seeker = Seeker(name, city)
                    seekers_lst.append(seeker)
                    screen_mode = "seeker_screen"
                    waiting_for_release = True

                elif mouse_in_button(helper_button, pos) and screen_mode == "log_in_screen":
                    helper = Helper()
                    helper.updateOperatingLocation(city)
                    helpers_lst.append(helper)
                    screen_mode = "helper_screen"
                    waiting_for_release = True

                elif mouse_in_button(go_back_button, pos):
                    screen_mode = handle_go_back_button(screen_mode)
                    waiting_for_release = True

                elif mouse_in_button(get_name_button, pos) and screen_mode == "user_info_screen":
                    name = get_text_input(NAME_BUTTON_X_POS + NAME_BUTTON_WIDTH + 10, NAME_BUTTON_Y_POS + NAME_BUTTON_HEIGHT // 3, BACKGROUND_COLOR, False)

                elif mouse_in_button(get_city_button, pos) and screen_mode == "user_info_screen":
                    city = get_text_input(CITY_BUTTON_X_POS + CITY_BUTTON_WIDTH + 10, CITY_BUTTON_Y_POS + CITY_BUTTON_HEIGHT // 3, BACKGROUND_COLOR, False)

                elif mouse_in_button(get_phone_button, pos) and screen_mode == "user_info_screen":
                    phone = get_text_input(PHONE_BUTTON_X_POS + PHONE_BUTTON_WIDTH + 10, PHONE_BUTTON_Y_POS + PHONE_BUTTON_HEIGHT // 3, BACKGROUND_COLOR, False)

                elif mouse_in_button(next_button, pos) and screen_mode == "user_info_screen" and name != "" and city != "" and phone != "":
                    screen_mode = "log_in_screen"
                    waiting_for_release = True

                elif mouse_in_button(accept_seek_button, pos) and screen_mode == "request_details_screen":
                    # when the helper finished helping the person it removes the request from the screen
                    if selected_seeker in seekers_lst:
                        seekers_lst.remove(selected_seeker)
                    selected_seeker = None
                    selected_request = None
                    screen_mode = "helper_screen"
                    waiting_for_release = True


                elif screen_mode == "seeker_screen":
                    for button in seek_help_button_lst:
                        if mouse_in_button(button, pos):
                            if button.text == "Personal request":
                                personal_req = get_text_input(SEEK_HELP_BUTTON_X_POS, SEEK_HELP_BUTTON_Y_POS + (SEEK_HELP_BUTTON_HEIGHT + 10) * (4 + 0.5), BTN_COLOR, True)
                                seek_help_in = personal_req
                            elif button.text != "SUBMIT":
                                seek_help_in = button.text
                            elif button.text == "SUBMIT":
                                if seekers_lst:
                                    seekers_lst[-1].setHelp(seek_help_in)

                elif screen_mode == "helper_screen":
                    for rect, seeker in seeker_rects:
                        if rect.collidepoint(pos):
                            selected_seeker = seeker
                            # Create a new HelpRequest object for the selected seeker
                            selected_request = HelpRequest(selected_seeker.getName(), selected_seeker.getHelp(), city, phone)
                            screen_mode = "request_details_screen"  # Switch to request details screen

            elif event.type == pygame.MOUSEBUTTONUP:
                waiting_for_release = False

        screen.fill(BLACK)
        screen.blit(background, (0, 0))

        if screen_mode == "user_info_screen":
            get_name_button.draw(screen)
            get_city_button.draw(screen)
            get_phone_button.draw(screen)

            next_button.draw(screen)
            display_text("Welcome to Connoctober", 35, WELCOME_TEXT_Y_POS)
            display_text("please enter your information", 32, WELCOME_TEXT_Y_POS + 25)
            display_text(name, 30, NAME_BUTTON_Y_POS + NAME_BUTTON_HEIGHT // 3, NAME_BUTTON_X_POS + NAME_BUTTON_WIDTH + 10)
            display_text(city, 30, CITY_BUTTON_Y_POS + CITY_BUTTON_HEIGHT // 3, CITY_BUTTON_X_POS + CITY_BUTTON_WIDTH + 10)
            display_text(phone, 30, PHONE_BUTTON_Y_POS + PHONE_BUTTON_HEIGHT // 3, PHONE_BUTTON_X_POS + PHONE_BUTTON_WIDTH + 10)

        elif screen_mode == "log_in_screen":
            seeker_button.draw(screen)
            helper_button.draw(screen)
            display_text("Welcome to Connoctober", 35, WELCOME_TEXT_Y_POS)
            display_text("please choose your role", 32, WELCOME_TEXT_Y_POS + 25)

        elif screen_mode == "seeker_screen":
            go_back_button.draw(screen)
            display_text(name, 30, 5, 5)
            display_text(city, 30, 30, 5)
            display_text("Choose what you need help in", 32, CHOOSE_HELP_TEXT_Y)
            for button in seek_help_button_lst:
                button.draw(screen)

        elif screen_mode == "helper_screen":
            go_back_button.draw(screen)
            display_text(name, 30, 5, 5)
            display_text(city, 30, 30, 5)
            display_text("Seekers who need help:", 32, HELPER_LIST_Y - 40)

            seeker_rects.clear()  # Clear the list of rectangles each time the helper screen is drawn
            i = 0
            for seeker in seekers_lst:
                if seeker.getHelp() != "":
                    help_text = f"{seeker.getHelp()} in {city}"
                    rect = pygame.Rect(HELPER_LIST_X, HELPER_LIST_Y + i * 50, HELPER_LIST_WIDTH, HELPER_LIST_HEIGHT)

                    # Highlight the selected seeker
                    if seeker == selected_seeker:
                        color = BTN_COLOR
                    else:
                        color = YELLOW

                    pygame.draw.rect(screen, color, rect)
                    display_text(help_text, 24, rect.y + 10, rect.x + 10)

                    # Save rect of the seeker for easy access
                    seeker_rects.append((rect, seeker))
                    i += 1

        elif screen_mode == "request_details_screen":
            if selected_request:
                display_request_details(selected_request, screen)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()

main()
