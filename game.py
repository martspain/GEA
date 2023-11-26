import pygame
from spritesheet import SpriteSheet

class Game:
  def __init__(self, name="New Game", width=800, height=600, bg_color=(50,50,50)):
    self.name = name
    self.width = width
    self.height = height
    self.bg_color = bg_color

    self.runningGame = False
    self.mainCharacterSpritesheet = None

  def load_main_character_spritesheet(self, path: str):
    spriteSheet = pygame.image.load(path).convert_alpha()
    return spriteSheet

  def run(self):
    pygame.init()

    screen = pygame.display.set_mode((self.width, self.height))
    pygame.display.set_caption(self.name)

    self.mainCharacterSpritesheet = self.load_main_character_spritesheet("assets/sprites/main_character/MarkFront.png")
    sprite_sheet = SpriteSheet(self.mainCharacterSpritesheet)
    frame_0 = sprite_sheet.get_image(0, 8, 8, 10)
    frame_1 = sprite_sheet.get_masked_image(0, 8, 8, 10, maskColor=(0,0,255))
    frame_2 = sprite_sheet.get_image(2, 8, 8, 5)

    self.runningGame = True

    while self.runningGame:
      # Clear screen
      screen.fill(self.bg_color)

      screen.blit(frame_0, (0, 0))
      screen.blit(frame_1, (100,0))
      # screen.blit(frame_2, (200,0))
      
      # Handle Events
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.runningGame = False
      
      pygame.display.update()


    pygame.quit()


spriteGame = Game("Sprite")
spriteGame.run()