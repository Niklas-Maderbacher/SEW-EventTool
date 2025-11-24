class UserNotAuthorised(Exception):
    def __str__(self):
        return "User is not Authorised"
