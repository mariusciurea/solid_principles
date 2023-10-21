# ############### L - Liskov Substitution #################################
# Author: Barbara Liskov
# Principle: Subtypes must be substitutable for their base types.
# A child class must be substitutable for its parent class
# Example: We use the same example with the employees.

# Example that violates this principle
#
# import csv
# from abc import ABC, abstractmethod
#
#
# class SaveData(ABC):
#     @abstractmethod
#     def save(self, data, file):
#         pass
#
#
# class TextData(SaveData):
#     def save(self, data, txt_file):
#         with open(txt_file, 'w') as fw:
#             fw.write(data)
#
#
# class CsvData(SaveData):
#     def save(self, data, csv_file):
#         with open(csv_file, 'w') as fw:
#             writer = csv.writer(fw)
#             writer.writerow([data])
#
#
# text = TextData()
# file_csv = CsvData()
#
# for item in [text, file_csv]:
#     item.save('test test test', 'test.txt')

# Solve Liskov substitution
# #
import csv
from abc import ABC, abstractmethod


class SaveData(ABC):
    def save(self, data):
        pass


class TextData(SaveData):
    def __init__(self, file):
        self.file = file

    def save(self, data):
        with open(self.file, 'w') as fw:
            fw.write(data)


class CsvData(SaveData):
    def __init__(self, file):
        self.file = file

    def save(self, data):
        with open(self.file, 'w') as fw:
            writer = csv.writer(fw)
            writer.writerow([data])


text = TextData('test.txt')
file_csv = CsvData('test.csv')

for item in [text, file_csv]:
    item.save('test test test')
