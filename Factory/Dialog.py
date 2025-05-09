import abc

class Dialog(abc.ABC):
    __metaclass__ = abc.ABCMeta
    def render(self):
        """Render the dialog"""
        button = self.create_button()   
        button.onclick()
        button.render(self.closeDialog)
         
    @abc.abstractmethod
    def create_button(self):
        """Create a button"""
        return
    
    def closeDialog(self):
        """Close the dialog"""
        print("Dialog closed")
        return

class Button(abc.ABC):
    __metaclass__ = abc.ABCMeta
    def render(self, f):
        """Render the button"""
        print("Button rendered")
        self.onclick = f
        return
    
    @abc.abstractmethod
    def onclick(self):
        """Button click event"""
        return
    
class WindowsDialog(Dialog):
    def create_button(self):
        """Create a Windows button"""
        return WindowsButton()
    
class WindowsButton(Button):
    def onclick(self):
        """Windows button click event"""
        print("Windows button clicked")
        return

class WebDialog(Dialog):
    def create_button(self):
        """Create a Web button"""
        return WebButton()
    
class WebButton(Button):
    def onclick(self):
        """Web button click event"""
        print("Web button clicked")
        return
    
class Application():
    def __init__(self, dialog):
        self.dialog = dialog
    
    def run(self):
        """Run the application"""
        self.dialog.render()
        return
    
if __name__ == "__main__":
    # Create a Windows dialog
    windows_dialog = WindowsDialog()
    app = Application(windows_dialog)
    app.run()
    
    # Create a Web dialog
    web_dialog = WebDialog()
    app = Application(web_dialog)
    app.run()