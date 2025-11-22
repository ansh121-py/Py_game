import pyame, sys

pygame.init()
Display = pygame.display.set_mode((400, 300))
pygane.display.set_caption("Hello World!")
while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  pygame.display.update()
