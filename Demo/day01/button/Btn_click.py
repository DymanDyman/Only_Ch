import wx
class MyFrame(wx.Frame):

    
    def OnButtonClick(self, event):
        print 'the button is clicked'
    
    
    def OnTextClicl(self, event):
        print 'the StaticText is clicked'
    
    
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'xingxing', size = (300, 200))
        panel = wx.Panel(self)
        self.button = wx.Button(panel, -1, 'Btn Click', pos = (100, 20))
        self.Bind(wx.EVT_BUTTON, self.OnButtonClick, self.button)
        self.label = wx.StaticText(panel, -1, 'SText Click', pos = (100, 120))
        self.label.Bind(wx.EVT_LEFT_DOWN, self.OnTextClicl)

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()
