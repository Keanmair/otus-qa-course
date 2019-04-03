# with open("mynewfile.txt", mode="r") as file:
class FileReader:

    def __init__(self, file_path):
        self.file = file_path

    def __enter__(self):
        self.f_obj = open(self.file, "r+")
        return self.f_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f_obj.close()


with FileReader("data.txt") as f:
    print(f)
    print(f.read())
