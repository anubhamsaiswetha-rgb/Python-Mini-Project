from abc import ABC, abstractmethod
class Notification(ABC):
    @abstractmethod
    def choose(self):
        pass
class Email(Notification):
    def choose(self):
        print("make an email")
class SMS(Notification):
    def choose(self):
        print("msg through SMS")
class WhatsApp(Notification):
    def choose(self):
        print("msg through Whatsapp")
e=Email()
s=SMS()
w=WhatsApp()

e.choose()
s.choose()
w.choose()