import reflex as rx

from .header_style import *
from ....shared_components.sidebar.sidebar import sidebar

from ...layout.layout_state import LayoutState

def header() -> rx.Component:
  return rx.flex(
    rx.desktop_only(style=header_item_style),
    rx.box(
      rx.link(
        "Home",
        href="/",
        style=navbar_item_style,
        color=rx.cond(LayoutState.current_page == "/", "rgb(255,255,50)", "none"), # active page
      ),
      rx.tooltip(
        rx.link(
          "Play with the API",
          href="#",
          style=navbar_disabled_item_style,
          #color=rx.cond(LayoutState.current_page == "/theApi", "rgb(255,255,50)", "none"), # active page
        ),
        label="Coming soon!",
      ),
      rx.link(
      "About",
      href="/about",
      style=navbar_item_style,
      color=rx.cond(LayoutState.current_page == "/about", "rgb(255,255,50)", "none"), # active page
    ),
      style=[header_item_style, navbar_style],
    ),
    rx.mobile_and_tablet(
      rx.button(
        rx.icon(tag="hamburger"),
        on_click=LayoutState.set_sidebar_menu_visible(~LayoutState.sidebar_menu_visible),
        style=menu_hamburger_btn,
      ),
      style=header_item_style,
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
          href=rx.cond(LayoutState.github_header_btn_disabled, "#", "https://github.com/Ferranxu-M365/PyReflex"),
          is_external=rx.cond(LayoutState.github_header_btn_disabled, False, True),
          rel="noreferrer noopener",
          opacity=rx.cond(LayoutState.github_header_btn_disabled, "0.3", "1"),
          cursor=rx.cond(LayoutState.github_header_btn_disabled, "default", "pointer"),
        ),
        label=rx.cond(LayoutState.github_header_btn_disabled, "Catch me on the Home page!", "Here is my code"),
        margin_right="10px",
      ),
      style=[header_item_style, contact_section_style],
    ),
    sidebar(
      rx.box(
        rx.heading(
          "Made with",
          rx.tooltip(
              rx.image(
                  src="/favicon.ico",
                  margin_left="5px",
                  display="inline",
              ),
              label="REFLEX",
          ),
          size="md",
          style=small_navbar_heading,
        ),
        rx.box(
          rx.link(
            "Home",
            href="/",
            style=navbar_item_style,
            color=rx.cond(LayoutState.current_page == "/", "rgb(255,255,50)", "none"), # active page
            on_click=LayoutState.set_sidebar_menu_visible(False),
          ),
          rx.link(
            "Play with the API",
            href="#",
            style=navbar_item_style,
            color=rx.cond(LayoutState.current_page == "/theApi", "rgb(255,255,50)", "none"), # active page
            on_click=LayoutState.set_sidebar_menu_visible(False),
          ),
          rx.link(
            "About",
            href="/about",
            style=navbar_item_style,
            color=rx.cond(LayoutState.current_page == "/about", "rgb(255,255,50)", "none"), # active page
            on_click=LayoutState.set_sidebar_menu_visible(False),
          ),
          style=small_navbar_style,
        ),
      ),
      "left",
      LayoutState.sidebar_menu_visible,
      LayoutState.set_sidebar_menu_visible(False),
    ),
    style=header_style,
  )