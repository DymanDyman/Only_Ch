import wx 
class MyDia(wx.Dialog):
    def __init__(self):
        wx.Dialog.__init__(self, None, -1, 'dialog demo', size = (300, 200))
        lable = wx.StaticText(self, -1, 'do you leave?')
        okbtn = wx.Button(self, wx.ID_OK, 'ok', pos = (20, 60))
        okbtn.SetDefault()
        canbtn = wx.Button(self, wx.ID_CANCEL, 'cancel', pos = (200, 60))
    
if 1 == 1:
    app = wx.App()
    app.MainLoop()
    dlg = MyDia()
    result = dlg.ShowModal()
    if result == wx.ID_OK:
        print 'ok button is called'
    else:
        print 'cancel button'
    dlg.Destroy()
raw_input()   
