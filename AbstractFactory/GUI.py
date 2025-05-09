import abc

class GUI(abc.ABC):
    """Abstract GUI class"""
    __metaclass__ = abc.ABCMeta
    @abc.abstractmethod
    def create_button(self):
        """Create a button"""
        pass
    
    @abc.abstractmethod
    def create_checkbox(self):
        """Create a checkbox"""
        pass
    
class Button(abc.ABC):
    """Abstract Button class"""
    __metaclass__ = abc.ABCMeta
    @abc.abstractmethod
    def point(self):
        """Point to the button"""
        pass
    
class CheckBox(abc.ABC):
    """Abstract CheckBox class"""
    __metaclass__ = abc.ABCMeta
    @abc.abstractmethod
    def point(self):
        """Check the checkbox"""
        pass
    
class WindowsGUI(GUI):
    """Windows GUI class"""
    def create_button(self):
        """Create a Windows button"""
        return WindowsButton()
    
    def create_checkbox(self):
        """Create a Windows checkbox"""
        return WindowsCheckBox()
    
class WindowsButton(Button):
    """Windows Button class"""
    def point(self):
        """Point to the Windows button"""
        print("Pointing to Windows button")
        return
    
class WindowsCheckBox(CheckBox):
    """Windows CheckBox class"""
    def point(self):
        """Point to the Windows checkbox"""
        print("Pointing to Windows checkbox")
        return
    
class MacOSGUI(GUI):
    """MacOS GUI class"""
    def create_button(self):
        """Create a MacOS button"""
        return MacOSButton()
    
    def create_checkbox(self):
        """Create a MacOS checkbox"""
        return MacOSCheckBox()

class MacOSButton(Button):
    """MacOS Button class"""
    def point(self):
        """Point to the MacOS button"""
        print("Pointing to MacOS button")
        return
    
class MacOSCheckBox(CheckBox):
    """MacOS CheckBox class"""
    def point(self):
        """Point to the MacOS checkbox"""
        print("Pointing to MacOS checkbox")
        return
    
class Application():
    """Application class"""
    def __init__(self, gui):
        self.gui = gui
    
    def run(self):
        """Run the application"""
        button = self.gui.create_button()
        checkbox = self.gui.create_checkbox()
        
        # Point to the button and checkbox
        button.point()
        checkbox.point()
        return
    
# Example usage
if __name__ == "__main__":
    # Create a Windows GUI
    windows_gui = WindowsGUI()
    app = Application(windows_gui)
    app.run()
    
    # Create a MacOS GUI
    macos_gui = MacOSGUI()
    app = Application(macos_gui)
    app.run()