# coding: utf-8

import wx


class MyApp(wx.App):
    def OnInit(self):
        self.mainWnd = wx.Frame(None, -1, "")
        self.SetTopWindow(self.mainWnd)
        self.mainWnd.SetTitle('Hello wx_Freeze')
        self.mainWnd.Show()
        return True


if __name__ == "__main__":
    app = MyApp(False)
    app.MainLoop()
