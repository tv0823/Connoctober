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

    screen_mode = "log_in_screen"

    running = True
    while running:
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if(mouse_in_button(seeker_button, pos) and screen_mode == "log_in_screen"):
                    seeker = Seeker("Beer-Sheva")
                    seekers_lst.append(seeker)
                    screen_mode = "seeker_screen"
                elif(mouse_in_button(helper_button, pos) and screen_mode == "log_in_screen"):
                    helper = Helper()
                    helpers_lst.append(helper)
                    screen_mode = "helper_screen"
                elif(mouse_in_button(go_back_button, pos) and screen_mode != "log_in_screen"):
                    screen_mode = "log_in_screen"


        # Display background and buttons
        screen.fill(BLACK)
        screen.blit(background, (0, 0))

        if(screen_mode == "log_in_screen"):
            seeker_button.draw(screen)
            helper_button.draw(screen)
        elif(screen_mode == "seeker_screen"):
            go_back_button.draw(screen)

            # display text on screen
            choose_help_msg = "Choose what you need help in"
            font = pygame.font.SysFont(None, 32)
            text = font.render(choose_help_msg, True, WHITE)
            screen.blit(text, (CHOOSE_HELP_TEXT_X, CHOOSE_HELP_TEXT_Y))

            for button in seek_help_button_lst:
                button.draw(screen)

        elif(screen_mode == "helper_screen"):
            go_back_button.draw(screen)


        # Update display - without input update everything
        pygame.display.update()

        # Set the clock tick to be 60 times per second. 60 frames for second.
        clock.tick(60)
    pygame.quit()
    quit()

main()