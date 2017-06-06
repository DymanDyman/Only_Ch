
import wx
class WuFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'woshiwufan', size=(300, 200))
        panel=wx.Panel(self,-1)
        lable2 = wx.StaticText(panel, -1, 'woshineirong', (100, 10))
        lable2.SetBackgroundColour('BLACK')
        lable2.SetForegroundColour("White")
        
        text=wx.StaticText(panel,-1,'sssss',(150,20),(50,-1),wx.ALIGN_BOTTOM)
        text.SetForegroundColour('BLUE')
        text.SetBackgroundColour('Purpose')
app = wx.App()        
wFrame = WuFrame()
wFrame.Show()
app.MainLoop()
