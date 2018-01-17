from ThreeDObjects import *
from tkinter import messagebox,simpledialog
import wolframalpha
import urllib
import json

class SimpleButton(object):
    def __init__(self,name,cx,cy,r):
        self.name = name
        self.cx = cx
        self.cy = cy
        self.r = r
        self.r1 = r
        self.r2 = r/2
        self.mouseHovering = False #mouse is over the button

    def getBounds(self):
        x0 = self.cx - self.r1
        y0 = self.cy - self.r2
        x1 = self.cx + self.r1
        y1 = self.cy + self.r2
        return (x0,y0,x1,y1)

    def containsPoint(self,x,y):
        (x0,y0,x1,y1) = self.getBounds()
        #point inside the bounds
        return x0 <= x <= x1 and y0 <= y <= y1

    def draw(self,canvas):
        #bolds the box if the mouse is over it
        if self.mouseHovering:
            font = 'Helvetica 10 bold'
            width = 3
        else:
            font = 'Helvetica 10'
            width = 1
        canvas.create_rectangle(self.getBounds(),width =width)
        canvas.create_text(self.cx,self.cy,text = self.name,font = font)

class ActionButton(SimpleButton):
    def __init__(self,name,cx,cy,r,f):
        super().__init__(name,cx,cy,r)
        self.f = f #function the button will call

    def action(self,*args):
        #calls the function
        return self.f(*args)

class CheckBox(ActionButton):
    def __init__(self,name,cx,cy,r,f,color):
        super().__init__(name,cx,cy,r,f)
        self.visible = True
        self.r1 = self.r2 = r
        self.color = color

    def action(self,*args):
        super().action(*args)
        #toggle fill on box
        self.visible = not self.visible

    def hide(self):
        #force visibility False
        super().action(False)
        self.visible = False

    def show(self):
        #force visibility True
        super().action(True)
        self.visible = True

    def draw(self,canvas):
        if self.visible: fill = self.color
        else: fill = 'white'
        r = self.r
        cx,cy = self.cx,self.cy
        canvas.create_rectangle(cx - r,cy - r, cx + r, cy + r, fill = fill)
        canvas.create_text(cx + r,cy,text = "  " + self.name,anchor = 'w')
