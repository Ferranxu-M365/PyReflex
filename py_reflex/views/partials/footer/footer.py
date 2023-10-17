import reflex as rx

from .footer_style import *

from ...layout.layout_state import LayoutState

def footer() -> rx.Component:
  return rx.cond(LayoutState.current_page == "/",
    rx.box(
      rx.link(
        rx.image(
          src="/github_icon_white.png",
          transform=rx.cond(LayoutState.github_visible, "translateY(-120%)", "translateY(0%)"),
          style=github_cat_btn_style,
        ),
        href="https://github.com/Ferranxu-M365/PyReflex",
        is_external=True,
        rel="noreferrer noopener",
      ),
      rx.box(
        rx.text("Catch Me!"),
        display=rx.cond(LayoutState.catchme_btn_hide, "none", "block"),
        style=github_text_btn,
      ),
      on_click=LayoutState.github_btn_handler,
      animation_play_state=rx.cond(LayoutState.catchme_btn_hide, "paused", "running"),
      style=bottom_moving_line,
    ),
  )