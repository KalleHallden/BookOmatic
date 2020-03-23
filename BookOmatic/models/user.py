class User:
    def __init__(self, UserID, email, password, first_name, last_name, created_at):
        self.uuid = UserID
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.created_at = created_at