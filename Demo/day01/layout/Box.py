import wx
class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, '111', size = (400, 300))
        sizer = wx.BoxSizer(wx.VERTICAL)
        names = ['111', '222', '333', '444', '555']
        for item in names:
            btn = wx.Button(self, -1, item)
            sizer.Add(btn)
            
        self.SetSizer(sizer)
app = wx.App()
MyFrame().Show()
app.MainLoop()
  
