from bdcontatos import insert, listar_contatos
from conexaobd import connect
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class Backend:
    def __init__(self):
        try:
            self.bd = connect()
        except Exception as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            raise

    def armazenar_e_ordenar(self, nome, numero='', email='', nascimento=''):
        insert(self.bd, nome, numero, email, nascimento)

    def mostrar_nomes_ordenados(self):
        nomes = listar_contatos(self.bd)
        nomes_ordenados = sorted(nomes)
        return nomes_ordenados

class InterfaceKivy(BoxLayout):
    def __init__(self, backend, **kwargs):
        super(InterfaceKivy, self).__init__(**kwargs)
        self.backend = backend

        self.orientation = 'vertical'

        self.input_nome = TextInput(hint_text='Digite um nome')
        self.add_widget(self.input_nome)

        self.btn_adicionar_nome = Button(text='Adicionar Nome')
        self.btn_adicionar_nome.bind(on_press=self.adicionar_nome)
        self.add_widget(self.btn_adicionar_nome)

        self.btn_mostrar_nomes = Button(text='Mostrar Nomes Ordenados')
        self.btn_mostrar_nomes.bind(on_press=self.mostrar_nomes)
        self.add_widget(self.btn_mostrar_nomes)

        self.label_nomes = Label(text='')
        self.add_widget(self.label_nomes)

    def adicionar_nome(self, instance):
        nome = self.input_nome.text.strip()
        if nome:
            self.backend.armazenar_e_ordenar(nome)
            self.input_nome.text = ''

    def mostrar_nomes(self, instance):
        nomes_ordenados = self.backend.mostrar_nomes_ordenados()
        self.label_nomes.text = '\n'.join(nomes_ordenados)

class MyApp(App):
    def build(self):
        try:
            backend = Backend()
            return InterfaceKivy(backend)
        except Exception as e:
            print(f"Erro ao iniciar a aplicação: {e}")
            return None

if __name__ == '__main__':
    MyApp().run()
