import reflex as rx

from .sidebar_style import *

def sidebar(children: rx.Component, position, is_open: bool, on_close):
    VALID_POSITIONS = ("left", "right")
    if position not in VALID_POSITIONS:
        raise ValueError(f"results: position must be one of {VALID_POSITIONS}.")
    
    return rx.cond(is_open, rx.box(
        rx.vstack(
            rx.button(
                rx.icon(tag="close"),
                on_click=on_close,
                style=close_btn,
            ),
            children,
            style=sidebar_container,
        ),
        animation_name=rx.cond(position == "left", "slidelefttoright", "sliderighttoleft"),
        animation_fill_mode=rx.cond(position == "left", "default", "forwards"),
        style=sidebar_style,
    ))