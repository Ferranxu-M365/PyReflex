import reflex as rx

from ...layout.layout_state import LayoutState

def footer() -> rx.Component:
  return rx.cond(LayoutState.current_page == "/",
    rx.box(
      rx.link(
        rx.image(
          src="/github_icon_white.png",
          class_name=rx.cond(LayoutState.github_visible, "githubCatvisible", "githubCatHidden"),
          id="githubCat",
        ),
        href="https://github.com/Ferranxu-M365/PyReflex",
        is_external=True,
        rel="noreferrer noopener",
      ),
      rx.box(
        rx.text("Catch Me!"),
        display=rx.cond(LayoutState.catchme_btn_hide, "none", "block"),
        id="githubTextBtn",
      ),
      on_click=LayoutState.github_btn_handler,
      animation_play_state=rx.cond(LayoutState.catchme_btn_hide, "paused", "running"),
      id="bottomMovingLine",
    ),
  )