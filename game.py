import pygame
from spritesheet import SpriteSheet

class Game:
  def __init__(self, name="New Game", width=800, height=600, bg_color=(50,50,50)):
    self.name = name
    self.width = width
    self.height = height
    self.bg_color = bg_color
    self.currentState = "idle"
    self.playerPosition = (50, 500)
    self.playerVelocity = 0.5
    self.playerWidth = 8
    self.playerHeight = 8
    self.playerScale = 5
    self.currentMovement = []

    self.runningGame = False
    self.mainCharacterSpritesheet = None

  def load_spritesheet(self, path: str):
    spriteSheet = pygame.image.load(path).convert_alpha()
    return spriteSheet

  def update_player_position(self):
    if self.currentMovement.count("left") > 0:
      if self.playerPosition[0] - self.playerVelocity >= 0:
        self.playerPosition = (self.playerPosition[0] - self.playerVelocity, self.playerPosition[1])
    if self.currentMovement.count("right") > 0:
      if self.playerPosition[0] + self.playerVelocity + self.playerWidth <= self.width - self.playerWidth * 3:
        self.playerPosition = (self.playerPosition[0] + self.playerVelocity, self.playerPosition[1])
    if self.currentMovement.count("down") > 0:
      if self.playerPosition[1] + self.playerVelocity + self.playerHeight <= self.height - self.playerHeight * 4:
        self.playerPosition = (self.playerPosition[0], self.playerPosition[1] + self.playerVelocity)
    if self.currentMovement.count("up") > 0:
      if self.playerPosition[1] - self.playerVelocity >= 0:
        self.playerPosition = (self.playerPosition[0], self.playerPosition[1] - self.playerVelocity)


  def run(self):
    pygame.init()

    screen = pygame.display.set_mode((self.width, self.height))
    pygame.display.set_caption(self.name)

    # Background Sprites
    bgSpriteSheet = self.load_spritesheet("assets/sprites/background/Background.png")
    bg_sprite_sheet = SpriteSheet(bgSpriteSheet)
    bg_sprite_sheet.get_all_frames(8, 1, 80, 60, 10)

    bg_animation = bg_sprite_sheet.get_action_frames([0,1,2,3,4,5,6,7,8])

    # Character Sprites
    self.mainCharacterSpritesheet = self.load_spritesheet("assets/sprites/main_character/MarkFront.png")
    sprite_sheet = SpriteSheet(self.mainCharacterSpritesheet)
    sprite_sheet.get_all_frames(4, 8, self.playerWidth, self.playerHeight, self.playerScale)

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

    # Animation timer
    # self.currentState = "right"
    animation_cooldown = 250 # ms
    last_update = pygame.time.get_ticks()
    currentFrame = 0
    bg_currentFrame = 0

    self.runningGame = True

    while self.runningGame:
      # Clear screen
      screen.fill(self.bg_color)

      # Update animations frame
      currentTime = pygame.time.get_ticks()

      self.update_player_position()

      if currentTime - last_update >= animation_cooldown:
        if bg_currentFrame < len(bg_animation)-1:
          bg_currentFrame += 1
        else:
          bg_currentFrame = 0
        if currentFrame < len(animations[self.currentState])-1:
          currentFrame += 1
        else:
          currentFrame = 0
        last_update = currentTime

      screen.blit(bg_animation[bg_currentFrame], (0, 0))
      screen.blit(animations[self.currentState][currentFrame], self.playerPosition)
      
      # Handle Events
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.runningGame = False
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_LEFT or event.key == pygame.K_a:
            if self.currentMovement.count("right") == 0:
              self.currentState = "left"
            self.currentMovement.append("left")
          if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            if self.currentMovement.count("left") == 0:
              self.currentState = "right"
            self.currentMovement.append("right")
          if event.key == pygame.K_DOWN or event.key == pygame.K_s:
            if self.currentMovement.count("up") == 0:
              self.currentState = "down"
            self.currentMovement.append("down")
          if event.key == pygame.K_UP or event.key == pygame.K_w:
            if self.currentMovement.count("down") == 0:
              self.currentState = "up"
            self.currentMovement.append("up")
          currentFrame = 0
        if event.type == pygame.KEYUP:
          if event.key == pygame.K_LEFT or event.key == pygame.K_a:
            if len(self.currentMovement) == 1:
              self.currentState = "idleLeft"
            self.currentMovement.remove("left")
          if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            if len(self.currentMovement) == 1:
              self.currentState = "idleRight"
            self.currentMovement.remove("right")
          if event.key == pygame.K_DOWN or event.key == pygame.K_s:
            if len(self.currentMovement) == 1:
              self.currentState = "idle"
            self.currentMovement.remove("down")
          if event.key == pygame.K_UP or event.key == pygame.K_w:
            if len(self.currentMovement) == 1:
              self.currentState = "idleUp"
            self.currentMovement.remove("up")
          currentFrame = 0
      
      pygame.display.update()


    pygame.quit()


spriteGame = Game("Sprite")
spriteGame.run()