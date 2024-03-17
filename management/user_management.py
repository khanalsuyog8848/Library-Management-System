class UserManager:
    def __init__(self, storage_handler):
        """
        Initializes a UserManager object with a storage handler.

        Args:
            storage_handler: An instance of StorageHandler for interacting with the database.
        """
        self.storage = storage_handler

    def add_user(self, name, user_id):
        """
        Adds a new user to the library system.

        Args:
            name: The name of the user.
            user_id: The unique identifier for the user.
        """
        self.storage.add_user(name, user_id)
        print(f"User '{name}' added successfully.")

    def update_user(self, user_id, name=None):
        """
        Updates the information of an existing user in the library system.

        Args:
            user_id: The unique identifier of the user to update.
            name: (Optional) The new name of the user.
        """
        users = self.storage.database._read_data(self.storage.database.users_file)
        updated = False
        for user in users:
            if user["user_id"] == user_id:
                if name:
                    user["name"] = name
                updated = True
                break
        if updated:
            self.storage.database._write_data(self.storage.database.users_file, users)
            print(f"User with ID {user_id} updated successfully.")
        else:
            print(f"No user found with ID {user_id}.")

    def delete_user(self, user_id):
        """
        Deletes a user from the library system.

        Args:
            user_id: The unique identifier of the user to delete.
        """
        users = self.storage.database._read_data(self.storage.database.users_file)
        users = [user for user in users if user["user_id"] != user_id]
        self.storage.database._write_data(self.storage.database.users_file, users)
        print(f"User with ID {user_id} deleted successfully.")

    def list_users(self):
        """Lists all users in the library system."""
        self.storage.list_users()

    def search_users(self, **kwargs):
        """
        Searches for users in the library system based on specified criteria.

        Args:
            **kwargs: Arbitrary keyword arguments representing search criteria.

        Returns:
            None. Prints matching users or a message if no users are found.
        """
        users = self.storage.database._read_data(self.storage.database.users_file)
        results = users
        for key, value in kwargs.items():
            results = [user for user in results if user.get(key) == value]
        for user in results:
            print(user)
