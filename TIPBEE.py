#!/usr/bin/python3

#!/usr/bin/python

"""
    The Isle Player Enumeration Engine
    Version 0.1.1
    By: Timothy Carlisle
    Description:
        This script is meant to simplify the analysis of the playerbase
        via FTP for The Isle game server administrators.
        TIPBEE.py is the main starting point.
        This product is copyrighted by Timothy Carlisle.
        Contact gwa2100@gmail.com with any questions.
"""
__title__ = 'The Isle Player Enumeration Engine'
__all__ = ['The Isle', 'console']
__version__ = '0.1.1'
__author__ = 'Timothy Carlisle'

import ftplib
import json
import tkinter
from tkinter import ttk
import os

class Tipbee:
    def __init__(self):
        self.dinoList = [
            "Anky",
            "AnkyJuv",
            "Austro",
            "AustroJuv",
            "Ava",
            "AvaJuv",
            "Camara",
            "Oro",
            "Taco",
            "Puerta",
            "PuertaJuv",
            "Shant",
            "ShantJuv",
            "Stego",
            "StegoJuv",
            "Theri",
            "TheriJuv",
            "Acro",
            "AcroJuv",
            "Albert",
            "Bary",
            "BaryJuv",
            "Herrera",
            "HerreraJuv",
            "Spino",
            "SpinoJuv",
            "Velo",
            "DiabloAdultS",
            "DiabloJuvS",
            "DiabloHatchS",
            "DryoAdultS",
            "DryoJuvS",
            "DryoHatchS",
            "GalliAdultS",
            "GalliJuvS",
            "GalliHatchS",
            "MaiaAdultS",
            "MaiaJuvS",
            "MaiaHatchS",
            "PachyAdultS",
            "PachyHatchS",
            "PachyJuvS",
            "ParaAdultS",
            "ParaJuvS",
            "ParaHatchS",
            "TrikeAdultS",
            "TrikeSubS",
            "TrikeJuvS",
            "TrikeHatchS",
            "AlloAdultS",
            "AlloJuvS",
            "AlloHatchS",
            "CarnoAdultS",
            "CarnoSubS",
            "CarnoJuvS",
            "CarnoHatchS",
            "CeratoAdultS",
            "CeratoJuvS",
            "CeratoHatchS",
            "DiloAdultS",
            "DiloJuvS",
            "DiloHatchS",
            "GigaAdultS",
            "GigaSubS",
            "GigaJuvS",
            "GigaHatchS",
            "SuchoAdultS",
            "SuchoHatchS",
            "SuchoJuvS",
            "RexAdultS",
            "RexSubS",
            "RexJuvS",
            "UtahAdultS",
            "UtahJuvS",
            "UtahHatchS"]
        # Core Objects
        self.top = tkinter.Tk()
        self.top.protocol("WM_DELETE_WINDOW", self.CatchShutdown)
        self.top.title(__title__ + " v" + __version__)

        self.top.geometry('900x640')
        self.serverIPEntryLabel = tkinter.Label(self.top, text="FTP IP:")
        self.serverIPEntryLabel.grid(column=0, row=0)
        self.serverIPEntry = tkinter.Entry(self.top, width=10)
        self.serverIPEntry.grid(column=1, row=0)

        self.serverPortEntryLabel = tkinter.Label(self.top, text="PORT:")
        self.serverPortEntryLabel.grid(column=2, row=0)
        self.serverPortEntry = tkinter.Entry(self.top, width=5)
        self.serverPortEntry.insert(tkinter.END, "21")
        self.serverPortEntry.grid(column=3, row=0)

        self.serverUsernameEntryLabel = tkinter.Label(self.top, text="USER:")
        self.serverUsernameEntryLabel.grid(column=4, row=0)
        self.serverUsername = tkinter.Entry(self.top, width=20)
        self.serverUsername.grid(column=5, row=0)

        self.serverPasswordEntryLabel = tkinter.Label(self.top, text="PASS:")
        self.serverPasswordEntryLabel.grid(column=6, row=0)
        self.serverPassword = tkinter.Entry(self.top, width=20, show="*")
        self.serverPassword.grid(column=7, row=0)

        # Configs
        self.ftpHostAddress = ""
        self.ftpHostPort = ""
        self.ftpUsername = ""
        self.ftpPassword = ""
        self.ftpUserFileDir = ""
        self.locations = [
            "Location_IslandV3",
            "Location_Thenyaw_Island",
            "DevTest"
        ]

        self.dinoCount = {}

        for x in self.dinoList:
            self.dinoCount[x] = 0

        # Startup check for ftp save file
        with open("config.dat", 'a+') as f:
            f.seek(0)
            try:
                data = json.load(f)
                self.ftpHostAddress = data['ftpHostAddress']
                self.ftpHostPort = data['ftpHostPort']
                self.ftpUsername = data['ftpUsername']
                self.ftpPassword = ""

                self.serverIPEntry.insert(tkinter.END, self.ftpHostAddress)
                self.serverPortEntry.insert(tkinter.END, self.ftpHostPort)
                self.serverPortEntry.delete(0, tkinter.END)
                if self.ftpHostPort == "":
                    self.serverPortEntry.insert(tkinter.END, "21")
                else:
                    self.serverPortEntry.insert(tkinter.END, self.ftpHostPort)
                self.serverUsername.insert(tkinter.END, self.ftpUsername)
            except TypeError:
                pass

            f.close()

        def MainLoop(self):
            self.top.mainloop()

        def ProcessUserFiles(self):
            files = ""
            self.ftpHostAddress = self.serverIPEntry.get()
            self.ftpHostPort = int(self.serverPortEntry.get())
            self.ftpUsername = self.serverUsername.get()
            self.ftpPassword = self.serverPassword.get()
            ftpObject = ftplib.FTP()
            ftpObject.connect(self.ftpHostAddress, self.ftpHostPort)
            ftpObject.login(self.ftpUsername, self.ftpPassword)
            ftpObject.cwd(self.ftpUserFileDir)
            try:
                files = ftpObject.nlst()
            except ftplib.error_perm:
                return ""
            for x in files:
                with open(x,'r') as f:
                    data = json.load(f)
                    if data['CharacterClass'] in self.dinoList:
                        self.dinoCount[data['CharacterClass']] += 1




