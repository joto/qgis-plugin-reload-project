#!python
def classFactory(iface):
 from plugin import ReloadProjectPlugin
 return ReloadProjectPlugin(iface)
