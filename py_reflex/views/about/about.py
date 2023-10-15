import reflex as rx

from ..layout.layout import layout

from ...app_state import AppState

class AboutState(AppState):
  pass

def about() -> rx.Component:
  return layout(
    rx.fragment(
      "about"
    )
  )