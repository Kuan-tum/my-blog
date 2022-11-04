import sys,time,os,random
import psycopg2
from PyQt5.QtWidgets import*
from PyQt5.QtGui import * 
from PyQt5.QtCore import *

__version__ = "2.0"


app =QApplication(sys.argv)


class Library(QMainWindow):
    """docstring for Library"""
    def __init__(self, parent=None):
        super(Library, self).__init__(parent)

        self.backgroundImages=images =os.listdir('files/backgroundImages')
        self.current_background_image =0 
        
        
        self._Background_loop()
        

        self.setWindowTitle("Learner For Life")
        self.setFixedSize(QSize(850,650))

        self.setFont(QFont("Aerial",11))
        self.toolBar = QToolBar(self)
        self.toolBar.setMovable(False)
        self.toolBar.setIconSize(QSize(40,40))
        self.toolBar.toggleViewAction().setEnabled(False)
        

        

        self.mainLayout =QGridLayout()
        
    
        self.mainWidget = QWidget()
        self.mainLabel()
        self.setSearchBar()
        self.setNewAuthorBar()
        self.setNewBookBar()
        self.setSettingsBar()
        

        

        self.mainLayout.addWidget(self.mainLabel(),0,0)

        
        self.mainWidget.setLayout(self.mainLayout)
        
        

        self.addToolBar(Qt.LeftToolBarArea,self.toolBar)
        self.setCentralWidget(self.mainWidget)
    def _Background_changer(self,current):
        self.current_background_image=current
        file='files/backgroundImages'
        current_image=file+"/"+self.backgroundImages[current].replace("jpg","JPG")
        background_style ="""Library{background-color:black;background-image:url(%s);background-repeat:no-repeat;background-position:center;}QToolBar{background:grey;spacing:20px}QStatusBar{background:rgb(128,0,150)}
                            """%current_image
        
        
       # print(self.backgroundImage)
        app.setStyleSheet(background_style)
        
        




        
    def _Background_loop(self):
        #self._Background_changer()
        self._Background_changer(random.randrange(len(self.backgroundImages)))
        timer=QTimer(self)
        timer.timeout.connect(lambda:self._Background_changer(random.randrange(len(self.backgroundImages))))
        timer.setInterval(50000)
        timer.start()
    def mainLabel(self):
        label = QLabel()
        label.setText("<font size=50 color=white><b>Library<b/><font/>")
        label.setAlignment(Qt.AlignLeft)
        #label.setGeometry(self.width()//2,0,100,100)
        #Library.layout(self).addWidget(label)
        return label 
    def setQuotesArea(self):
        TextArea = QTextBrowser()
        s = "<font color=blue><h1>welcome<h1/><font/>"
        TextArea.append(s)
        return TextArea
    def setNewAuthorBar(self):
        self.createBar("new author",self.addNewAuthor,"files/icons/author3.PNG")
        
    def createBar(self,barTitle,connect,icon=None):
        if icon:
            
            action = QAction(QIcon(icon),barTitle,self)
            action.triggered.connect(connect)
            self.toolBar.addAction(action)
        
    def addNewAuthor(self):
        print("added successifuly")
        self.statusBar().showMessage("author added successifully")
    def addNewBook(self):
        print("book added")
        self.statusBar().showMessage("book added successifully")
    def setNewBookBar(self):
        self.createBar("add new book",self.addNewBook,"files/icons/book6.PNG")
    def setSearchBar(self):
        self.createBar("search library",self.respondToSearch,'files/icons/search2.PNG')
    def respondToSearch(self):
        self.statusBar().showMessage("we are working on it......")
    def setSettingsBar(self):
        self.createBar("library settings",self.updateSettings,'files/icons/settings2.PNG')
    def updateSettings(self):
        self.statusBar().showMessage("welcome settings....")
    
    



    







"""background_style1 =Library{
                                background-image:url("files/library49.JPG");
                                background-repeat:no-repeat;
                                background-position:center;

                            }"""

if __name__ == '__main__':
    
    #app.setStyleSheet(background_style)
    lib = Library()
    lib.show() 
    #QTimer.singleShot(5000,lambda:app.setStyleSheet(background_style1))
    
    sys.exit(app.exec())
