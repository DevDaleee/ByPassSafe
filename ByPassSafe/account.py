# account.py


class MasterAccount:
    def __init__(self, username, hashed_password, email):
        self.username = username
        self.password = hashed_password  
        self.email = email


class Account:
    def __init__(self, master_id, username, password, email):
        self.master_id = master_id
        self.username = username
        self.password = password
        self.email = email