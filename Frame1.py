#Boa:Frame:Frame1
# pajekpart-gui - a gui for pajekpart
#
#  Copyright (c) 2005 Ryszard Szopa
#
#  Author: Ryszard Szopa <ryszard (dot) szopa (at) gmail (dot) com>
#              http://szopa.tasak.gda.pl/
#              http://szopa.wordpress.com/
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License as
#  published by the Free Software Foundation; either version 2 of the
#  License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307
#  USA
import wx, pajekpart, sys


def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1CATTEXTCTRL, wxID_FRAME1CREATEBUTTON, 
 wxID_FRAME1NETTEXTCTRL, wxID_FRAME1OPENCATBUTTON, wxID_FRAME1OPENNETBUTTON, 
 wxID_FRAME1OUTPUTFILEBUTTON, wxID_FRAME1OUTPUTFILETEXTCTRL, 
] = [wx.NewId() for _init_ctrls in range(8)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(548, 281), size=wx.Size(448, 196),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Pajek partition creator')
        self.SetClientSize(wx.Size(448, 196))

        self.openNetButton = wx.Button(id=wxID_FRAME1OPENNETBUTTON,
              label=u'Open NET file...', name=u'openNetButton', parent=self,
              pos=wx.Point(16, 24), size=wx.Size(120, 34), style=0)
        self.openNetButton.Bind(wx.EVT_BUTTON, self.OnOpenNetButton,
              id=wxID_FRAME1OPENNETBUTTON)

        self.openCatButton = wx.Button(id=wxID_FRAME1OPENCATBUTTON,
              label=u'Open CAT file...', name=u'openCatButton', parent=self,
              pos=wx.Point(16, 70), size=wx.Size(120, 34), style=0)
        self.openCatButton.Bind(wx.EVT_BUTTON, self.onOpenCatButton,
              id=wxID_FRAME1OPENCATBUTTON)

        self.netTextCtrl = wx.TextCtrl(id=wxID_FRAME1NETTEXTCTRL,
              name=u'netTextCtrl', parent=self, pos=wx.Point(152, 24),
              size=wx.Size(280, 27), style=0, value=u'')

        self.catTextCtrl = wx.TextCtrl(id=wxID_FRAME1CATTEXTCTRL,
              name=u'catTextCtrl', parent=self, pos=wx.Point(152, 72),
              size=wx.Size(280, 27), style=0, value=u'')

        self.outputFileButton = wx.Button(id=wxID_FRAME1OUTPUTFILEBUTTON,
              label=u'Output file...', name=u'outputFileButton', parent=self,
              pos=wx.Point(16, 116), size=wx.Size(120, 34), style=0)
        self.outputFileButton.Bind(wx.EVT_BUTTON, self.OnOutputFileButton,
              id=wxID_FRAME1OUTPUTFILEBUTTON)

        self.outputFileTextCtrl = wx.TextCtrl(id=wxID_FRAME1OUTPUTFILETEXTCTRL,
              name=u'outputFileTextCtrl', parent=self, pos=wx.Point(152, 120),
              size=wx.Size(280, 27), style=0, value=u'')

        self.CreateButton = wx.Button(id=wxID_FRAME1CREATEBUTTON,
              label=u'Create partition', name=u'CreateButton', parent=self,
              pos=wx.Point(280, 157), size=wx.Size(152, 34), style=0)
        self.CreateButton.Bind(wx.EVT_BUTTON, self.OnCreateButton,
              id=wxID_FRAME1CREATEBUTTON)

    def __init__(self, parent):
        self._init_ctrls(parent)

        
    def OnOpenNetButton(self, event):
        dlg = wx.FileDialog(self, "Choose a file", ".", "", "*.net", wx.OPEN)
        try:
            if dlg.ShowModal() == wx.ID_OK:
                filename = dlg.GetPath()
                # your code
                self.netTextCtrl.SetValue(filename)
        finally:
            dlg.Destroy()

    def onOpenCatButton(self, event):
        dlg = wx.FileDialog(self, "Choose a file", ".", "", "*.cat", wx.OPEN)
        try:
            if dlg.ShowModal() == wx.ID_OK:
                filename = dlg.GetPath()
                # Your code
                self.catTextCtrl.SetValue(filename)
        finally:
            dlg.Destroy()
        
        #event.Skip()

    def OnOutputFileButton(self, event):
        dlg = wx.FileDialog(self, "Choose a file", ".", "", "*.clu", wx.SAVE)
        try:
            if dlg.ShowModal() == wx.ID_OK:
                filename = dlg.GetPath()
                # Your code
                self.outputFileTextCtrl.SetValue(filename)
        finally:
            dlg.Destroy()
        
        #event.Skip()
    def OnCreateButton(self, event):
        try:
            outputFilename = self.outputFileTextCtrl.GetValue()
            sys.stdout = open(outputFilename, "w")
            # the filename without the extension
            logFilename = ''.join(outputFilename.split('.')[:-1])+'.log'
            log = open(logFilename, "w")
            
            print >> log, "This is pajekpart, a Pajek partition maker, version %s (%s)."%(pajekpart.__version__, pajekpart.__date__)
            print >> log, "(c) 2006 Ryszard Szopa."
            
            nodesFilename = self.netTextCtrl.GetValue()
            categoriesFilename = self.catTextCtrl.GetValue()
            nodes = pajekpart.importNodesFromNet(nodesFilename)
            category, categories = pajekpart.importCategories(categoriesFilename)
            
            partition = pajekpart.makePartition(nodes, category, categories, log)
            
            
           
            

            
            print "*Vertices %s \r\n"%(len(partition))
            for i in partition:
                print  i
                
            message = "Saved partition to file %s. Saved log file to %s. There were %s nodes in the net."%(outputFilename, logFilename, str(len(partition)))
            
            print >> log, message
               
            sys.stdout.close()
            log.close()
            
            
            dlg = wx.MessageDialog(self, message,
              'Success', wx.OK | wx.ICON_INFORMATION)
            try:
                dlg.ShowModal()
            finally:
                dlg.Destroy()
        
        except pajekpart.NoFilesError, inst:
            message = inst.value
            dlg = wx.MessageDialog(self, message,
              'Error', wx.OK | wx.ICON_INFORMATION)
            try:
                dlg.ShowModal()
            finally:
                dlg.Destroy()
                
        except IOError, (errno, strerror):
            message  = "You haven't specified an output file or there's another I/O error."
            dlg = wx.MessageDialog(self, message,
              'Error', wx.OK | wx.ICON_INFORMATION)
            try:
                dlg.ShowModal()
            finally:
                dlg.Destroy()
        except pajekpart.NoFilesError, inst:
            message = inst.value
            dlg = wx.MessageDialog(self, message,
              'Error', wx.OK | wx.ICON_INFORMATION)
            try:
                dlg.ShowModal()
            finally:
                dlg.Destroy()
            
            
        

            
        #event.Skip()
