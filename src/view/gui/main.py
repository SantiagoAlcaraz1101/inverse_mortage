from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup

import sys
import os
sys.path.append(os.path.abspath("src"))

from model.inverse_mortage import Person, Property
from model.exceptions import OldAgeError, PropertyAntiquenessBigger, PropertyValueError, StratumError
from model.property_value import property_value

class MortgageForm(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=20, **kwargs)

        self.inputs = {}

        grid = GridLayout(cols=2, spacing=10, size_hint=(1, 0.9))

        fields = [
            ("Nombre", "name"),
            ("Edad", "age"),
            ("¿Es mujer? (si/no)", "is_women"),
            ("¿Tiene discapacidad? (si/no)", "discapacity_condition"),
            ("Estrato", "stratum"),
            ("Valor comercial", "commercial_value"),
            ("Antigüedad", "antiqueness"),
            ("¿Es legal la propiedad? (si/no)", "legality"),
            ("¿Está al día con impuestos? (si/no)", "taxes_ok"),
            ("¿Tiene título de propiedad? (si/no)", "property_title")
        ]

        for label_text, key in fields:
            grid.add_widget(Label(text=label_text, font_size=20, size_hint_x=0.5))
            input_field = TextInput(multiline=False, font_size=20, size_hint_x=0.5)
            self.inputs[key] = input_field
            grid.add_widget(input_field)

        self.add_widget(grid)

        submit_btn = Button(
            text="Verificar Hipoteca Inversa",
            size_hint=(1, 0.1),
            font_size=22,
            height=60
        )
        submit_btn.bind(on_press=self.verify)
        self.add_widget(submit_btn)

    def verify(self, instance):
        try:
            data = {k: v.text.strip().lower() for k, v in self.inputs.items()}

            if any(v == '' for v in data.values()):
                raise ValueError("Ingrese todos los datos")

            try:
                age = int(data["age"])
            except ValueError:
                raise ValueError("La edad debe ser un número entero válido.")

            # Validación del estrato (debe ser un número entero)
            try:
                stratum = int(data["stratum"])
            except ValueError:
                raise ValueError("El estrato debe ser un número entero válido.")

            # Validación del valor comercial (debe ser un número flotante)
            try:
                commercial_value = float(data["commercial_value"])
            except ValueError:
                raise ValueError("El valor comercial debe ser un número válido.")

            # Validación de antigüedad (debe ser un número entero)
            try:
                antiqueness = int(data["antiqueness"])
            except ValueError:
                raise ValueError("La antigüedad debe ser un número entero válido.")

            # Validación de sí/no para campos booleanos
            def validate_yes_no(value, field_name):
                if value not in ["si", "no"]:
                    raise ValueError(f"El valor para {field_name} debe ser 'si' o 'no'.")
                return value == "si"

            
            is_women = validate_yes_no(data["is_women"], "¿Es mujer?")
            discapacity_condition = validate_yes_no(data["discapacity_condition"], "¿Tiene discapacidad?")
            legality = validate_yes_no(data["legality"], "¿Es legal la propiedad?")
            taxes_ok = validate_yes_no(data["taxes_ok"], "¿Está al día con impuestos?")
            property_title = validate_yes_no(data["property_title"], "¿Tiene título de propiedad?")
            # Crear la persona y la propiedad
            person = Person(
                name=data["name"],
                age=int(data["age"]),
                is_women=data["is_women"] == "si",
                discapacity_condition=data["discapacity_condition"] == "si",
                property=Property(
                    stratum=int(data["stratum"]),
                    commercial_value=float(data["commercial_value"]),
                    antiqueness=int(data["antiqueness"]),
                    legality=data["legality"] == "si",
                    taxes_ok=data["taxes_ok"] == "si"
                ),
                property_title=data["property_title"] == "si"
            )
            

            person.is_old_enough()
            person.property.required_stratum()
            person.property.is_value_enough()
            person.property.is_property_valid()

            cuota = property_value(person.hope_of_life(), person.property.commercial_value)
            message = f"El valor de tu cuota es: {cuota:.2f}"
            self.show_popup("Resultado", message)

        except (PropertyAntiquenessBigger, PropertyValueError, StratumError, OldAgeError) as e:
            self.show_popup("Error de Validación", str(e))

        except Exception as e:
            self.show_popup("Error", f"Entrada inválida o error inesperado:\n{str(e)}")

    def show_popup(self, title, message):
        popup = Popup(
            title=title,
            content=Label(text=message, font_size=18),
            size_hint=(0.8, 0.5),
            auto_dismiss=True
        )
        popup.open()

class InverseMortgageApp(App):
    def build(self):
        return MortgageForm()

if __name__ == "__main__":
    InverseMortgageApp().run()
