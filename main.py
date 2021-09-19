from dotenv            import load_dotenv, main
from wx.core           import ICON_QUESTION, EmptyString, Font
from ui.gui            import mainWindow,dlgAbout
from ctypes            import windll
from secrets           import choice,randbits
from sys               import platform
from Crypto.PublicKey  import RSA, DSA, ECC
import os, wx, string
import lib.genbtc, lib.geneth

load_dotenv('./config/.env')

MB_OK       = 0x0
MB_OKCXL    = 0x01
MB_YESNOCXL = 0x03
MB_YESNO    = 0x04
MB_HELP     = 0x4000
ICON_EXLAIM = 0x30
ICON_INFO   = 0x40
ICON_STOP   = 0x10
IDYES = 6
IDNO = 7
IDCANCEL = 2


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

    def btnKeyGen_Click( self, event ):
        gen_without_passphrase = False
        secret = self.txtPassphrase.Value

        if self.txtPassphrase.Value != self.txtConfirm.Value: 
            windll.user32.MessageBoxW(0, "Passphrase does not match confirmation", f"{os.getenv('APPNAME')}", 0 ) 
            return
        if self.txtPassphrase.Value == EmptyString and self.txtConfirm.Value == EmptyString: 
            windll.user32.MessageBoxW(0, "Generating key pair without a passphrase", f"{os.getenv('APPNAME')}", 0 ) 
            gen_without_passphrase = True

        self.btnGenKeyPair.Enabled = False
        self.btnGenKeyPair.SetLabelText("Please wait...")
        algo = self.radioKeyType.GetStringSelection()

        key = None
        if algo=="RSA":
            key = RSA.generate(
                bits=int(self.radioKeySize.GetStringSelection()),
                e=65537
            )
        elif algo=="DSA":
            key = DSA.generate(
                bits=int(self.radioKeySize.GetStringSelection())
            )


        #Private key
        enc_private_key = None
        if gen_without_passphrase == True:
            if algo=="RSA":
                enc_private_key = key.export_key(pkcs=1)
            if algo=="DSA":
                enc_private_key = key.export_key(pkcs8=False)
        else:
            if algo=="RSA":
                enc_private_key = key.export_key(passphrase=secret, pkcs=1)
            if algo=="DSA":
                enc_private_key = key.export_key(passphrase=secret, pkcs8=False)


        #Public key
        public_key  = None
        if algo=="RSA":
            public_key  = key.publickey().export_key()
        if algo=="DSA":
            public_key  = key.publickey().export_key()


        save_file = ''.join(choice(string.ascii_uppercase) for _ in range(16))
        with open(f"{os.environ['USERPROFILE']}\Desktop\PRVKEY_{algo}_{save_file}", 'wb') as f:
            f.write(enc_private_key)
        with open(f"{os.environ['USERPROFILE']}\Desktop\PUBKEY_{algo}_{save_file}.pub", 'wb') as f:
            f.write(public_key)

        self.btnGenKeyPair.SetLabelText("Generate")
        self.btnGenKeyPair.Enabled = True
        windll.user32.MessageBoxW(0, 
        f"The following files were generated:\n{os.environ['USERPROFILE']}\Desktop\PRVKEY_{algo}_{save_file}\n{os.environ['USERPROFILE']}\Desktop\PUBKEY_{algo}_{save_file}.pub", 
        f"Success", 
        0) 

        
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

