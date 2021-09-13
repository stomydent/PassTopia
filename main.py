from dotenv import load_dotenv
from wx.core import EmptyString
from ui.gui import mainWindow,dlgAbout
from ctypes import windll
import os, wx, string

load_dotenv('./config/.env')

class MainWindow(mainWindow):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        icon = wx.Icon(f"{os.getcwd()}{os.getenv('APPICON')}", wx.BITMAP_TYPE_PNG)
        self.SetIcon(icon)
        self.SetTitle(os.getenv('APPNAME'))

    def AppExit(self, event):
        self.Destroy()

    def AppAbout( self, event ):
        DLGAbout(self)

    def btnGenPass_Click( self, event ):
        dict = ""
        if self.chkAlphabetMinor.IsChecked()==True:
            dict += string.ascii_lowercase
        if self.chkAlphabetCapital.IsChecked()==True:
            dict += string.ascii_uppercase
        if self.chkAlphabetNumbers.IsChecked()==True:
            dict += string.digits
        if self.chkAlphabetSpecial.IsChecked()==True:
            dict += string.punctuation
        
        if not dict: windll.user32.MessageBoxW(0, "Dictionary cannot be empty", f"{os.getenv('APPNAME')}", 0 )


class DLGAbout(dlgAbout):
    def __init__(self, parent):
        super().__init__(parent)
        self.txtAppName.SetLabel(f"{os.getenv('APPNAME')} v{os.getenv('APPVERSION')}")
        self.lblAppDescription.SetLabel(os.getenv('APPDESC'))
        self.Show()

    def btnOK_Click( self, event ):
        self.Destroy()

    def btnCancel_Click( self, event ):
        self.Destroy()

























if __name__ == '__main__':
    app = wx.App()
    frame =  MainWindow(None)
    frame.Show()
    app.MainLoop()

