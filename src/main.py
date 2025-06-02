#  _________________
#  Import LIBRARIES
import flet as ft
from flet import Page, app, TextField, Dropdown, Checkbox, Text, ElevatedButton
#  Import FILES
#  _________________


def main(page: Page) -> None:  # función principal de la ventana
    page.title = "Terzero ejercicio -  Ejemplo de Controles Básicos"

    # Controles
    nombre: TextField = TextField(label="Nombre", width=500)
    edad: TextField = TextField(
        label="Edad", width=200, keyboard_type=ft.KeyboardType.NUMBER
    )
    genero: Dropdown = Dropdown(
        value="menu desplegable",
        label="Género",
        options=[
            ft.dropdown.Option(key="Masculino"),
            ft.dropdown.Option(key="Femenino"),
            ft.dropdown.Option(key="Otro"),
        ],
    )

    acepto: Checkbox = Checkbox(label="Acepto Los términos")
    salida: Text = Text(value="")

    def enviar_click(e: ft.ControlEvent):
        if acepto.value:
            salida.value = (
                f"Hola, {nombre.value}, tienes {edad.value} años y eres {genero.value}."
            )
        else:
            salida.value = "Debes aceptar los términos."
        page.update()

    # Diseño UI
    page.add(
        nombre,
        edad,
        genero,
        acepto,
        ElevatedButton(text="Enviar", on_click=enviar_click),
        salida,
    )


if __name__ == "__main__":
    app(target=main)


#  _________________
#  Import LIBRARIES
#  Import FILES
#  _________________
