import pygame

class SpriteSheet():
  def __init__(self, image):
    self.sheet = image
    self.frames = []

  def get_all_frames(self, rows, cols, width, height, scale=1, transColor=(0,0,0)):
    frame_collection = []
    for r in range(rows):
      for c in range(cols):
        frame_collection.append(self.get_image(c, width, height, scale, transColor, r))
    self.frames = frame_collection
    return frame_collection
  
  def get_action_frames(self, indexes:list[int]):
    frame_collection = []
    for ind in indexes:
      if ind < len(self.frames):
        frame_collection.append(self.frames[ind])
    return frame_collection

  def get_image(self, frame, width, height, scale=1, transColor=(0,0,0), row=0):
    image = pygame.Surface((width, height)).convert_alpha()
    image.blit(self.sheet, (0,0), (frame * width, row * height, width, height))
    image = pygame.transform.scale(image, (width * scale, height * scale))
    image.set_colorkey(transColor)
    return image

  def get_masked_image(self, frame, width, height, scale=1, transColor=(0,0,0), maskColor=(255,255,255), row=0):
    image = pygame.Surface((width, height)).convert_alpha()
    image.fill(maskColor)
    image.blit(self.sheet, (0,0), (frame * width, row * height, width, height), special_flags=pygame.BLEND_RGBA_MULT)
    image = pygame.transform.scale(image, (width * scale, height * scale))
    image.set_colorkey(transColor)
    return image
