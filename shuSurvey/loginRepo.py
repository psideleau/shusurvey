class LoginRepo:
    def __init__(self):
        self.user = {1234:
                     'Password',
                     5678:
                     'Password'}

    def get_user_info(self, user_id, password):
        db_password = self.user[user_id]
        
        return db_password == password
