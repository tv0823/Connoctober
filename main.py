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

    running = True
    while running:
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if(mouse_in_button(seeker_button, pos)):
                    print("click")
                    seeker = Seeker("Beer-Sheva")
                    seekers_lst.append(seeker)
                elif(mouse_in_button(helper_button, pos)):
                    print("BOOM")
                    helper = Helper()
                    helpers_lst.append(helper)

        # Display background and buttons
        screen.fill(BLACK)
        screen.blit(background, (0, 0))

        seeker_button.draw(screen)
        helper_button.draw(screen)


        # Update display - without input update everything
        pygame.display.update()

        # Set the clock tick to be 60 times per second. 60 frames for second.
        clock.tick(60)
    pygame.quit()
    quit()

main()