import pygame
from spritesheet import SpriteSheet

class Game:
  def __init__(self, name="New Game", width=800, height=600, bg_color=(50,50,50)):
    self.name = name
    self.width = width
    self.height = height
    self.bg_color = bg_color
    self.currentState = "idle"

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
    sprite_sheet.get_all_frames(4, 8, 8, 8, 15)

    # Animation List
    animations = {
      "idle": sprite_sheet.get_action_frames([0,6,7]),
      "idleUp": sprite_sheet.get_action_frames([8,15]),
      "idleLeft": sprite_sheet.get_action_frames([16, 23]),
      "idleRight": sprite_sheet.get_action_frames([24, 31]),
      "down": sprite_sheet.get_action_frames([1,2,3,4]),
      "up": sprite_sheet.get_action_frames([9,10,11,12,13,14]),
      "left": sprite_sheet.get_action_frames([16,17,18,19,20,21]),
      "right": sprite_sheet.get_action_frames([24,25,26,27,28,29])
    }

    # self.currentState = "right"
    animation_cooldown = 250 # ms
    last_update = pygame.time.get_ticks()
    currentFrame = 0

    self.runningGame = True

    while self.runningGame:
      # Clear screen
      screen.fill(self.bg_color)

      # Update animations frame
      currentTime = pygame.time.get_ticks()

      if currentTime - last_update >= animation_cooldown:
        if currentFrame < len(animations[self.currentState])-1:
          currentFrame += 1
        else:
          currentFrame = 0
        last_update = currentTime

      screen.blit(animations[self.currentState][currentFrame], (100, 100))
      
      # Handle Events
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.runningGame = False
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_LEFT:
            self.currentState = "left"
          if event.key == pygame.K_RIGHT:
            self.currentState = "right"
          if event.key == pygame.K_DOWN:
            self.currentState = "down"
          if event.key == pygame.K_UP:
            self.currentState = "up"
          currentFrame = 0
        if event.type == pygame.KEYUP:
          if event.key == pygame.K_LEFT:
            self.currentState = "idleLeft"
          if event.key == pygame.K_RIGHT:
            self.currentState = "idleRight"
          if event.key == pygame.K_DOWN:
            self.currentState = "idle"
          if event.key == pygame.K_UP:
            self.currentState = "idleUp"
          currentFrame = 0
      
      pygame.display.update()


    pygame.quit()


spriteGame = Game("Sprite")
spriteGame.run()