# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.aui

###########################################################################
## Class mainWindow
###########################################################################

class mainWindow ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"APPNAME", pos = wx.DefaultPosition, size = wx.Size( 887,600 ), style = wx.DEFAULT_FRAME_STYLE )

		self.SetSizeHints( wx.Size( 800,600 ), wx.DefaultSize )

		self.mainMenu = wx.MenuBar( 0 )
		self.menuFile = wx.Menu()
		self.mQuit = wx.MenuItem( self.menuFile, wx.ID_ANY, u"Quit"+ u"\t" + u"Q", wx.EmptyString, wx.ITEM_NORMAL )
		self.mQuit.SetBitmap( wx.Bitmap( u"ui/icons/exit.png", wx.BITMAP_TYPE_ANY ) )
		self.menuFile.Append( self.mQuit )

		self.mainMenu.Append( self.menuFile, u"File" )

		self.menuHelp = wx.Menu()
		self.mAbout = wx.MenuItem( self.menuHelp, wx.ID_ANY, u"About"+ u"\t" + u"A", wx.EmptyString, wx.ITEM_NORMAL )
		self.mAbout.SetBitmap( wx.Bitmap( u"ui/icons/info.png", wx.BITMAP_TYPE_ANY ) )
		self.menuHelp.Append( self.mAbout )

		self.mainMenu.Append( self.menuHelp, u"Help" )

		self.SetMenuBar( self.mainMenu )

		vSizer = wx.BoxSizer( wx.VERTICAL )

		vSizer.SetMinSize( wx.Size( 800,600 ) )
		self.m_auinotebook = wx.aui.AuiNotebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_NB_TOP )
		self.pPassword = wx.Panel( self.m_auinotebook, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		flexGridPassword = wx.FlexGridSizer( 6, 1, 0, 0 )
		flexGridPassword.AddGrowableCol( 0 )
		flexGridPassword.AddGrowableRow( 1 )
		flexGridPassword.AddGrowableRow( 2 )
		flexGridPassword.AddGrowableRow( 3 )
		flexGridPassword.AddGrowableRow( 4 )
		flexGridPassword.AddGrowableRow( 5 )
		flexGridPassword.SetFlexibleDirection( wx.BOTH )
		flexGridPassword.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

		lblAlphabet = wx.StaticBoxSizer( wx.StaticBox( self.pPassword, wx.ID_ANY, u"Alphabet" ), wx.HORIZONTAL )

		self.chkAlphabetMinor = wx.CheckBox( lblAlphabet.GetStaticBox(), wx.ID_ANY, u"a-z", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.chkAlphabetMinor.SetValue(True)
		lblAlphabet.Add( self.chkAlphabetMinor, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.chkAlphabetCapital = wx.CheckBox( lblAlphabet.GetStaticBox(), wx.ID_ANY, u"A-Z", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.chkAlphabetCapital.SetValue(True)
		lblAlphabet.Add( self.chkAlphabetCapital, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.chkAlphabetNumbers = wx.CheckBox( lblAlphabet.GetStaticBox(), wx.ID_ANY, u"0-9", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.chkAlphabetNumbers.SetValue(True)
		lblAlphabet.Add( self.chkAlphabetNumbers, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.chkAlphabetSpecial = wx.CheckBox( lblAlphabet.GetStaticBox(), wx.ID_ANY, u"!@#$", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.chkAlphabetSpecial.SetValue(True)
		lblAlphabet.Add( self.chkAlphabetSpecial, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		bSizer7.Add( lblAlphabet, 5, wx.EXPAND, 5 )


		bSizer7.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		lblLength = wx.StaticBoxSizer( wx.StaticBox( self.pPassword, wx.ID_ANY, u"Length" ), wx.VERTICAL )

		self.slideLength = wx.Slider( lblLength.GetStaticBox(), wx.ID_ANY, 10, 1, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_BOTH|wx.SL_HORIZONTAL|wx.SL_LABELS )
		lblLength.Add( self.slideLength, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer7.Add( lblLength, 5, wx.EXPAND, 5 )


		bSizer7.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		lblCount = wx.StaticBoxSizer( wx.StaticBox( self.pPassword, wx.ID_ANY, u"Count" ), wx.VERTICAL )

		self.slideCount = wx.Slider( lblCount.GetStaticBox(), wx.ID_ANY, 1, 1, 50, wx.DefaultPosition, wx.DefaultSize, wx.SL_BOTH|wx.SL_HORIZONTAL|wx.SL_LABELS )
		lblCount.Add( self.slideCount, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer7.Add( lblCount, 5, wx.EXPAND, 5 )


		bSizer7.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.btnGenPass = wx.Button( self.pPassword, wx.ID_ANY, u"Generate", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.btnGenPass, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		flexGridPassword.Add( bSizer7, 5, wx.ALL|wx.EXPAND, 5 )

		bSizer71 = wx.BoxSizer( wx.VERTICAL )

		sbSizer7 = wx.StaticBoxSizer( wx.StaticBox( self.pPassword, wx.ID_ANY, u"Password" ), wx.VERTICAL )

		self.m_textCtrl1 = wx.TextCtrl( sbSizer7.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.BORDER_SIMPLE )
		sbSizer7.Add( self.m_textCtrl1, 1, wx.EXPAND, 5 )


		bSizer71.Add( sbSizer7, 1, wx.EXPAND, 5 )


		flexGridPassword.Add( bSizer71, 10, wx.ALL|wx.EXPAND, 5 )


		self.pPassword.SetSizer( flexGridPassword )
		self.pPassword.Layout()
		flexGridPassword.Fit( self.pPassword )
		self.m_auinotebook.AddPage( self.pPassword, u"Password", False, wx.Bitmap( u"ui/icons/password.png", wx.BITMAP_TYPE_ANY ) )
		self.pCertificate = wx.Panel( self.m_auinotebook, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		flexGridCertificate = wx.FlexGridSizer( 10, 5, 5, 20 )
		flexGridCertificate.AddGrowableCol( 1 )
		flexGridCertificate.AddGrowableCol( 2 )
		flexGridCertificate.SetFlexibleDirection( wx.BOTH )
		flexGridCertificate.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		flexGridCertificate.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		flexGridCertificate.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )

		radioKeyTypeChoices = [ u"RSA and DSA", u"DSA and ElGamal", u"DSA (sign only)", u"RSA (sign only)" ]
		self.radioKeyType = wx.RadioBox( self.pCertificate, wx.ID_ANY, u"Key Type", wx.DefaultPosition, wx.DefaultSize, radioKeyTypeChoices, 2, wx.RA_SPECIFY_COLS )
		self.radioKeyType.SetSelection( 0 )
		bSizer10.Add( self.radioKeyType, 1, wx.EXPAND, 5 )

		radioKeySizeChoices = [ u"1024", u"2048", u"3072", u"4096" ]
		self.radioKeySize = wx.RadioBox( self.pCertificate, wx.ID_ANY, u"Key Size", wx.DefaultPosition, wx.DefaultSize, radioKeySizeChoices, 2, wx.RA_SPECIFY_COLS )
		self.radioKeySize.SetSelection( 3 )
		bSizer10.Add( self.radioKeySize, 1, wx.EXPAND, 5 )


		bSizer9.Add( bSizer10, 1, wx.EXPAND, 5 )

		lblRealName = wx.StaticBoxSizer( wx.StaticBox( self.pCertificate, wx.ID_ANY, u"Real name" ), wx.VERTICAL )

		self.txtRealName = wx.TextCtrl( lblRealName.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		lblRealName.Add( self.txtRealName, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer9.Add( lblRealName, 1, wx.EXPAND, 5 )

		lblEmail = wx.StaticBoxSizer( wx.StaticBox( self.pCertificate, wx.ID_ANY, u"Email address" ), wx.VERTICAL )

		self.txtEmail = wx.TextCtrl( lblEmail.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		lblEmail.Add( self.txtEmail, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer9.Add( lblEmail, 1, wx.EXPAND, 5 )

		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )

		lblExpiresChoices = [ u"Never", u"Custom" ]
		self.lblExpires = wx.RadioBox( self.pCertificate, wx.ID_ANY, u"Expires", wx.DefaultPosition, wx.DefaultSize, lblExpiresChoices, 1, wx.RA_SPECIFY_COLS )
		self.lblExpires.SetSelection( 1 )
		bSizer11.Add( self.lblExpires, 2, wx.EXPAND, 5 )

		lblCustomExpires = wx.StaticBoxSizer( wx.StaticBox( self.pCertificate, wx.ID_ANY, u"Custom expiry string" ), wx.VERTICAL )

		self.txtTimeQuanity = wx.TextCtrl( lblCustomExpires.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		lblCustomExpires.Add( self.txtTimeQuanity, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer11.Add( lblCustomExpires, 2, wx.EXPAND, 5 )


		bSizer9.Add( bSizer11, 1, wx.EXPAND, 5 )

		lblComment = wx.StaticBoxSizer( wx.StaticBox( self.pCertificate, wx.ID_ANY, u"Comment" ), wx.VERTICAL )

		self.txtEmail1 = wx.TextCtrl( lblComment.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		lblComment.Add( self.txtEmail1, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer9.Add( lblComment, 1, wx.EXPAND, 5 )

		lblPass = wx.StaticBoxSizer( wx.StaticBox( self.pCertificate, wx.ID_ANY, u"Passphrase" ), wx.HORIZONTAL )

		self.lblPassphrase = wx.StaticText( lblPass.GetStaticBox(), wx.ID_ANY, u"Passphrase", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblPassphrase.Wrap( -1 )

		lblPass.Add( self.lblPassphrase, 0, wx.ALL, 5 )

		self.txtPassphrase = wx.TextCtrl( lblPass.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		lblPass.Add( self.txtPassphrase, 2, 0, 5 )

		self.lblConfirm = wx.StaticText( lblPass.GetStaticBox(), wx.ID_ANY, u"Confirm", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblConfirm.Wrap( -1 )

		lblPass.Add( self.lblConfirm, 0, wx.ALL, 5 )

		self.txtConfirm = wx.TextCtrl( lblPass.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		lblPass.Add( self.txtConfirm, 2, 0, 5 )


		bSizer9.Add( lblPass, 1, wx.EXPAND, 5 )


		flexGridCertificate.Add( bSizer9, 10, wx.ALL|wx.EXPAND, 5 )


		flexGridCertificate.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer14.Add( ( 0, 0), 3, wx.EXPAND, 5 )

		bSizer13 = wx.BoxSizer( wx.VERTICAL )


		bSizer13.Add( ( 0, 0), 5, wx.EXPAND, 5 )

		self.btnGenKeyPair = wx.Button( self.pCertificate, wx.ID_ANY, u"Generate", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.btnGenKeyPair.SetBitmap( wx.Bitmap( u"ui/icons/solution.png", wx.BITMAP_TYPE_ANY ) )
		bSizer13.Add( self.btnGenKeyPair, 1, wx.EXPAND, 5 )


		bSizer13.Add( ( 0, 0), 5, wx.EXPAND, 5 )


		bSizer14.Add( bSizer13, 1, wx.EXPAND, 5 )


		bSizer14.Add( ( 0, 0), 3, wx.EXPAND, 5 )


		flexGridCertificate.Add( bSizer14, 1, wx.EXPAND, 5 )


		self.pCertificate.SetSizer( flexGridCertificate )
		self.pCertificate.Layout()
		flexGridCertificate.Fit( self.pCertificate )
		self.m_auinotebook.AddPage( self.pCertificate, u"GPG Keypair", False, wx.Bitmap( u"ui/icons/keys.png", wx.BITMAP_TYPE_ANY ) )
		self.pWallet = wx.Panel( self.m_auinotebook, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		self.m_auinotebook2 = wx.aui.AuiNotebook( self.pWallet, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel4 = wx.Panel( self.m_auinotebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer141 = wx.BoxSizer( wx.VERTICAL )


		bSizer141.Add( ( 0, 0), 2, wx.EXPAND, 5 )

		self.btnGenBTC = wx.Button( self.m_panel4, wx.ID_ANY, u"Generate", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer141.Add( self.btnGenBTC, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		bSizer141.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		lblBTCPubKey = wx.StaticBoxSizer( wx.StaticBox( self.m_panel4, wx.ID_ANY, u"Address" ), wx.VERTICAL )

		self.txtBTCPublicKey = wx.TextCtrl( lblBTCPubKey.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		lblBTCPubKey.Add( self.txtBTCPublicKey, 0, wx.EXPAND, 5 )


		bSizer141.Add( lblBTCPubKey, 1, wx.ALL|wx.EXPAND, 5 )

		lblBTCPrivateKey = wx.StaticBoxSizer( wx.StaticBox( self.m_panel4, wx.ID_ANY, u"Private key" ), wx.VERTICAL )

		self.txtBTCPrivateKey = wx.TextCtrl( lblBTCPrivateKey.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		lblBTCPrivateKey.Add( self.txtBTCPrivateKey, 0, wx.EXPAND, 5 )


		bSizer141.Add( lblBTCPrivateKey, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer141.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.btnBTCSave = wx.Button( self.m_panel4, wx.ID_ANY, u"Save As", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer141.Add( self.btnBTCSave, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		bSizer141.Add( ( 0, 0), 5, wx.EXPAND, 5 )


		self.m_panel4.SetSizer( bSizer141 )
		self.m_panel4.Layout()
		bSizer141.Fit( self.m_panel4 )
		self.m_auinotebook2.AddPage( self.m_panel4, u"Bitcoin", False, wx.Bitmap( u"ui/icons/bitcoin.png", wx.BITMAP_TYPE_ANY ) )
		self.m_panel5 = wx.Panel( self.m_auinotebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer1411 = wx.BoxSizer( wx.VERTICAL )


		bSizer1411.Add( ( 0, 0), 2, wx.EXPAND, 5 )

		self.btnGenETH = wx.Button( self.m_panel5, wx.ID_ANY, u"Generate", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1411.Add( self.btnGenETH, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		bSizer1411.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		lblETHPubKey1 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel5, wx.ID_ANY, u"Address" ), wx.VERTICAL )

		self.txtETHPubKey = wx.TextCtrl( lblETHPubKey1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		lblETHPubKey1.Add( self.txtETHPubKey, 0, wx.EXPAND, 5 )


		bSizer1411.Add( lblETHPubKey1, 1, wx.ALL|wx.EXPAND, 5 )

		lblETHPrivateKey = wx.StaticBoxSizer( wx.StaticBox( self.m_panel5, wx.ID_ANY, u"Private key" ), wx.VERTICAL )

		self.txtETHPrivateKey = wx.TextCtrl( lblETHPrivateKey.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		lblETHPrivateKey.Add( self.txtETHPrivateKey, 0, wx.EXPAND, 5 )


		bSizer1411.Add( lblETHPrivateKey, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer1411.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.btnETHSave = wx.Button( self.m_panel5, wx.ID_ANY, u"Save As", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1411.Add( self.btnETHSave, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		bSizer1411.Add( ( 0, 0), 5, wx.EXPAND, 5 )


		self.m_panel5.SetSizer( bSizer1411 )
		self.m_panel5.Layout()
		bSizer1411.Fit( self.m_panel5 )
		self.m_auinotebook2.AddPage( self.m_panel5, u"Ethereum", False, wx.Bitmap( u"ui/icons/ethereum.png", wx.BITMAP_TYPE_ANY ) )

		bSizer8.Add( self.m_auinotebook2, 1, wx.EXPAND |wx.ALL, 5 )


		self.pWallet.SetSizer( bSizer8 )
		self.pWallet.Layout()
		bSizer8.Fit( self.pWallet )
		self.m_auinotebook.AddPage( self.pWallet, u"Wallet", True, wx.Bitmap( u"ui/icons/wallet.png", wx.BITMAP_TYPE_ANY ) )

		vSizer.Add( self.m_auinotebook, 1, wx.ALL|wx.EXPAND, 5 )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )


		vSizer.Add( bSizer5, 1, wx.EXPAND, 5 )


		self.SetSizer( vSizer )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.AppExit, id = self.mQuit.GetId() )
		self.Bind( wx.EVT_MENU, self.AppAbout, id = self.mAbout.GetId() )
		self.btnGenPass.Bind( wx.EVT_BUTTON, self.btnGenPass_Click )
		self.lblExpires.Bind( wx.EVT_RADIOBOX, self.radioGPGExpiry_Click )
		self.btnGenKeyPair.Bind( wx.EVT_BUTTON, self.btnGPGGen_Click )
		self.btnGenBTC.Bind( wx.EVT_BUTTON, self.btnBTCGen_Click )
		self.btnBTCSave.Bind( wx.EVT_BUTTON, self.btnBTCSave_Click )
		self.btnGenETH.Bind( wx.EVT_BUTTON, self.btnETHGen_Click )
		self.btnETHSave.Bind( wx.EVT_BUTTON, self.btnETHSave_Click )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def AppExit( self, event ):
		pass

	def AppAbout( self, event ):
		pass

	def btnGenPass_Click( self, event ):
		pass

	def radioGPGExpiry_Click( self, event ):
		pass

	def btnGPGGen_Click( self, event ):
		pass

	def btnBTCGen_Click( self, event ):
		pass

	def btnBTCSave_Click( self, event ):
		pass

	def btnETHGen_Click( self, event ):
		pass

	def btnETHSave_Click( self, event ):
		pass


###########################################################################
## Class dlgAbout
###########################################################################

class dlgAbout ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"About", pos = wx.DefaultPosition, size = wx.Size( 500,376 ), style = wx.CAPTION )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		gSizer3 = wx.GridSizer( 1, 2, 0, 0 )

		self.m_bitmap3 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"ui/icons/icon.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_bitmap3, 0, wx.ALL, 5 )

		self.txtAppName = wx.StaticText( self, wx.ID_ANY, u"APPNAME", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.txtAppName.Wrap( -1 )

		self.txtAppName.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		gSizer3.Add( self.txtAppName, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM, 5 )


		bSizer4.Add( gSizer3, 1, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND|wx.SHAPED, 5 )

		self.lblAppDescription = wx.StaticText( self, wx.ID_ANY, u"AppDescription", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.lblAppDescription.Wrap( -1 )

		bSizer4.Add( self.lblAppDescription, 0, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 4, wx.EXPAND, 5 )

		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		self.btnOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.btnOK, 0, wx.ALL, 5 )


		bSizer5.Add( ( 25, 0), 1, wx.EXPAND, 5 )

		self.btnCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.btnCancel, 0, wx.ALL, 5 )


		bSizer4.Add( bSizer5, 1, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.FIXED_MINSIZE, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btnOK.Bind( wx.EVT_BUTTON, self.btnOK_Click )
		self.btnCancel.Bind( wx.EVT_BUTTON, self.btnCancel_Click )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btnOK_Click( self, event ):
		pass

	def btnCancel_Click( self, event ):
		pass


