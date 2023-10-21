# ################# D - Dependency Inversion #############################
# Principle: High-level modules should not depend on low-level modules.
            # Both should depend on abstractions - The scope of this principle is to
            # eliminate the coupling


# Example that violates the principle

# class ShowData:
#     def __init__(self, data_from_txt):
#         self.data_from_txt = data_from_txt
#
#     def print_data(self):
#         print(self.data_from_txt.get_data_from_text())
#
#
# class FileData:
#     def __init__(self, file):
#         self.file = file
#
#     def get_data_from_text(self):
#         with open(self.file, 'r') as fr:
#             content = fr.read()
#         return content
#
#
# txt = FileData('test.txt')
# show = ShowData(txt)
# show.print_data()

# This follows the Dependency inversion principle

import csv
from abc import ABC, abstractmethod


class FileType(ABC):
    @abstractmethod
    def get_data(self):
        pass


class TextFile(FileType):
    def __init__(self, file):
        self.file = file

    def get_data(self):
        with open(self.file, 'r') as fr:
            content = fr.read()
        return content


class CSVFile(FileType):
    def __init__(self, file):
        self.file = file

    def get_data(self):
        with open(self.file, 'r') as fr:
            reader = csv.reader(fr)
            content = [line for line in reader]
        return content


class ShowData:
    def __init__(self, data_from_file):
        self.data_from_file = data_from_file

    def print_data(self):
        print(self.data_from_file.get_data())


txt = TextFile('test.txt')
csv_data = CSVFile('test.csv')

for item in [txt, csv_data]:
    show = ShowData(item)
    show.print_data()
