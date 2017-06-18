import wx
class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'gride demo')
        sizer = wx.FlexGridSizer(rows = 2, cols = 2, hgap = 5, vgap = 5)
        sizer.AddGrowableCol(0,1)
        sizer.AddGrowableCol(1,10)
        label = ['C', 'java', 'python', 'php']
        style = {'C':wx.ALIGN_BOTTOM, 'java':wx.ALIGN_CENTER, 'python':wx.ALIGN_RIGHT, 'php':wx.EXPAND}
        for item in label:
            bt = wx.Button(self, -1, item)
            flag = style.get(item, 0)
            sizer.Add(bt, 0, flag)
        self.SetSizer(sizer)
        self.Fit()
app = wx.App()
MyFrame().Show()
app.MainLoop()
  
