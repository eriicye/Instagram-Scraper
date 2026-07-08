from program import Program

user = input("Enter in your username: ")
password = input("Enter in your password: ")

program = Program(username=user, password=password)

program.login()
program.checkWhoIsntFollowingYou()
