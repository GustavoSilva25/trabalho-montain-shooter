#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        self.direction = 1

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self):

        if self.name != "Enemy3":
            self.rect.centerx -= ENTITY_SPEED[self.name]
            
        else:
            # implementando o movimento zig zag do enemy3
            self.rect.centerx -= ENTITY_SPEED[self.name]
            self.rect.centery += self.direction * 2
            if self.rect.top <= 0 or self.rect.bottom >= 324:
                self.direction *= - 1