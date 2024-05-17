from conexaobd import *
from bdcontatos import *
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class Backend:
    def __init__(self):
        self.emails = set()

    def adicionar_email(self, email):
        if email:
            self.emails.add(email)
            print(f"E-mail '{email}' adicionado com sucesso!")

    def consultar_email(self, email):
        if email in self.emails:
            print(f"E-mail '{email}' encontrado.")
        else:
            print(f"E-mail '{email}' não encontrado.")

    def mostrar_emails(self):
        print("Lista de e-mails:")
        for email in self.emails:
            print(email)

class InterfaceKivy(BoxLayout):
    def __init__(self, backend, **kwargs):
        super().__init__(**kwargs)
        self.backend = backend

        self.orientation = 'vertical'

        self.input_email = TextInput(hint_text='Digite seu e-mail')
        self.add_widget(self.input_email)

        self.btn_adicionar_email = Button(text='Adicionar Email')
        self.btn_adicionar_email.bind(on_press=self.adicionar_email)
        self.add_widget(self.btn_adicionar_email)

        self.btn_consultar_email = Button(text='Consultar Email')
        self.btn_consultar_email.bind(on_press=self.consultar_email)
        self.add_widget(self.btn_consultar_email)

        self.label_emails = Label(text='')
        self.add_widget(self.label_emails)

    def adicionar_email(self, instance):
        email = self.input_email.text.strip()
        self.backend.adicionar_email(email)

    def consultar_email(self, instance):
        email = self.input_email.text.strip()
        self.backend.consultar_email(email)
        self.backend.mostrar_emails()
        self.label_emails.text = '\n'.join(self.backend.emails)

class MyApp(App):
    def build(self):
        backend = Backend()
        return InterfaceKivy(backend)

if __name__ == '__main__':
    MyApp().run()