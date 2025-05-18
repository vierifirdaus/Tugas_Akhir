from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self):
        pass

class Email(Notification):
    def send(self):  # Polymorphism
        print("Sending email")

class SMS(Notification):
    def send(self):  # Polymorphism
        print("Sending SMS")

# Usage
notifications = [Email(), SMS()]
for notify in notifications:
    notify.send()  # Output: Sending email / Sending SMS