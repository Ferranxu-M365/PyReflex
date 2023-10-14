import reflex as rx

def layout(children: rx.Component) -> rx.Component:
  return rx.grid(
    rx.grid_item(
      row_start=1,
      col_span=3,
    ),
    rx.grid_item(
      children,
      row_start=2,
      col_start=2,
      border= "1px solid white",
      border_radius= "5px",
      box_shadow= "white 1px 1px 10px 1px",
      padding= "10px",
      background_color= "#150015",
    ),
    rx.grid_item(
      row_start=3,
      col_span=3,
    ),
    template_rows="8% 84% 8%",
    template_columns="30% 40% 30%",
    height="100vh",
    overflow="hidden",
  )