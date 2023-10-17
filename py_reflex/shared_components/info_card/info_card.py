import reflex as rx

from .info_card_style import *

def info_card(children: rx.Component, text_color: str, bg_color: str):
  return rx.box(
    children,
    color=text_color,
    background_color=bg_color,
    style= info_card_style,
  )