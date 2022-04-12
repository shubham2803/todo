from Base import BaseClass
import ast
from threading import Thread
import pickle


class SourceCode(BaseClass):

    def add(self):
        input_1 = open(self.get_file_path(), 'r').readline().strip()
        input_2 = open(self.get_file_path_2(), 'r').readline().strip()

        try:
            input_1 = ast.literal_eval(input_1)
        except:
            pass

        try:
            input_2 = ast.literal_eval(input_2)
        except:
            pass
        print(type(input_1))
        result = input_1 + input_2

        print(result)

    def multiply(self):
        input_1 = open(self.get_file_path(), 'r').readline().strip()
        input_2 = open(self.get_file_path_2(), 'r').readline().strip()

        try:
            input_1 = ast.literal_eval(input_1)
        except:
            pass

        try:
            input_2 = ast.literal_eval(input_2)
        except:
            pass

        if isinstance(input_2, int) and isinstance(input_1, int):
            print(input_1 * input_2)
        else:
            print('Data Types not compatible or don\'t match')

    def divide(self):
        input_1 = open(self.get_file_path(), 'r').readline().strip()
        input_2 = open(self.get_file_path_2(), 'r').readline().strip()

        try:
            input_1 = ast.literal_eval(input_1)
        except:
            pass

        try:
            input_2 = ast.literal_eval(input_2)
        except:
            pass

        if isinstance(input_2, int) and isinstance(input_1, int):
            print(input_1 // input_2)


obj = SourceCode()
thread_1 = Thread(target=obj.multiply)
thread_1.start()
thread_1.join()

with open('saved_objects.txt', 'wb') as objects:
    pickle.dump(f'{thread_1.__dict__}', objects)
