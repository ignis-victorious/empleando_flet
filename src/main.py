#  _________________
#  Import LIBRARIES
import flet as ft
from flet import Page, app, Slider, Switch, Text, ElevatedButton
#  Import FILES
#  _________________


def main(page: Page) -> None:  # función principal de la ventana
    page.title = "Terzero ejercicio - Slider y Switch"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    slider: Slider = Slider(min=0, max=100, divisions=10, label="(value)")
    switch: Switch = Switch(label="Activar opción")
    salida: Text = Text(value="")

    def mostrar_click(e: ft.ControlEvent) -> None:
        estado: str = "activado" if switch.value else "desactivado"
        salida.value = f"Valor del slider: {slider.value}, Opción está {estado}"
        page.update()

    page.add(
        slider, switch, ElevatedButton(text="Mostrar", on_click=mostrar_click), salida
    )


if __name__ == "__main__":
    app(target=main)


#  _________________
#  Import LIBRARIES
#  Import FILES
#  _________________
