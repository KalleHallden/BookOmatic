class ForgotPassword:
    def __init__(self, UserID, email, reset_url, created_at):
        self.uid = UserID
        self.email = email
        self.reset_url = reset_url
        self.created_at = created_at