#!/usr/bin/env python
#Boa:App:BoaApp

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
import wx

import Frame1

modules ={'Frame1': [1, u'Main frame of Application', u'Frame1.py']}

class BoaApp(wx.App):
    def OnInit(self):
        wx.InitAllImageHandlers()
        self.main = Frame1.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

def main():
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
