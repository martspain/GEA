import pygame

class SpriteSheet():
  def __init__(self, image):
    self.sheet = image

  def get_image(self, frame, width, height, scale=1, transColor=(0,0,0)):
    image = pygame.Surface((width, height)).convert_alpha()
    image.blit(self.sheet, (0,0), (frame * width, 0, width, height))
    image = pygame.transform.scale(image, (width * scale, height * scale))
    image.set_colorkey(transColor)
    return image

  def get_masked_image(self, frame, width, height, scale=1, transColor=(0,0,0), maskColor=(255,255,255)):
    image = pygame.Surface((width, height)).convert_alpha()
    image.fill(maskColor)
    image.blit(self.sheet, (0,0), (frame * width, 0, width, height), special_flags=pygame.BLEND_RGBA_MULT)
    image = pygame.transform.scale(image, (width * scale, height * scale))
    image.set_colorkey(transColor)
    return image
