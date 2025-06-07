from kivymd.app import MDApp
from kivy.app import App
from kivy.core.window import Window
from kivymd.uix.label import MDLabel, MDIcon
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager
from kivy.core.image import Image as CoreImage
from kivy.graphics import Color, Rectangle
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.button import MDRaisedButton
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, ListProperty, StringProperty
from kivy.uix.widget import Widget
from kivymd.uix.textfield import MDTextField
from kivy.properties import NumericProperty
from kivy.properties import ObjectProperty
from kivymd.uix.menu import MDDropdownMenu
import data
import functions
from cost import crop
import webbrowser

Window.size = (350, 600)
cr = ["rice", "maize", "chickpea", "kidneybeans", "pigeonpeas", "mothbeans", "mungbeans", "blackgram", "lentil", "pomegranate", "banana", "mango", "grapes", "watermelon", "muskmelon", "apple", "orange", "papaya", "coconut", "cotton", "jute", "coffee"]
crop_ids = {'rice': 1, 'maize': 2, 'chickpea': 3, 'kidneybeans': 4, 'pigeonpeas': 5, 'mothbeans': 6, 'mungbean': 7, 'blackgram': 8, 'lentil': 9, 'pomegranate': 10, 'banana': 11, 'mango': 12, 'grapes': 13, 'watermelon': 14, 'muskmelon': 15, 'apple': 16, 'orange': 17, 'papaya': 18, 'coconut': 19, 'cotton': 20, 'jute': 21, 'coffee': 22}
class Main(MDApp):
    global screen_manager
    screen_manager = ScreenManager()
    cap_temp = ""
    cap_rain = ""
    cap_hum = ""
    cap_pH = ""
    cap_crop = ""
    
    def build(self):
        self.icon = 'assets/favicon.png'
        self.title = "baliraja"
        self.theme_cls.primary_palette = "BlueGray"
        screen_manager.add_widget(Builder.load_file("splash.kv"))
        screen_manager.add_widget(Builder.load_file("main.kv"))
        return screen_manager
    def on_start(self):
        Clock.schedule_once(self.change_screen, 5)
    def change_screen(self, dt):
        screen_manager.current = "mainscreen"
    
    def generate_npk(self):
        cap_rain = float(self.root.get_screen("mainscreen").ids.rain.text)
        cap_hum = float(self.root.get_screen("mainscreen").ids.hum.text)
        cap_temp = float(self.root.get_screen("mainscreen").ids.temp.text)
        cap_pH = float(self.root.get_screen("mainscreen").ids.pH.text)
        cap_crop = self.root.get_screen("mainscreen").ids.crop.text
        text = ""
        for i in crop_ids.keys():
            if cap_crop == i:
                crid = crop_ids[cap_crop]
        N = functions.train_and_predict_N(data.df, cap_hum, cap_temp, cap_rain, cap_pH, crid)
    #    K = functions.train_and_predict_K_category(data.df, cap_hum, cap_temp, cap_rain, cap_pH, crid)
     #   P = functions.train_and_predict_P_category(data.df, cap_hum, cap_temp, cap_rain, cap_pH, crid)
        best = functions.train_evaluate_random_forest(data.df, N, cap_temp, cap_hum, cap_pH, cap_rain)
        text = "Optimal Nitrogen content for " + cap_crop + ": " + str(N) + "\nRecommended for this soil: " + best
        
        result = self.root.get_screen("mainscreen").ids.result
        result.text = text
    def crop_yield(self):
        cap_wgt = float(self.root.get_screen("mainscreen").ids.wgt.text)
        cap_mois = float(self.root.get_screen("mainscreen").ids.mois.text)
        cap_area = float(self.root.get_screen("mainscreen").ids.area.text)
        cap_crop = self.root.get_screen("mainscreen").ids.cropy.text
        text = ""
        output = crop(cap_crop, cap_wgt, cap_mois, cap_area)
        text = "The crop yield for " + cap_crop + " in the specified conditions is projected to be " + str(output) + " megagram per hectare."
        resulty = self.root.get_screen("mainscreen").ids.resulty
        resulty.text = text
    def link1(self):
        webbrowser.open("https://www.iari.res.in/soil-testing")
    def link2(self):
        webbrowser.open("https://farmer.gov.in/FertilizerCalculator.aspx")
    def link3(self):
        webbrowser.open("https://agricoop.nic.in/")
    def link4(self):
        webbrowser.open("https://agricoop.nic.in/en/major-schemes")
    def link5(self):
        webbrowser.open("https://www.iari.res.in")
    def link6(self):
        webbrowser.open("https://www.iari.res.in/sustainable-agriculture")
Main().run()
