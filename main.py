from dotenv  import load_dotenv
from wx.core import EmptyString, Font
from ui.gui  import mainWindow,dlgAbout
from ctypes  import windll
from secrets import choice,randbits
from sys     import platform
import os, wx, string, gnupg
import lib.genbtc, lib.geneth

load_dotenv('./config/.env')

gpg_customhome = os.getenv('GPG_HOME')
gpg_home       = ''

if gpg_customhome == 'default':
    found = False
    if found == False and os.path.isdir(os.environ['USERPROFILE']):
        brk = False
        for root, dirs, files in os.walk(os.environ['USERPROFILE']):
            if brk == True: break
            for name in dirs:
                if name == '.gnupg':
                    brk   = True
                    found = True
                    gpg_home = os.environ['USERPROFILE']+'\.gnupg'
                    break
                if name == 'gnupg':
                    brk   = True
                    found = True
                    gpg_home = os.environ['USERPROFILE']+'\gnupg'
                    break

if gpg_customhome != 'default':
    gpg_home = os.getenv('GPG_HOME')

gpg = gnupg.GPG(gnupghome=gpg_home)



class MainWindow(mainWindow):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        icon = wx.Icon(f"{os.getcwd()}{os.getenv('APPICON')}", wx.BITMAP_TYPE_PNG)
        self.SetIcon(icon)
        self.SetTitle(os.getenv('APPNAME'))

        #Set GPG keypair expiry to Never as default
        self.lblExpires.Selection = 0
        if (self.lblExpires.Selection == 0): 
            self.txtTimeQuantity.Enabled = False
        else:

            self.txtTimeQuantity.Enabled = True

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

    def btnBTCGen_Click( self, event ):
        bits = randbits(256)
        bits_hex = hex(bits)
        private_key = bits_hex[2:] 
        self.txtBTCPublicKey.Value  = lib.genbtc.BitcoinWallet.generate_compressed_address(private_key)
        self.txtBTCPrivateKey.Value = lib.genbtc.BitcoinWallet.private_to_wif_compressed(private_key)

    def btnETHGen_Click(self, event):
        bits = randbits(256)
        bits_hex = hex(bits)
        private_key = bits_hex[2:] 
        self.txtETHPubKey.Value = lib.geneth.EthereumWallet.generate_address(private_key)
        self.txtETHPrivateKey.Value = private_key

    def btnBTCSave_Click( self, event ):
        if (self.txtBTCPublicKey.GetValue() == EmptyString) or (self.txtBTCPrivateKey.GetValue() == EmptyString):
            windll.user32.MessageBoxW(0, "You must generate your wallet before saving it", f"{os.getenv('APPNAME')}", 0 ) 
            return
        dlgFileSave = wx.FileDialog(self,
                                'Save File',
                                "", "",
                                'All files (*.*)|*.*',
                                wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
        if dlgFileSave.ShowModal() == wx.ID_CANCEL:
            return
        file = open(dlgFileSave.GetPath(),'w')
        file.write('Public  Key: ' + self.txtBTCPublicKey.GetValue() + '\n')
        file.write('Private Key: ' + self.txtBTCPrivateKey.GetValue() + '\n')
        file.close()
        windll.user32.MessageBoxW(0, "File saved successfully", f"{os.getenv('APPNAME')}", 0 ) 

    def btnETHSave_Click( self, event ):
        if (self.txtETHPubKey.GetValue() == EmptyString) or (self.txtETHPrivateKey.GetValue() == EmptyString):
            windll.user32.MessageBoxW(0, "You must generate your wallet before saving it", f"{os.getenv('APPNAME')}", 0 ) 
            return
        dlgFileSave = wx.FileDialog(self,
                                'Save File',
                                "", "",
                                'All files (*.*)|*.*',
                                wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
        if dlgFileSave.ShowModal() == wx.ID_CANCEL:
            return
        file = open(dlgFileSave.GetPath(),'w')
        file.write('Public  Key: ' + self.txtETHPubKey.GetValue() + '\n')
        file.write('Private Key: 0x' + self.txtETHPrivateKey.GetValue() + '\n')
        file.close()
        windll.user32.MessageBoxW(0, "File saved successfully", f"{os.getenv('APPNAME')}", 0 ) 

    def radioGPGExpiry_Click( self, event ):
        if self.lblExpires.Selection == 1: self.txtTimeQuantity.Enabled = True
        if self.lblExpires.Selection == 0: self.txtTimeQuantity.Enabled = False

    def btnGPGGen_Click( self, event ):
        expiry = 0 if self.lblExpires.GetSelection() == 0 else self.txtTimeQuantity.Value
        comment = self.txtComment.Value

        if expiry == EmptyString: expiry = 0

        if self.txtPassphrase.Value != self.txtConfirm.Value: 
            windll.user32.MessageBoxW(0, "Passphrase does not match confirmation", f"{os.getenv('APPNAME')}", 0 ) 
            return
        if self.txtPassphrase.Value == EmptyString and self.txtConfirm.Value == EmptyString:
            windll.user32.MessageBoxW(0, "Empty passphrase field", f"{os.getenv('APPNAME')}", 0 )
            return
        if self.txtEmail.Value == EmptyString:
            windll.user32.MessageBoxW(0, "Empty email field", f"{os.getenv('APPNAME')}", 0 )
            return
        if self.txtRealName.Value == EmptyString:
            windll.user32.MessageBoxW(0, "Empty name field", f"{os.getenv('APPNAME')}", 0 )
            return
        if comment == EmptyString: comment = f"Generated with GNUPG/{os.getenv('APPNAME')}" 

        input_data = gpg.gen_key_input(
            key_type      = self.radioKeyType.GetStringSelection(),
            key_length    = int(self.radioKeySize.GetStringSelection()),
            # subkey_type   = "RSA",
            # subkey_length = int(self.radioKeySize.GetStringSelection()),
            # subkey_usage  = "encrypt,sign,auth",
            name_real     = self.txtRealName.Value,
            name_email    = self.txtEmail.Value,
            name_comment  = comment,
            expire_date   = expiry,
            passphrase    = self.txtPassphrase.Value
        )
        print(input_data)
        return

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

