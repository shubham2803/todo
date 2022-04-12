class BaseClass:
    def __init__(self, file_path=None):
        self.file_path = file_path

    def get_file_path(self, file_path=None):
        return self.file_path or '/home/admin1/Documents/todo/root/input.txt'

    def get_file_path_2(self, file_path=None):
        return self.file_path or '/home/admin1/Documents/todo/root/input_2.txt'
