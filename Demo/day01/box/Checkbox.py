import wx
class MyFrame(wx.Frame):

    
    def OnClick1(self,event):
        print 11111,self.check1.GetValue()
    
    
    def OnClick2(self,event):
        print 22222,self.check2.GetValue()
    
    
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'checkbox demo',size=(300,200))
        panel=wx.Panel(self)
        self.check1=wx.CheckBox(panel,-1,'basketball',(50,40),(150,20))
        self.check2=wx.CheckBox(panel,-1,"football",(50,60),(150,20))
        self.check3=wx.CheckBox(panel,-1,"volleyball",(50,80),(150,20))
        self.check1.Bind(wx.EVT_CHECKBOX, self.OnClick1)
        self.check2.Bind(wx.EVT_CHECKBOX, self.OnClick2)

if 1==1:
    app=wx.App()
    MyFrame().Show()
    app.MainLoop()