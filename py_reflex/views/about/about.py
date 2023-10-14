import reflex as rx

from ...app_state import AppState

class AboutState(AppState):
  pass

def about() -> rx.Component:
  return rx.text("about")