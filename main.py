from utils.socket import ClientSocket
import kivy
kivy.require('2.1.0')
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.properties import StringProperty

client_socket = ClientSocket()
Builder.load_file("signals.kv")

class MainWindow(Widget):
    connection_state = StringProperty("Disconnected")
    def connect_to_server(self):
        try:
            client_socket.addr =  (self.ids.ip_input.text, int(self.ids.port_input.text),)
            client_socket.connect()
            self.connection_state = "Connected"
        except:
            self.connection_state = "Disconnected"

    def disconnect(self):
        client_socket.disconnect()
        self.connection_state = "Disconnected"

    def send_message(self, text):
        if self.connection_state == "Connected":
            client_socket.send(text)    
        
class SignalsApp(App):
    def build(self):
        return MainWindow()


if __name__ == '__main__':
    SignalsApp().run()