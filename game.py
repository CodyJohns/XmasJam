import pygame


class Entity:
    def __init__(self):
        self.x = 10
        self.y = 10
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.vel = 10
        self.alive = True

    def update(self):
        if self.alive:
            self.checkMovement()

    def checkMovement(self):
        if self.up:
            self.y = self.y - self.vel
        if self.down:
            self.y = self.y + self.vel
        if self.left:
            self.x = self.x - self.vel
        if self.right:
            self.x = self.x + self.vel


# define a main function
def main():
    pygame.init()
    # load and set the logo
    #logo = pygame.image.load("logo32x32.png")
    #pygame.display.set_icon(logo)
    pygame.display.set_caption("XmasJam")
     
    screen = pygame.display.set_mode((1280,720), pygame.SCALED | pygame.DOUBLEBUF, vsync=1)
     
    running = True

    block = Entity()

    entities = [block]
     
    # main loop
    while running:
        pygame.draw.rect(screen, (0, 0, 0), (0, 0, 1280, 720))

        for entity in entities:
            entity.update()
            if entity.alive:
                pygame.draw.rect(screen, (255, 0, 0), (entity.x, entity.y, 100, 100))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_a:
                    block.left = True
                if event.key == pygame.K_d:
                    block.right = True
                if event.key == pygame.K_w:
                    block.up = True
                if event.key == pygame.K_s:
                    block.down = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    block.left = False
                if event.key == pygame.K_d:
                    block.right = False
                if event.key == pygame.K_w:
                    block.up = False
                if event.key == pygame.K_s:
                    block.down = False

if __name__=="__main__":
    main()