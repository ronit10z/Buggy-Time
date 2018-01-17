from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.clock import Clock
from collections import defaultdict


class AppScreenManager(ScreenManager):

    def __init__(self, **kwargs):
        super(AppScreenManager, self).__init__(**kwargs)


class Menu(Screen):
    trials = 5
    view = ObjectProperty()
    scrollview = None
    timeDict = defaultdict(lambda: [0]*trials)
    headerString = ["Name"] + ["trial {}".format(i) for i in range(1, trials + 1)]


    def __init__(self, **kwargs):
        super(Menu, self).__init__(**kwargs)
        Clock.schedule_interval(self.create_scrollview, 1)

    def submit_student(self):
 
        # Get the student name from the TextInputs
        student_name = self.name_text_input.text
        print(student_name)
        self.trials+=1
        self.view._trigger_reset_populate()

    def create_scrollview(self, dt):
        # self.view.clear_Widgets()
        if (self.scrollview != None):
            self.scrollview.clear_Widgets()

        base = ["{}".format(i) for i in range(40)]
        layout = GridLayout(cols=self.trials + 1, spacing=0, size_hint_y=None)
        layout.bind(minimum_height=layout.setter("height"))

        for element in self.headerString:
            layout.add_widget(Button(text=element, size=(50, 50), size_hint=(1, None),
                                     background_color=(0.5, 0.5, 0.5, 1), color=(1, 1, 1, 1)))

        for element in base:
            layout.add_widget(Button(text=element, size=(50, 50), size_hint=(1, None),
                                     background_color=(0.5, 0.5, 0.5, 1), color=(1, 1, 1, 1)))
        self.scrollview = ScrollView(size_hint=(None, None), size=(Window.width/2, Window.height),
                pos_hint={'center_x': .5, 'center_y': .5}
                , do_scroll_x=False)
        self.scrollview.add_widget(layout)
        self.view.add_widget(self.scrollview)


Builder.load_file("debug.kv")


class MyAppli(App):

    def build(self):
        return AppScreenManager()


if __name__ == '__main__':
    MyAppli().run()