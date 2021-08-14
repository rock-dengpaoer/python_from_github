import sys

import pygame

from settings import Settings
from ship import Ship
from alien import Alien

import game_functions as gf

from pygame.sprite import Group

from game_stats import GameStats

from scoreboard import Scoreboard

from button import Button


def run_game():
    pygame.init()
    # screen = pygame.display.set_mode((1200, 800))

    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )

    pygame.display.set_caption("Alien Invasion")

    play_button = Button(ai_settings, screen, "play")

    stats = GameStats(ai_settings)

    sb = Scoreboard(ai_settings, screen, stats)

    ship = Ship(screen, ai_settings)

    bullets = Group()

    aliens = Group()

    # bg_color = (230, 230, 230)

    # alien = Alien(ai_settings, screen)

    gf.create_fleet(ai_settings, screen, ship, aliens)

    while True:

        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         sys.exit()
        gf.check_events(ai_settings, screen, ship, bullets, stats, play_button, aliens, sb)

        if stats.game_active:
            ship.update()

            gf.update_bullets(ai_settings, screen, ship, aliens, bullets, stats, sb)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets, sb)

        # bullets.update()
        #
        # for bullet in bullets.copy():
        #     if bullet.rect.bottom <= 0:
        #         bullets.remove(bullet)
        # print(len(bullets))

        # screen.fill(bg_color)

        # screen.fill(ai_settings.bg_color)
        # ship.blitme()
        #
        # pygame.display.flip()

        gf.update_screen(ai_settings, screen, ship, aliens, bullets, play_button, stats, sb)


run_game()
