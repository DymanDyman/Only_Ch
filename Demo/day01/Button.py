'''
Created on 2017-6-6

@author: WuFan
'''
import wx
class Mybutton(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'button demo',size=(400,200))
        panel=wx.Panel(self)
        bmp=wx.Image('HBuilder.bmp',wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        self.button=wx.BitmapButton(panel,-1,bmp,pos=(50,50))
        #self.button=wx.Button(panel,-1,'in',pos=(50,50))
 
if __name__ == '__main__' :
    app=wx.App()      
    frame=Mybutton()
    frame.Show()
    app.MainLoop()