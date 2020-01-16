#!/usr/bin/env python
import wx
import sys, os
import win32api
from win32con import AW_ACTIVATE, AW_BLEND, AW_CENTER, AW_HIDE, AW_HOR_NEGATIVE, AW_HOR_POSITIVE, AW_SLIDE, AW_VER_NEGATIVE, AW_VER_POSITIVE,SPI_GETWORKAREA
from ctypes import windll, c_int


APP_TITLE = u'TDL'
APP_ICON = './favicon.ico'

class mainFrame(wx.Frame):
    '''程序主窗口类，继承自wx.Frame'''
    
    id_open = wx.NewId()
    id_save = wx.NewId()
    id_quit = wx.NewId()
    
    id_help = wx.NewId()
    id_about = wx.NewId()
    
    def __init__(self, parent):
        '''构造函数'''

        wx.Frame.__init__(self, parent, id=-1, title=APP_TITLE)
        workarea = win32api.GetMonitorInfo(1)['Work']
        print(workarea)
        pos=(workarea[2]-280,workarea[3]-180)
        print(pos)
        self.SetBackgroundColour(wx.Colour(224, 224, 224))
        self.SetSize((200, 150))
        self.SetMaxSize((200, 150))
        self.SetPosition(pos)
        # self.Center()
        
        if hasattr(sys, "frozen") and getattr(sys, "frozen") == "windows_exe":
            icon = wx.Icon(APP_ICON, wx.BITMAP_TYPE_ICO)
        else :
            icon = wx.Icon(APP_ICON, wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon)
        
        # self.Maximize() # 左上角
        # 控制最大化，最小化按钮
        self.SetWindowStyle(wx.DEFAULT_FRAME_STYLE^(wx.RESIZE_BORDER|wx.MAXIMIZE_BOX|wx.MINIMIZE_BOX|wx.CLOSE_BOX))

        # AW_SLIDE 使用滑动类型。缺省为滚动类型。使用AW_CENTER标志时被忽略
        # AW_VER_NEGATIVE 自下向上显示窗口。该标志可以在滚动动画和滑动动画中使用。当使用AW_CENTER标志时，该标志将被忽略
        # AW_ACTIVATE 激活窗口。在使用了AW_HIDE标志后不能使用这个标志
        flags = AW_SLIDE | AW_VER_NEGATIVE | AW_ACTIVATE
        windll.user32.AnimateWindow(c_int(self.GetHandle()), c_int(600), c_int(flags)) # 淡入淡出
        self.Refresh() # 底部淡出
        # self.Bind(wx.EVT_CLOSE,self.RemovePopup)

        ws = wx.WrapSizer()

        inputText = wx.TextCtrl(self, -1, u'', size=(175, -1), style=wx.TE_MULTILINE|wx.TE_PROCESS_ENTER)  
        inputText.SetInsertionPoint(0)
        inputText.SetFocus()
        ws.Add(inputText)
        self.Bind(wx.EVT_TEXT_ENTER, self.submit)
        
        # self._CreateMenuBar()         # 菜单栏
        # self._CreateToolBar()         # 工具栏
        # self._CreateStatusBar()       # 状态栏
    def submit(self, params):
        print(params)

    def _CreateMenuBar(self):
        '''创建菜单栏'''
        
        self.mb = wx.MenuBar()
        
        # 文件菜单
        m = wx.Menu()
        m.Append(self.id_open, u"打开文件")
        m.Append(self.id_save, u"保存文件")
        m.AppendSeparator()
        m.Append(self.id_quit, u"退出系统")
        self.mb.Append(m, u"文件")
        
        self.Bind(wx.EVT_MENU, self.OnOpen, id=self.id_open)
        self.Bind(wx.EVT_MENU, self.OnSave, id=self.id_save)
        self.Bind(wx.EVT_MENU, self.OnQuit, id=self.id_quit)
        
        # 帮助菜单
        m = wx.Menu()
        m.Append(self.id_help, u"帮助主题")
        m.Append(self.id_about, u"关于...")
        self.mb.Append(m, u"帮助")
        
        self.Bind(wx.EVT_MENU, self.OnHelp,id=self.id_help)
        self.Bind(wx.EVT_MENU, self.OnAbout,id=self.id_about)
        
        self.SetMenuBar(self.mb)
    
    def _CreateToolBar(self):
        '''创建工具栏'''
        
        # bmp_open = wx.Bitmap('res/open_16.png', wx.BITMAP_TYPE_ANY) # 请自备按钮图片
        # bmp_save = wx.Bitmap('res/save_16.png', wx.BITMAP_TYPE_ANY) # 请自备按钮图片
        # bmp_help = wx.Bitmap('res/help_16.png', wx.BITMAP_TYPE_ANY) # 请自备按钮图片
        # bmp_about = wx.Bitmap('res/about_16.png', wx.BITMAP_TYPE_ANY) # 请自备按钮图片
        bmp_open = wx.Bitmap(APP_ICON, wx.BITMAP_TYPE_ANY) # 请自备按钮图片
        bmp_save = wx.Bitmap(APP_ICON, wx.BITMAP_TYPE_ANY) # 请自备按钮图片
        bmp_help = wx.Bitmap(APP_ICON, wx.BITMAP_TYPE_ANY) # 请自备按钮图片
        bmp_about = wx.Bitmap(APP_ICON, wx.BITMAP_TYPE_ANY) # 请自备按钮图片
        
        self.tb = wx.ToolBar(self)
        self.tb.SetToolBitmapSize((16,16))
        
        self.tb.AddLabelTool(self.id_open, u'打开文件', bmp_open, shortHelp=u'打开', longHelp=u'打开文件')
        self.tb.AddLabelTool(self.id_save, u'保存文件', bmp_save, shortHelp=u'保存', longHelp=u'保存文件')
        self.tb.AddSeparator()
        self.tb.AddLabelTool(self.id_help, u'帮助', bmp_help, shortHelp=u'帮助', longHelp=u'帮助')
        self.tb.AddLabelTool(self.id_about, u'关于', bmp_about, shortHelp=u'关于', longHelp=u'关于...')
        
        #self.Bind(wx.EVT_TOOL_RCLICKED, self.OnOpen, id=self.id_open)
        
        self.tb.Realize()
    
    def _CreateStatusBar(self):
        '''创建状态栏'''
        
        self.sb = self.CreateStatusBar()
        self.sb.SetFieldsCount(3)
        self.sb.SetStatusWidths([-2, -1, -1])
        self.sb.SetStatusStyles([wx.SB_RAISED, wx.SB_RAISED, wx.SB_RAISED])
        
        self.sb.SetStatusText(u'状态信息0', 0)
        self.sb.SetStatusText(u'', 1)
        self.sb.SetStatusText(u'状态信息2', 2)
    
    def OnOpen(self, evt):
        '''打开文件'''
        
        self.sb.SetStatusText(u'打开文件', 1)
    
    def OnSave(self, evt):
        '''保存文件'''
        
        self.sb.SetStatusText(u'保存文件', 1)
    
    def OnQuit(self, evt):
        '''退出系统'''
        
        self.sb.SetStatusText(u'退出系统', 1)
        self.Destroy()
    
    def OnHelp(self, evt):
        '''帮助'''
        
        self.sb.SetStatusText(u'帮助', 1)
    
    def OnAbout(self, evt):
        '''关于'''
        
        self.sb.SetStatusText(u'关于', 1)
        
class mainApp(wx.App):
    def OnInit(self):
        self.SetAppName(APP_TITLE)
        self.Frame = mainFrame(None)
        self.Frame.Show()
        return True

if __name__ == "__main__":
    app = mainApp()
    app.MainLoop()