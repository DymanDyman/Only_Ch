# -*-coding:utf-8 -*-
import wx
class MyFrame(wx.Frame):
    #打印索引+所选内容
    def rb1(self, event):
       print self.radio1.GetSelection(), self.radio1.GetStringSelection()
    
    
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Radio demo', size=(400, 300))
        panel = wx.Panel(self, -1)
        list1 = ['a1111', '2222', '3333', '4444', '5555', '6666']
        list2 = ['hhhh', 'dddd', 'eeee', 'wwww', 'cccc']
        self.radio1 = wx.RadioBox(panel, -1, 'the name', (20, 20), wx.DefaultSize, list1, 4, wx.RA_SPECIFY_COLS)
        wx.RadioBox(panel, -1, 'the sex', (100, 100), wx.DefaultSize, list2, 1, wx.RA_SPECIFY_ROWS)
        
        self.radio1.Bind(wx.EVT_RADIOBOX, self.rb1)
        self.radio1.SetSelection(1)
        
if 1 == 1:
    app = wx.App()
    MyFrame().Show()
    app.MainLoop()
    
