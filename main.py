from dotenv  import load_dotenv
from wx.core import EmptyString, Font
from ui.gui  import mainWindow,dlgAbout
from ctypes  import windll
from secrets import choice
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
        #Get generation boundaries
        dict = ""
        passLength = self.slideLength.GetValue()
        passCount  = self.slideCount.GetValue()

        #Validation
        if self.chkAlphabetMinor.IsChecked()==True:
            dict += string.ascii_lowercase
        if self.chkAlphabetCapital.IsChecked()==True:
            dict += string.ascii_uppercase
        if self.chkAlphabetNumbers.IsChecked()==True:
            dict += string.digits
        if self.chkAlphabetSpecial.IsChecked()==True:
            dict += string.punctuation
        if        not dict: windll.user32.MessageBoxW(0, "Dictionary cannot be empty", f"{os.getenv('APPNAME')}", 0 )
        if passLength <= 0: windll.user32.MessageBoxW(0, f"Password length cannot be <= {passLength}", f"{os.getenv('APPNAME')}", 0 )
        if passLength >100: windll.user32.MessageBoxW(0, f"Password length cannot be  > {passLength}", f"{os.getenv('APPNAME')}", 0 )
        if passCount  <= 0: windll.user32.MessageBoxW(0, f"Password  count cannot be <= {passCount}", f"{os.getenv('APPNAME')}", 0 ) 
        if passCount   >50: windll.user32.MessageBoxW(0, f"Password  count cannot be  > {passCount}", f"{os.getenv('APPNAME')}", 0 ) 

        #Generation
        passBuffer = []
        for i in range(passCount): passBuffer.append(''.join([choice(dict) for _ in range(passLength)]))
        self.m_textCtrl1.SetFont(Font(10, wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, underline=False, faceName="Terminal", encoding=wx.FONTENCODING_DEFAULT))
        self.m_textCtrl1.Value = '\n'.join(passBuffer)


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

