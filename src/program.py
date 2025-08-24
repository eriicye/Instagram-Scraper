from instagrapi import Client


class Program:
    def __init__(self, username, password):
        self.client = Client()
        self.client.delay_range = [1, 3]

        self.username = username
        self.password = password

        self.followers = {}
        self.following = {}

    # private account info
    def retrieveAccountInfo(self):
        account_info = self.client.account_info()
        print(account_info)

    # public user profile
    def retrieveProfileInfo(self):
        print(f"Followers JSON File: {self.followers}")
        print("\n")
        print(f"Following JSON File: {self.following}")

    def checkWhoIsntFollowingYou(self): #
        for user_id in self.following:
            if user_id not in self.followers:
                user = self.following[user_id]
                print(f"Full Name: {user.full_name} | Username: {user.username}")

    def login(self):
        if self.client.login(self.username, self.password):
            print("Login successful")

            self.followers = self.client.user_followers(str(self.client.user_id))
            self.following = self.client.user_following(str(self.client.user_id))
        else:
            print("Unable to login")

    def logout(self):
        self.client.logout()
