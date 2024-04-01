class UserInfo():
    def __init__(self, user_id: str = "codetree", level: int = 10):
        self.user_id = user_id
        self.level = level

    def print_user_info(self) -> None:
        print(f"user {self.user_id} lv {self.level}")
    

user_id, level = input().split()
user1 = UserInfo()
user1.print_user_info()

user2 = UserInfo(user_id, level)
user2.print_user_info()