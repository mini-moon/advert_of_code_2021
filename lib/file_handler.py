
class FileHandler:
    def __init__(self,name):
        self.name = name

    def raw_content(self):
        with open(self.name,'r') as file:
            content = file.read()
            return content

    def content_by_lines(self):
        with open(self.name,'r') as file:
            content = file.readlines()
            content = [line.replace('\n','') for line in content]
            return content

    def str_content_to_list(self):
        raw = self.raw_content()
        if isinstance(raw, str):
            return raw.split(",")