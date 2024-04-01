class Secret007():
    def __init__(self, code, place, time):
        self.code = code
        self.place = place
        self.time = time

    def print_secret_data(self):
        print(f"secret code : {code}")
        print(f"meeting point : {place}")
        print(f"time : {time}")

code, place, time = input().split()
secret = Secret007(code, place, time)
secret.print_secret_data()