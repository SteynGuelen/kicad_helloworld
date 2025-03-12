import pcbnew
import wx
from pathlib import Path

class hello_world(pcbnew.ActionPlugin):
    def defaults(self):
        # set the plugin path, resource directory and icon in toolbar
        plugin_dir = Path(__file__).resolve().parent 
        self.resources_dir = plugin_dir.parent.parent / "resources" / plugin_dir.name
        self.icon_file_name = str(self.resources_dir / "icon.png")
        self.show_toolbar_button = True

        # basic information about the plugin
        self.name = "Hello World"
        self.category = "Modify PCB"
        self.description = "An example plugin"

    def Run(self):
        board = pcbnew.GetBoard()

        # show a message box
        wx.MessageBox("Hello World!", "Hello!")
