from pygame_utils import PygameButton
import pong_ai as pong
import pygame
import sys
import os

if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config.txt")

    config = pong.neat.Config(pong.neat.DefaultGenome, pong.neat.DefaultReproduction,
                         pong.neat.DefaultSpeciesSet, pong.neat.DefaultStagnation,
                         config_path)
    
    # Initialize Pygame
    pygame.init()

    clock=pygame.time.Clock()

    # Create a Pygame window
    window_size = (700, 500)
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption('Pong AI')

    # Create a font object
    font = pygame.font.Font(None, 24)

    train_ai_button = PygameButton(700 / 6, 500 / 2, 150, 50, "Train AI")
    play_ai_button = PygameButton(4 * 700 / 6, 500 / 2, 150, 50, "Play AI")

    # Start the main loop
    while True:
        # Set the frame rate
        clock.tick(60)

        # Fill the display with color
        screen.fill((155, 255, 155))

        # Get events from the event queue
        for event in pygame.event.get():
            # Check for the quit event
            if event.type == pygame.QUIT:
                # Quit the game
                pygame.quit()
                sys.exit()

        # Check for the mouse button down event
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Call the on_mouse_button_down() function
            if train_ai_button.button_rect.collidepoint(event.pos):
                print("Training AI...")
                pong.run_neat(config)
            elif play_ai_button.button_rect.collidepoint(event.pos):
                print("Playing AI...")
                pong.test_ai(config)

        train_ai_button.draw(screen)
        play_ai_button.draw(screen)

        # Update the game state
        pygame.display.update()