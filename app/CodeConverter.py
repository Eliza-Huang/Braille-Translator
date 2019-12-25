class CodeConverter:
    
    def __init__(self):
        self.dict = {}
        path = 'app/encoding.txt'
        file = open(path, "r")
        l = file.readlines()
        for i in range(int(len(l) / 2)):
            self.dict[l[2 * i].rstrip()] = l[2 * i + 1].rstrip()
        file.close()
        self.dict[''] = ' '
    
    def translate(self, code):
        if code in self.dict:
            return self.dict[code]
        return ':('
