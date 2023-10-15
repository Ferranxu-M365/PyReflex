import reflex as rx

from ..layout.layout import layout

from ...app_state import AppState

class IndexState(AppState):
  pass

def index() -> rx.Component:
  return layout(
    rx.fragment(
      "index"
    )
  )