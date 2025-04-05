import pygame
from buttons import *
from helpers import *
from Seeker import *
from Helper import *

def main():
    # Set up the game display, clock and headline
    pygame.init()

    # Change the title of the window
    pygame.display.set_caption('Connoctober')

    clock = pygame.time.Clock()

    # Set up background image
    background = pygame.image.load('Images/background.png')
    background = pygame.transform.scale(background,
                                        (WINDOW_WIDTH, WINDOW_HEIGHT))

    seekers_lst = []
    helpers_lst = []

    name = ""
    city = ""

    screen_mode = "user_info_screen"

    running = True
    waiting_for_release = False

    while running:
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and not waiting_for_release:
                pos = pygame.mouse.get_pos()

                if(mouse_in_button(seeker_button, pos) and screen_mode == "log_in_screen"):
                    seeker = Seeker("Beer-Sheva")
                    seekers_lst.append(seeker)
                    screen_mode = "seeker_screen"
                    waiting_for_release = True

                elif(mouse_in_button(helper_button, pos) and screen_mode == "log_in_screen"):
                    helper = Helper()
                    helpers_lst.append(helper)
                    screen_mode = "helper_screen"
                    waiting_for_release = True

                elif(mouse_in_button(go_back_button, pos) and screen_mode != "log_in_screen"):
                    screen_mode = "log_in_screen"
                    waiting_for_release = True

                elif(mouse_in_button(get_name_button, pos) and screen_mode == "user_info_screen"):
                    name = get_text_input(NAME_BUTTON_X_POS + NAME_BUTTON_WIDTH + 10, NAME_BUTTON_Y_POS + NAME_BUTTON_HEIGHT//3)
                elif(mouse_in_button(get_city_button, pos) and screen_mode == "user_info_screen"):
                    city = get_text_input(CITY_BUTTON_X_POS + CITY_BUTTON_WIDTH + 10, CITY_BUTTON_Y_POS + CITY_BUTTON_HEIGHT //3)
                elif(mouse_in_button(next_button, pos) and screen_mode == "user_info_screen" and name != "" and city != ""):
                    screen_mode = "log_in_screen"
                    waiting_for_release = True


                elif(screen_mode == "seeker_screen"):
                    for button in seek_help_button_lst:
                        if(mouse_in_button(button, pos)):
                            print(button.text)
            elif event.type == pygame.MOUSEBUTTONUP:
                waiting_for_release = False

        # Display background and buttons
        screen.fill(BLACK)
        screen.blit(background, (0, 0))

        if(screen_mode == "user_info_screen"):
            get_name_button.draw(screen)
            get_city_button.draw(screen)
            next_button.draw(screen)

            welcome_msg = "Welcome to Connoctober"
            choose_role_msg = "please enter your information"
            display_text(welcome_msg , 35, WELCOME_TEXT_Y_POS)
            display_text(choose_role_msg, 32, WELCOME_TEXT_Y_POS + 25)

            # displays the name and city of the user
            display_text(name, 30, NAME_BUTTON_Y_POS + NAME_BUTTON_HEIGHT//3, NAME_BUTTON_X_POS + NAME_BUTTON_WIDTH + 10)
            display_text(city, 30, CITY_BUTTON_Y_POS + CITY_BUTTON_HEIGHT//3, CITY_BUTTON_X_POS + CITY_BUTTON_WIDTH + 10)


        elif(screen_mode == "log_in_screen"):
            seeker_button.draw(screen)
            helper_button.draw(screen)

            welcome_msg = "Welcome to Connoctober"
            choose_role_msg = "please choose your role"
            display_text(welcome_msg , 35, WELCOME_TEXT_Y_POS)
            display_text(choose_role_msg, 32, WELCOME_TEXT_Y_POS + 25)

        elif(screen_mode == "seeker_screen"):
            go_back_button.draw(screen)

            display_text(name, 30, 5, 5)
            display_text(city, 30, 30, 5)

            choose_help_msg = "Choose what you need help in"
            display_text(choose_help_msg, 32, CHOOSE_HELP_TEXT_Y)

            # display buttons on screen
            for button in seek_help_button_lst:
                button.draw(screen)

        elif(screen_mode == "helper_screen"):
            go_back_button.draw(screen)

            display_text(name, 30, 5, 5)
            display_text(city, 30, 30, 5)

        # Update display - without input update everything
        pygame.display.update()

        # Set the clock tick to be 60 times per second. 60 frames for second.
        clock.tick(60)
    pygame.quit()
    quit()


main()