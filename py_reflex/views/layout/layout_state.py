import reflex as rx

from ...app_state import AppState

# Layout's duty is to control the state of the Header and the Footer
class LayoutState(AppState):
  # Header
  github_header_btn_disabled: bool = True
  sidebar_menu_visible: bool = False

  # Footer
  github_visible: bool = False

  def github_btn_handler(self):
    self.set_github_header_btn_disabled(False)
    self.set_github_visible(True)

  @rx.var
  def catchme_btn_hide(self) -> bool:
    if self.github_visible:
      return True
    return False