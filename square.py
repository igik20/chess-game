class Square():
    def __init__(self, x, y, file, row) -> None:
        self.x = x
        self.y = y
        self.color = (110, 76, 35) if ( (x + y) // 125) % 2 == 1 else (217, 174, 121)
        self.file = file
        self.row = row

    def coord(self):
        return f"{self.file}{self.row}"