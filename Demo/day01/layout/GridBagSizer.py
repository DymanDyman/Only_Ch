import wx
class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'gride demo')
        sizer = wx.GridBagSizer(hgap=4,vgap=4)
        for col in range(3):
            for row in range(3):
                bt=wx.Button(self,-1,'python')
                sizer.Add(bt,pos=(row,col))
        btn1=wx.Button(self,-1,'java')
        sizer.Add(btn1,pos=(0,3),span=(2,1),flag=wx.EXPAND)
        
        btn2=wx.Button(self,-1,'ruby')
        sizer.Add(btn2,pos=(3,0),span=(1,3),flag=wx.EXPAND)
        
        sizer.AddGrowableCol(1)
        sizer.AddGrowableRow(3)
        self.SetSizer(sizer)
        self.Fit()
app = wx.App()
MyFrame().Show()
app.MainLoop()
  
