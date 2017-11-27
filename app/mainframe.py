import wx


class MainFrame(wx.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.InitUI()
        self.Center()
        self.Show()

    def InitUI(self):
        pass
