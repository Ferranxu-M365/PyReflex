import reflex as rx

from .footer_state import FooterState

def footer() -> rx.Component:
  return rx.cond(FooterState.current_page == "/",
    rx.box(
      rx.link(
        rx.image(
          src="/github_icon_white.png",
          class_name=rx.cond(FooterState.github_visible, "githubCatvisible", "githubCatHidden"),
          id="githubCat",
        ),
        href="https://github.com/Ferranxu-M365/PyReflex",
        is_external=True,
        rel="noreferrer noopener",
      ),
      rx.box(
        rx.text("Catch Me!"),
        display=rx.cond(FooterState.catchme_btn_hide, "none", "block"),
        id="githubTextBtn",
      ),
      on_click=FooterState.github_btn_handler,
      animation_play_state=rx.cond(FooterState.catchme_btn_hide, "paused", "running"),
      id="bottomMovingLine",
    ),
  )