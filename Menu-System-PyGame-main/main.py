import pygame
import os
import sys
import importlib.util
from button import Button
import cv2

# Update the path and file name
simulation_path = r"C:\Users\Lopez Santos\Basic-Traffic-Intersection-Simulationn"
simulation_file = "versiondraft.py"
simulation_module_name = "versiondraft"

# Construct the full path to the simulation file
simulation_full_path = os.path.join(simulation_path, simulation_file)

# Add the directory to the system path if not already added
if simulation_path not in sys.path:
    sys.path.append(simulation_path)

# Use importlib to dynamically import the module
spec = importlib.util.spec_from_file_location(simulation_module_name, simulation_full_path)
simulation_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(simulation_module)
Main = simulation_module.Main  # Access the Main class from the dynamically imported module

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 1080, 1080
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Menu")

# Initialize the video capture
video_path = r"C:\Users\Lopez Santos\Basic-Traffic-Intersection-Simulationn\INTERSECTION_bg.mp4"
cap = cv2.VideoCapture(video_path)

def get_font(size):
    return pygame.font.Font("Menu-System-PyGame-main/assets/font.ttf", size)

def play():
    main_simulation = Main()

    while True:
        main_simulation.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if main_simulation.quit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        SCREEN.fill("black")
        main_simulation.draw(SCREEN)

        pygame.display.update()
def CREDITS():
    while True:
        CREDITS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        # Render video frame
        ret, frame = cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = pygame.image.frombuffer(frame.tostring(), frame.shape[1::-1], "RGB")
            SCREEN.blit(frame, (0, 0))

        # Render "TRAFFIC SIM" text
        MENU_TEXT_SHADOW = get_font(70).render("GROUP 2 & 6", True, "#000000")
        MENU_TEXT = get_font(70).render("GROUP 2 & 6", True, "#FFFFFF")
        MENU_SHADOW_RECT = MENU_TEXT_SHADOW.get_rect(center=(530 + 3, 100 + 3))
        MENU_RECT = MENU_TEXT.get_rect(center=(530, 100))
        SCREEN.blit(MENU_TEXT_SHADOW, MENU_SHADOW_RECT)
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        # Render "BACK" button
        CREDITS_BUTTON = Button(image=pygame.image.load("Menu-System-PyGame-main/assets/Back Rect.png"), pos=(800, 800), 
                             text_input="BACK", font=get_font(35), base_color="GREEN", hovering_color="BLACK")
        CREDITS_BUTTON.changeColor(CREDITS_MOUSE_POS)
        CREDITS_BUTTON.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CREDITS_BUTTON.checkForInput(CREDITS_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def main_menu():
    while True:
        # Read the video frame
        ret, frame = cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = pygame.image.frombuffer(frame.tostring(), frame.shape[1::-1], "RGB")
            SCREEN.blit(frame, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT_SHADOW = get_font(70).render("TRAFFIC SIM", True, "#000000")
        MENU_TEXT = get_font(70).render("TRAFFIC SIM", True, "#FFAA00")
        MENU_SHADOW_RECT = MENU_TEXT_SHADOW.get_rect(center=(530 + 3, 100 + 3))
        MENU_RECT = MENU_TEXT.get_rect(center=(530, 100))
        SCREEN.blit(MENU_TEXT_SHADOW, MENU_SHADOW_RECT)
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        PLAY_BUTTON = Button(image=pygame.image.load("Menu-System-PyGame-main/assets/Play Rect.png"), pos=(530, 350), 
                             text_input="START SIM", font=get_font(40), base_color="Green", hovering_color="White")
        PLAY_BUTTON_SHADOW = get_font(40).render("START SIM", True, "#000000")
        PLAY_BUTTON_RECT = PLAY_BUTTON_SHADOW.get_rect(center=(530 + 3, 350 + 3))
        SCREEN.blit(PLAY_BUTTON_SHADOW, PLAY_BUTTON_RECT)

        CREDITS_BUTTON = Button(image=None, pos=(800, 800), 
                             text_input="CREDITS", font=get_font(40), base_color="Blue", hovering_color="White")
        CREDITS_BUTTON_SHADOW = get_font(40).render("CREDITS", True, "#000000")
        CREDITS_BUTTON_RECT = CREDITS_BUTTON_SHADOW.get_rect(center=(800 + 3, 800 + 3))
        SCREEN.blit(CREDITS_BUTTON_SHADOW, CREDITS_BUTTON_RECT)

        QUIT_BUTTON = Button(image=pygame.image.load("Menu-System-PyGame-main/assets/Quit Rect.png"), pos=(530, 470), 
                             text_input="QUIT", font=get_font(35), base_color="Red", hovering_color="White")

        for button in [PLAY_BUTTON, CREDITS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if CREDITS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    CREDITS()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

# Start the main menu
main_menu()
