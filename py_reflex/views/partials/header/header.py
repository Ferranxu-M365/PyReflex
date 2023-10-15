import reflex as rx

from .header_style import *

from .header_state import HeaderState

def header() -> rx.Component:
  return rx.flex(
    rx.box(style=header_item_style),
    rx.flex(
      rx.link(
        "Home",
        href="/",
        style=navbar_item_style,
        text_decoration=rx.cond(HeaderState.current_page == "/", "underline", "none") # active page
      ),
      rx.link(
        "Play with the API",
        href="#",
        style=navbar_item_style,
        text_decoration=rx.cond(HeaderState.current_page == "/theApi", "underline", "none") # active page
      ),
      rx.link(
        "About",
        href="/about",
        style=navbar_item_style,
        text_decoration=rx.cond(HeaderState.current_page == "/about", "underline", "none") # active page
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
      rx.tooltip(
        rx.link(
          rx.image(
            src="/github_icon_white.png",
            style=github_btn_style,
          ),
          href=rx.cond(HeaderState.github_header_btn_disabled, "#", "https://github.com/Ferranxu-M365/PyReflex"),
          is_external=rx.cond(HeaderState.github_header_btn_disabled, False, True),
          rel="noreferrer noopener",
          opacity=rx.cond(HeaderState.github_header_btn_disabled, "0.3", "1"),
          cursor=rx.cond(HeaderState.github_header_btn_disabled, "default", "pointer"),
        ),
        label=rx.cond(HeaderState.github_header_btn_disabled, "Catch me on the Home page!", "Here is my code"),
        margin_right="10px",
      ),
      style=[header_item_style, contact_section_style],
    ),
    style=header_style,
  )