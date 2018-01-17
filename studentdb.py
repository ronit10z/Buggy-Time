from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton
from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory
from kivy.uix.popup import Popup
from collections import OrderedDict

import csv
import os

class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)


class SaveDialog(FloatLayout):
    save = ObjectProperty(None)
    text_input = ObjectProperty(None)
    cancel = ObjectProperty(None)

class StudentListButton(ListItemButton):
    pass
 

class StudentDB(BoxLayout):
 
    # Connects the value in the TextInput widget to these
    # fields
    name_text_input = ObjectProperty()
    student_list = ObjectProperty()

    loadfile = ObjectProperty()
    savefile = ObjectProperty()
    text_input = ObjectProperty()

    

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def show_save(self):
        content = SaveDialog(save=self.save, cancel=self.dismiss_popup)
        self._popup = Popup(title="Save file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        assert(filename[0].endswith(".csv"))

        with open(os.path.join(path, filename[0])) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            names = [row[0] for row in readCSV]
            for name in names:
                self.student_list.adapter.data.extend([name])

        self.dismiss_popup()

    def save(self, path, filename):
        with open(os.path.join(path, filename), 'w') as stream:
            stream.write(self.text_input.text)

        self.dismiss_popup()

    def submit_student(self):
 
        # Get the student name from the TextInputs
        student_name = self.name_text_input.text
 
        # Add the student to the ListView
        self.student_list.adapter.data.extend([student_name])
 
        # Reset the ListView
        self.student_list._trigger_reset_populate()
 
    def delete_student(self, *args):
 
        # If a list item is selected
        if self.student_list.adapter.selection:
 
            # Get the text from the item selected
            selection = self.student_list.adapter.selection[0].text
 
            # Remove the matching item
            self.student_list.adapter.data.remove(selection)
 
            # Reset the ListView
            self.student_list._trigger_reset_populate()
 
    def replace_student(self, *args):
 
        # If a list item is selected
        if self.student_list.adapter.selection:
 
            # Get the text from the item selected
            selection = self.student_list.adapter.selection[0].text
 
            # Remove the matching item
            self.student_list.adapter.data.remove(selection)
 
            # Get the student name from the TextInputs
            student_name = self.first_name_text_input.text + " " + self.last_name_text_input.text
 
            # Add the updated data to the list
            self.student_list.adapter.data.extend([student_name])
 
            # Reset the ListView
            self.student_list._trigger_reset_populate()
 
 
class StudentDBApp(App):
    def build(self):
        return StudentDB()

    

def main():
    dbApp = StudentDBApp()
    dbApp.run()
    return

if __name__ == '__main__':
    main()