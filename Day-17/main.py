class User:
    def __init__(self,user_id,username):
        self.user_id = id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self,user):
        user.followers += 1
        user.following +=1



user1 = User(7022005,"Rijiya Sultana")
user2 = User(21102002,"Rakibul Islam")

user1.follow(user2)

print(user2.followers)
print(user2.following)
print(user1.followers)
print(user1.following)