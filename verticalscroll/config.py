#!/usr/bin/env python3

class Config:

    screen_size = (640,480)
    game_title = "Vertical Scroll"

    scroll_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    font_sprites_filename = ["verticalscroll", "assets", "images", "042_32.png"]
    font_fps_size = 24

    animation_speed = 0.2

    fps = 60
    time_per_frame = 1000.0 / fps
    refresh_time = 1000.0

    background_color = (0,0,0)
    fps_foreground_color = (255,255,255)
    fps_background_color = (0,0,0)

    def __init__(self):
        pass