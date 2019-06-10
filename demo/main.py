from kivy.lang import Builder
from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.properties import ObjectProperty, ListProperty

Builder.load_string('''
<ListAvions>:
    box: box
    BoxLayout:
        id: box
        orientation: 'vertical'

<AvionToBuy>:
    boxlabel: boxlabel
    size_hint_y: None
    height: 300
    background_color: [1, 0, 1, .5]
    on_release: print(root.avion)
    BoxLayout:
        orientation: 'horizontal'
        Label:
            text: root.avion[0]
            size_hint: None, None
            size: 300, 300
        BoxLayout:
            orientation: 'vertical'
            id: boxlabel
            Label:
                text: root.avion[1]
                size_hint: None, None
                size: 420, 150
        Label:
            text: str(root.avion[2]) + "$"
            size_hint: None, None
            size: 420, 150
''')

AVIONS = [["P51.png", "P51", 750], ["F22.png", "F22", 1500]]

class ListAvions(Popup):
    box = ObjectProperty(None)

def add(self):
    for avion in range(len(AVIONS)):
        aviontobuybut = AvionToBuy()
        aviontobuybut.avion = AVIONS[avion]
        self.box.add_widget(aviontobuybut)

class AvionToBuy(Button):
    avion = ListProperty(AVIONS[0])

class AvionApp(App):
    def build(self):
        z = ListAvions()
        z.add()
        return z

if __name__=="__main__":
    AvionApp().run()