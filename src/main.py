#  _________________
#  Import LIBRARIES
import flet as ft
from flet import Page, app, RadioGroup, Column, Radio, Text, ElevatedButton
#  Import FILES
#  _________________


def main(page: Page) -> None:  # función principal de la ventana
    page.title = "Quinto ejercicio - Grupo de RadioButtons"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    grupo: RadioGroup = RadioGroup(
        content=Column(
            controls=[
                Radio(value="opcion1", label="Opción 1"),
                Radio(value="opcion2", label="Opción 2"),
                Radio(value="opcion3", label="Opción 3"),
            ]
        )
    )

    resultado: Text = Text(value="")

    def mostrar_opcion(e: ft.ControlEvent):
        resultado.value = f"Seleccionaste: {grupo.value}"
        page.update()

    page.add(
        grupo, ElevatedButton(text="Mostrar opción", on_click=mostrar_opcion), resultado
    )


if __name__ == "__main__":
    app(target=main)


#  _________________
#  Import LIBRARIES
#  Import FILES
#  _________________
