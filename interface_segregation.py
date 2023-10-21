# ################# I - Interface Segregation #######################
# Author: Uncle Bob (Robert C. Martin)
# Principle: Clients (subclasses) should not be forced to implement interfaces (methods) they do not use.


# This violates the Interface Segregation principle


# from abc import ABC, abstractmethod
#
#
# class Widget(ABC):
#     @abstractmethod
#     def get_pressed_key(self):
#         pass
#
#     @abstractmethod
#     def click(self):
#         pass
#
#
# class TextWidget(Widget):
#     def get_pressed_key(self):
#         key = input()
#         return key
#
#     def click(self):
#         raise Exception('TextWidget does not implement click()')
#
#
# class ButtonWidget(Widget):
#     def get_pressed_key(self):
#         raise Exception('ButtonWidget does not implement get_pressed_key()')
#
#     def click(self):
#         return 'do somthing'
#
#
# txt = TextWidget()
# print(txt.get_pressed_key())
# txt.click()


# This follows the Interface Segregation principle

from abc import ABC, abstractmethod


class KeyboardWidget(ABC):
    @abstractmethod
    def get_pressed_key(self):
        pass


class ClickableWidget(ABC):
    @abstractmethod
    def click(self):
        pass


class TextWidget(KeyboardWidget):
    def get_pressed_key(self):
        key = input('input: ')
        return key


class ButtonWidget(ClickableWidget):
    def click(self):
        return 'button pressed -> do something'


txt = TextWidget()
print(txt.get_pressed_key())

btn = ButtonWidget()
print(btn.click())
