import time
import cv2
import numpy as np

from src.char.Healer import Healer, Priority
from ok import color_range_to_bound


class Verina(Healer):
    def count_liberation_priority(self):
        return 2

    def do_perform(self):
        if self.has_intro:
            self.wait_down(click=False)
        else:
            self.continues_normal_attack(1.1)
        liberated = False
        if self.liberation_available():
            liberated = self.click_liberation()
        if self.resonance_available():
            self.click_resonance(send_click=False,post_sleep=0.35)
        if self.echo_available():
            self.click_echo()
        if self.is_mouse_forte_full():
            self.task.jump(after_sleep=0.1)
            self.continues_normal_attack(1.1)
        elif not liberated:
            self.click_liberation(wait_if_cd_ready=1)
        return self.switch_next_char()
