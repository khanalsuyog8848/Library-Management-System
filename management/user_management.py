from storage import StorageHandler

class UserManager:
    def __init__(self, storage_handler):
        self.storage = storage_handler

    def add_user(self, name, user_id):
        self.storage.add_user(name, user_id)
        print(f"User '{name}' added successfully.")

    def update_user(self, user_id, name=None):
        users = self.storage.database._read_data(self.storage.database.users_file)
        updated = False
        for user in users:
            if user['user_id'] == user_id:
                if name:
                    user['name'] = name
                updated = True
                break
        if updated:
            self.storage.database._write_data(self.storage.database.users_file, users)
            print(f"User with ID {user_id} updated successfully.")
        else:
            print(f"No user found with ID {user_id}.")

    def delete_user(self, user_id):
        users = self.storage.database._read_data(self.storage.database.users_file)
        users = [user for user in users if user['user_id'] != user_id]
        self.storage.database._write_data(self.storage.database.users_file, users)
        print(f"User with ID {user_id} deleted successfully.")

    def list_users(self):
        self.storage.list_users()

    def search_users(self, **kwargs):
        users = self.storage.database._read_data(self.storage.database.users_file)
        results = users
        for key, value in kwargs.items():
            results = [user for user in results if user.get(key) == value]
        for user in results:
            print(user)
