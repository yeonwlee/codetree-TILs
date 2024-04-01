class Bomb():
    def __init__(self, release_code: str = "", target_line_color: str = "", sec: int = 0):
        self.release_code = release_code
        self.target_line_color = target_line_color
        self.sec = sec
    
    def print_data(self):
        print(f"code : {self.release_code}")
        print(f"color : {self.target_line_color}")
        print(f"second : {self.sec}")
        


release_code, target_line_color, sec = input().split()
bomb = Bomb(release_code, target_line_color, int(sec))
bomb.print_data()