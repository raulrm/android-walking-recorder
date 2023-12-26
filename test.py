import kivy.app
import kivy.uix.label
from kivy.uix.boxlayout import BoxLayout 
import random

kivy.require('1.9.0')

class MiRaiz(BoxLayout):

    def __init__(self):
        super(MiRaiz, self).__init__()
    
    def generar(self):
        self.random_label.text = str(random.randint(0, 1000))

class TestApp(kivy.app.App):

    def build(self):
        #return kivy.uix.label.Label(text='Hola a todos')
        return MiRaiz()
            
    
app = TestApp(title='Primera Aplicacion')
app.run()