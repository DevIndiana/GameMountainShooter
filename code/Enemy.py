#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.EnemyShot import EnemyShot
from code.Entity import Entity
from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY, WIN_HEIGHT


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self):
        # Movimento horizontal (da direita para a esquerda)
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay <= 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))


class Enemy3(Enemy):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.vertical_velocity = ENTITY_SPEED[self.name]  # Velocidade vertical normal
        self.moving_up = True  # Começa movendo para cima

    def move(self):
        # Movimento horizontal (da direita para a esquerda)
        self.rect.centerx -= ENTITY_SPEED[self.name]

        # Movimento vertical
        if self.moving_up:
            self.rect.centery -= self.vertical_velocity
            # Verifica se atingiu a borda superior
            if self.rect.top <= 0:  # Borda superior
                self.moving_up = False  # Começa a descer
        else:
            self.rect.centery += self.vertical_velocity * 2  # Desce com o dobro da velocidade
            # Verifica se atingiu a borda inferior
            if self.rect.bottom >= WIN_HEIGHT:  # Borda inferior
                self.moving_up = True  # Começa a subir