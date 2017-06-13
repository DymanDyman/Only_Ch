import wx
class MyFrame(wx.Frame):

    
    def OnClick1(self, event):
        print 11111, self.radio1.GetValue()
    
    
    def OnClick2(self, event):
        print 22222, self.radio2.GetValue()
        
    def OnClick3(self, event):
        print 33333, self.radio3.GetValue() 
    
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'radiobutton demo', size = (300, 300))
        panel = wx.Panel(self)
        self.radio1 = wx.RadioButton(panel, -1, "11111", pos = (50, 50), style = wx.RB_GROUP)
        self.radio2 = wx.RadioButton(panel, -1, "22222", pos = (50, 80))
        self.radio3 = wx.RadioButton(panel, -1, "33333", pos = (50, 110))
        self.radio1.Bind(wx.EVT_RADIOBUTTON, self.OnClick1)
        self.radio2.Bind(wx.EVT_RADIOBUTTON, self.OnClick2)
        self.radio3.Bind(wx.EVT_RADIOBUTTON, self.OnClick3)
        
if 1 == 1:
    app = wx.App()
    MyFrame().Show()
    app.MainLoop()
