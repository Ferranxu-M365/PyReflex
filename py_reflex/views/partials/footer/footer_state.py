import reflex as rx

from ...layout.layout_state import LayoutState

class FooterState(LayoutState):
  github_visible: str = False

  def github_btn_handler(self):
    self.set_github_header_btn_disabled(False)
    self.set_github_visible(True)

  @rx.var
  def catchme_btn_hide(self) -> bool:
    if self.github_visible:
      return True
    return False