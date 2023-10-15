import reflex as rx

from .header_style import *

from ...app_state import AppState

def header() -> rx.Component:
  return rx.flex(
    rx.box(style=header_item_style),
    rx.flex(
      rx.link(
        "Home",
        href="/",
        style=navbar_item_style,
        text_decoration=rx.cond(AppState.current_page == "/", "underline", "none") # active page
      ),
      rx.link(
        "Play with the API",
        href="#",
        style=navbar_item_style,
        text_decoration=rx.cond(AppState.current_page == "/theApi", "underline", "none") # active page
      ),
      rx.link(
        "About",
        href="/about",
        style=navbar_item_style,
        text_decoration=rx.cond(AppState.current_page == "/about", "underline", "none") # active page
      ),
      style=[header_item_style, navbar_style],
    ),
    rx.flex(
      rx.link(
        rx.text(
          "Contact me",
          style=linkedin_text
        ),
        rx.image(
          src="/linkedin_icon.png",
          style=linkedin_img,
        ),
        href="https://es.linkedin.com/in/ferran-ortega-torrabadell-271313133",
        is_external=True,
        rel="noreferrer noopener",
        style=linkedin_btn,
      ),
      style=[header_item_style, contact_section_style]
    ),
    style=header_style,
  )