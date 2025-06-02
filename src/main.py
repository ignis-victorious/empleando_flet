#  _________________
#  Import LIBRARIES
import flet as ft
from flet import Page, app, TextField, Text, Column, Row, ElevatedButton
#  Import FILES
#  _________________


class Persona:
    def __init__(
        self, codigo: int, nombre: str, apellido: str, edad: int
    ) -> None:  # constructor del objeto de la clase p
        self.codigo: int = codigo
        self.nombre: str = nombre
        self.apellido: str = apellido
        self.edad: int = edad

    def __repr__(self) -> str:
        return f"({self.codigo}, {self.nombre}, {self.apellido}, {self.edad})"  # método que retorna los valores


class Nodo:
    def __init__(self, dato: Persona) -> None:
        self.dato: Persona = dato
        self.siguiente = None


class ListaEnlazada:  # LinkedList
    def _init__(self) -> None:
        self.primer_nodo: Nodo | None = None

    def insertar_al_inicio(self, dato: Persona) -> None:
        print("Inside insertar_al_inicio")
        nuevo_nodo: Nodo = Nodo(dato=dato)
        print(f"nuevo_nodo: {nuevo_nodo}")
        nuevo_nodo.siguiente = self.primer_nodo
        print(f"nuevo_nodo.siguiente: {nuevo_nodo.siguiente}")
        self.primer_nodo: Nodo | None = nuevo_nodo

    def imprimir(self) -> list[Persona | None]:  # Print
        elementos: list = []
        nodo_actual = self.primer_nodo
        while nodo_actual:
            elementos.append(str(nodo_actual.dato))
            nodo_actual = nodo_actual.siguiente
        return elementos

    def buscar(self, codigo: int) -> Persona | None:
        nodo_actual: Nodo | None = self.primer_nodo
        while nodo_actual:
            if nodo_actual.dato.codigo == codigo:
                return nodo_actual.dato
            nodo_actual = nodo_actual.sigulente
        return None

    def ordenar(self):
        if self_primer_nodo is None:
            return

        nodo_actual: Nodo | None = self.primer_nodo
        while nodo_actual:
            nodo_min = nodo_actual
            sigulente_nodo = nodo_actual.sigulente
            while siguiente_nodo:
                if siguiente_nodo.dato.edad > nodo_min.dato.edad:
                    nodo_min = siguiente_nodo
                siguiente_nodo = siguiente_nodo.siguiente
            nodo_actual.dato, nodo_min.dato = nodo_min.dato, nodo_actual.dato
            nodo_actual = nodo_actual.sigulente


lista: ListaEnlazada = ListaEnlazada()


#  ---  UI  ---
def main(page: Page) -> None:
    page.title = "Segundo exercicio - Lista Enlazada de Personas"

    codigo: TextField = TextField(label="Codigo", width=200)
    nombre: TextField = TextField(label="Nombre", width=200)
    apellido: TextField = TextField(label="Apellido", width=200)
    edad: TextField = TextField(
        label="Edad", width=200, keyboard_type=ft.KeyboardType.NUMBER
    )

    output: Text = Text(value="", size=16)
    lista_output = Column()

    def agregar_persona(e: ft.ControlEvent) -> None:
        try:
            persona: Persona = Persona(
                codigo=int(codigo.value or 0),
                nombre=nombre.value or "",
                apellido=apellido.value or "",
                edad=int(edad.value or 0),
            )
            print(f"persona: {persona}")
            lista.insertar_al_inicio(dato=persona)
            output.value = "Persona registrada con éxito."
            codigo.value = nombre.value = apellido.value = edad.value = ""
            actualizar_lista()
        except:
            output.value = "Error: Datos inválidos."
        page.update()

    def actualizar_lista() -> None:
        lista_output.controls.clear()
        for item in lista.imprimir():
            lista_output.controls.append(Text(value=item))

    def ordenar_lista(e: ft.ControlEvent) -> None:
        lista.ordenar()
        output.value = "Lista ordenada por edad (mayon a menor)."
        actualizar_lista()
        page.update()

    def buscar_persona(e: ft.ControlEvent):
        try:
            cod: int = int(codigo.value)
            persona = lista.buscar(codigo=cod)
            if persona:
                output.value = f"Encontrado: {persona}"
            else:
                output.value = f"No se encontró persona con código {cod}"
        except:
            output.value = "Ingrese un código válido para buscar."
        page.update()

    page.add(
        Column(
            controls=[
                Row(controls=[codigo, nombre]),
                Row(controls=[apellido, edad]),
                Row(
                    controls=[
                        ElevatedButton(text="Agregar", on_click=agregar_persona),
                        ElevatedButton(text="Ordenar por edad", on_click=ordenar_lista),
                        ElevatedButton(
                            text="Buscar por código", on_click=buscar_persona
                        ),
                    ]
                ),
                output,
                Text(value="Lista de personas:"),
                lista_output,
            ]
        )
    )


if __name__ == "__main__":
    app(target=main)


#  _________________
#  Import LIBRARIES
#  Import FILES
#  _________________
