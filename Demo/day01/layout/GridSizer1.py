import wx
class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'grid demo')
        sizer=wx.GridSizer(rows=3,cols=2,hgap=4,vgap=4)
        label=['C','java','python','ruby','perl']
        for item in label:
            bt=wx.Button(self,-1,item)
            sizer.Add(bt)
        self.SetSizer(sizer)
        self.Fit()
app=wx.App()
MyFrame().Show()
app.MainLoop()