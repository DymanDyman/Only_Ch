import wx 
class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'static demo')
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.panel = wx.Panel(self)
        box1 = wx.StaticBox(self.panel, -1, 'java')
        sizer1 = wx.StaticBoxSizer(box1, wx.VERTICAL)
        for item in ['java', 'j2e', 'jvm']:
            btn = wx.Button(box1, -1, item)
            sizer1.Add(btn)
        box2 = wx.StaticBox(self.panel, -1, 'php')
        sizer2 = wx.StaticBoxSizer(box2, wx.VERTICAL)
        for item in ['111', '222', '333', '444']:
            btn = wx.Button(box2, -1, item)
            sizer2.Add(btn)
        sizer.Add(sizer1)
        sizer.Add(sizer2)
        self.panel.SetSizer(sizer)
app = wx.App()
MyFrame().Show()
app.MainLoop()
