# coding=utf-8
import wx
import os
class MyFrame(wx.Frame):

    
    def onOpen(self,event):
        dlg=wx.FileDialog(None,'选择一个文件',os.getcwd(),'','',wx.OPEN)
        if dlg.ShowModal()==wx.ID_OK:
            print dlg.GetPath()
        dlg.Destroy()
    
    
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'dialog demo', size = (300, 200))
        panel = wx.Panel(self)
        btn = wx.Button(panel, -1, '打开文件', pos = (30, 30))
        btn.Bind(wx.EVT_BUTTON, self.onOpen)
app = wx.App()
MyFrame().Show()
app.MainLoop()