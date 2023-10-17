import reflex as rx

from .layout_style import *

from ..partials.header.header import header
from ..partials.footer.footer import footer

def layout(children: rx.Component) -> rx.Component:
  return rx.grid(
    rx.grid_item(
      header(),
      row_start=1,
      col_span=3,
    ),
    rx.grid_item(
      children,
      row_start=2,
      grid_column=2,
      style=main_content_style,
    ),
    rx.grid_item(
      footer(),
      row_start=3,
      col_span=3,
    ),
    template_rows="10% 86% 4%",
    grid_template_columns=["0% 100% 0%", "10% 80% 10%", "20% 60% 20%", "30% 40% 30%", "30% 40% 30%"],
    style=layout_style,
  )