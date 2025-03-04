from circleshape import CircleShape
from shot import Shot
from constants import *

import pygame

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.__shootcooldown = 0

        # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        points = self.triangle()
        pygame.draw.polygon(screen, "white", points, 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        new_position = self.position + forward * PLAYER_SPEED * dt

        if self.in_frame_limits(new_position):
            self.position = new_position

    def shoot(self):

        if self.__shootcooldown <= 0:
            shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            self.__shootcooldown = PLAYER_SHOOT_COOLDOWN

    def in_frame_limits(self, move_position):
        if move_position[0] > 0 and move_position[0] < SCREEN_WIDTH and move_position[1] > 0 and move_position[1] < SCREEN_HEIGHT:
            return True
        return False 

    def update(self, dt):
        self.__shootcooldown -= dt
        
        keys = pygame.key.get_pressed()
        
        print(self.position, self.rotation)

        if keys[pygame.K_s]:
            self.move(dt * -1)

        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_a]:
            self.rotate(dt * -1)
        
        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_SPACE]:
            self.shoot()