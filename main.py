from cmath import log
import random
from dotenv             import load_dotenv, main
from wx.core            import ICON_QUESTION, EmptyString, Font
from ui.gui             import mainWindow,dlgAbout
from ctypes             import windll
from secrets            import choice,randbits
from sys                import platform
from Crypto.PublicKey   import RSA, DSA, ECC
from Crypto.Hash        import SHA1, SHA256, SHA512, SHA3_256, SHA3_512, MD5
from fastcrc            import crc32, crc64

from tkinter            import Tk
from tkinter.filedialog import askopenfilename

import os, wx, string, rstr, ftfy
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
        
        self.passphrase_lang = ""
        self.hash_this_file  = None

    def AppExit(self, event):
        self.Destroy()

    def AppAbout( self, event ):
        DLGAbout(self)

    def btnGenPass_Click( self, event ):
        #Get generation boundaries
        dict = ""
        pattern = self.txtPattern.Value
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
        if  not dict: windll.user32.MessageBoxW(0, "Dictionary cannot be empty", f"{os.getenv('APPNAME')}", 0 )
        
        if passLength <= 0:  windll.user32.MessageBoxW(0, f"Password length cannot be <= {passLength}", f"{os.getenv('APPNAME')}", 0 )
        if passLength >1000: windll.user32.MessageBoxW(0, f"Password length cannot be  > {passLength}", f"{os.getenv('APPNAME')}", 0 )
        if passCount  <= 0:  windll.user32.MessageBoxW(0, f"Password  count cannot be <= {passCount}", f"{os.getenv('APPNAME')}", 0 ) 
        if passCount   >50:  windll.user32.MessageBoxW(0, f"Password  count cannot be  > {passCount}", f"{os.getenv('APPNAME')}", 0 ) 

        #Generation
        passBuffer = []

        if pattern != ".*":
            for i in range(passCount): passBuffer.append(rstr.xeger(pattern))
        else:
            for i in range(passCount): passBuffer.append(''.join([choice(dict) for _ in range(passLength)]))

        self.m_textCtrl1.SetFont(Font(10, wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, underline=False, faceName="sans-serif", encoding=wx.FONTENCODING_DEFAULT))
        self.m_textCtrl1.Value = '\n'.join(passBuffer)

    def btnResetPattern_Click(self, event):
         self.txtPattern.Value = ".*"
         pattern = self.txtPattern.Value

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

    def dictChooser_Change(self, event):
        self.passphrase_lang = self.dictChooser.GetString(self.dictChooser.GetCurrentSelection())

    def btnGenPassphrase_Click(self, event):
        if self.passphrase_lang == "": self.passphrase_lang = self.dictChooser.GetString(self.dictChooser.GetCurrentSelection())
        wordCount = self.slideLengthPassphrase.GetValue()

        passBuffer = []
        with open(f"./res/{str.lower(self.passphrase_lang)}-words.txt", 'r') as f:
            lines      = f.readlines()
            passBuffer = list(map(lambda x: str.replace(x,'\n',' '), random.sample(lines,k=wordCount)))
            f.close()

        passBuffer[-1] = str.replace(passBuffer.pop(), ' ', '')
        self.txtGenPassphrase.SetFont(Font(10, wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, underline=False, faceName="sans-serif", encoding=wx.FONTENCODING_DEFAULT))
        self.txtGenPassphrase.Value = ftfy.fix_encoding(''.join(passBuffer))

    def btnBrowseFileForHashing_Click(self, event):
        Tk().withdraw()
        select_file = askopenfilename()
        if(select_file == ""): return None
        self.hash_this_file = select_file
        select_file = os.path.basename(select_file)
        if(len(select_file) >= 75): select_file = '...'+select_file[65:] 
        self.lblSelectedFile.SetLabelText(select_file)

    def btnHashToFile_Click(self, event):
            def saveFileHash(h):
                if(self.hash_this_file == None): return None
                fo = 'w+'
                fn  = os.path.basename(self.hash_this_file)
                with open(self.hash_this_file, 'rb') as f:
                    data    = f.read()   
                    with open(os.path.realpath(self.hash_this_file) + f'.{h}', fo) as s:
                        if(h == 'md5'):       s.write(str.upper(MD5.new(data=data).hexdigest()) + "  MD5")
                        if(h == 'crc32'):     s.write(str.upper(str(hex(crc32.iso_hdlc(data)))[2:]) + "  CRC32")
                        if(h == 'crc64'):     s.write(str.upper((hex(crc64.xz(data)))[2:]) + "  CRC64")
                        if(h == 'sha1'):      s.write(str.upper(SHA1.new(data=data).hexdigest()) + "  SHA1")
                        if(h == 'sha256'):    s.write(str.upper(SHA256.new(data=data).hexdigest()) + "  SHA256")
                        if(h == 'sha512'):    s.write(str.upper(SHA512.new(data=data).hexdigest()) + "  SHA512")
                        if(h == 'sha3-256'):  s.write(str.upper(SHA3_256.new(data=data).hexdigest()) + "  SHA3-256")
                        if(h == 'sha3-512'):  s.write(str.upper(SHA3_512.new(data=data).hexdigest()) + "  SHA3-512")
            saved = ""
            if(self.chkMD5.IsChecked() == True):    
                saveFileHash('md5')
                saved += f'\n{os.path.abspath(self.hash_this_file)}.md5'
            if(self.chkCRC32.IsChecked() == True):  
                saveFileHash('crc32')
                saved += f'\n{os.path.abspath(self.hash_this_file)}.crc32'
            if(self.chkCRC64.IsChecked() == True):  
                saveFileHash('crc64')
                saved += f'\n{os.path.abspath(self.hash_this_file)}.crc64'
            if(self.chkSHA1.IsChecked() == True):   
                saveFileHash('sha1')
                saved += f'\n{os.path.abspath(self.hash_this_file)}.sha1' 
            if(self.chkSHA256.IsChecked() == True): 
                saveFileHash('sha256')
                saved += f'\n{os.path.abspath(self.hash_this_file)}.sha256'          
            if(self.chkSHA512.IsChecked() == True): 
                saveFileHash('sha512')
                saved += f'\n{os.path.abspath(self.hash_this_file)}.sha512'
            if(self.chkSHA3256.IsChecked() == True):
                saveFileHash('sha3-256')
                saved += f'\n{os.path.abspath(self.hash_this_file)}.sha3-256'
            if(self.chkSHA3512.IsChecked() == True):
                saveFileHash('sha3-512')
                saved += f'\n{os.path.abspath(self.hash_this_file)}.sha3-512'   
            windll.user32.MessageBoxW(0, 
            f"Generated:\n{saved}", 
            f"Success", 
            0)      

    def btnGenHash_Click(self, event):
        self.txtHashOutput.Value = ""
        if(self.hash_this_file is None):
            return None
        with open(self.hash_this_file, 'rb') as f:
            data    = f.read()
            self.txtHashOutput.Value += f'---------------------------------------------------------'
            if(self.chkMD5.IsChecked() == True):
                self.txtHashOutput.Value += f'\nMD5:      '+ str.upper(MD5.new(data=data).hexdigest())
            if(self.chkCRC32.IsChecked() == True):
                self.txtHashOutput.Value += f'\nCRC32:    '+ str.upper(str(hex(crc32.iso_hdlc(data)))[2:])
            if(self.chkCRC64.IsChecked() == True):
                self.txtHashOutput.Value += f'\nCRC64:    '+ str.upper((hex(crc64.xz(data)))[2:])
            if(self.chkSHA1.IsChecked() == True):
                self.txtHashOutput.Value += f'\nSHA-1:    '+ str.upper(SHA1.new(data=data).hexdigest())
            if(self.chkSHA256.IsChecked() == True):
                self.txtHashOutput.Value += f'\nSHA-256:  '+ str.upper(SHA256.new(data=data).hexdigest())
            if(self.chkSHA512.IsChecked() == True):
                self.txtHashOutput.Value += f'\nSHA-512:  '+ str.upper(SHA512.new(data=data).hexdigest())
            if(self.chkSHA3256.IsChecked() == True):
                self.txtHashOutput.Value += f'\nSHA3-256: '+ str.upper(SHA3_256.new(data=data).hexdigest())
            if(self.chkSHA3512.IsChecked() == True):        
                self.txtHashOutput.Value += f'\nSHA3-512: '+ str.upper(SHA3_512.new(data=data).hexdigest())
            self.txtHashOutput.Value += f'---------------------------------------------------------'

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

