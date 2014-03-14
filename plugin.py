#!python
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
from urllib import *
import time
# initialize Qt resources from file resouces.py
import resources
class ReloadProjectPlugin:
  def __init__(self, iface):
    self.iface = iface
  def initGui(self):
    self.action = QAction(QIcon(":/plugins/ReloadProject/icon.png"), "Reload Project", self.iface.mainWindow())
    self.action.setEnabled(True);
    self.action.setWhatsThis("Reload project")
    self.action.setStatusTip("Reload project")
    self.action.triggered.connect(self.run)
    self.action.setShortcut(QKeySequence("Ctrl+r"))
    insert_before = self.iface.projectMenu().actions()[2]
    self.iface.projectMenu().insertAction(insert_before, self.action)
  def unload(self):
    self.iface.removeToolBarIcon(self.action)
  def run(self):
    self.extent = self.iface.mapCanvas().extent()
    filename = QgsProject.instance().fileName()
    if filename == '':
      self.iface.messageBar().pushMessage("Error", "Can't reload project because you don't have one", level=QgsMessageBar.CRITICAL)
    else:
      self.iface.projectRead.connect(self.set_extent)
      self.iface.addProject(filename)
  def set_extent(self):
    self.iface.mapCanvas().setExtent(self.extent)
    self.iface.projectRead.disconnect(self.set_extent)
