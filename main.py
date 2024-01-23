from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from models import Pizza
from kivy.properties import ObjectProperty, StringProperty, BooleanProperty, NumericProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.behaviors import CoverBehavior
from http_client import HttpClient
from storage_manager import StorageManager
import os

class PizzaWidget(BoxLayout):
    name = StringProperty()
    ingredients = StringProperty()
    price = NumericProperty()
    vegetarian = BooleanProperty()

class MainWidget(FloatLayout):
    recycleView = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        HttpClient().get_pizzas(self.on_server_data)

    def on_parent(self, widget, parent):
        pizza_dict = StorageManager().load_data('pizzas')
        if pizza_dict:
            self.recycleView.data = pizza_dict

    def on_server_data(self, pizza_dict):
        self.recycleView.data = pizza_dict
        StorageManager().save_data('pizzas', pizza_dict)


class PizzaApp(App):
    pass

PizzaApp().run()    