class Assignment1:
    def __init__(self):
        self.user_names = []  
        self.storage_spaces = [] 
        self.used_spaces = []  
    
    def create_user(self, user_name, storage_space):
        if user_name == "" or user_name in self.user_names:
            print(" Username blank or already taken!")
            return
        if int(storage_space) <= 0:
            print("Storage space must be a positive number!")
            return
        
        self.user_names.append(user_name)
        self.storage_spaces.append(int(storage_space))
        self.used_spaces.append(0)
        print(f"User '{user_name}' created successfully with {storage_space}MB of storage.")
    
    def delete_account(self, user_name):
        if user_name not in self.user_names:
            print(f"Error: User '{user_name}' does not exist.")
            return
        index = self.user_names.index(user_name)
        self.user_names.pop(index)
        self.storage_spaces.pop(index)
        self.used_spaces.pop(index)
        print(f"User '{user_name}' deleted successfully.")
    
    def upload_file(self, user_name, filename, filesize):
        if user_name not in self.user_names:
            print(f"Error: User '{user_name}' does not exist.")
            return
        if int(filesize) <= 0:
            print("Error: File size must be positive.")
            return
        
        index = self.user_names.index(user_name)
        if self.storage_spaces[index] - self.used_spaces[index] < int(filesize):
            print(f"Error: Not enough space for '{filename}'. Available: {self.storage_spaces[index] - self.used_spaces[index]}MB.")
            return
        
        self.used_spaces[index] += int(filesize)
        print(f"'{filename}' uploaded successfully. {filesize}MB used.")
    
    def display_users(self):
        if len(self.user_names) == 0:
            print("No users exist.")
        else:
            for i in range(len(self.user_names)):
                available_storage = self.storage_spaces[i] - self.used_spaces[i]
                print(f"Username: {self.user_names[i]}, Available Storage: {available_storage}MB / {self.storage_spaces[i]}MB")
            print()
    
    def main(self):
        while True:
            print("\nCloud Storage Management System")
            print("1. Create User Account")
            print("2. Delete User Account")
            print("3. Upload File")
            print("4. List User Accounts")
            print("5. Exit")
            
            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                username = input("Enter the username: ")
                try:
                    storage_space = int(input("Enter available storage space (in MB): "))
                    self.create_user(username, storage_space)
                except ValueError:
                    print("Error: Storage space must be a valid integer.")
                
            elif choice == "2":
                username = input("Enter the username to delete: ")
                self.delete_account(username)
                
            elif choice == "3":
                username = input("Enter the username: ")
                filename = input("Enter the filename: ")
                try:
                    filesize = int(input("Enter the file size (in MB): "))
                    self.upload_file(username, filename, filesize)
                except ValueError:
                    print("Error: File size must be a valid integer.")
            
            elif choice == "4":
                self.display_users()
            
            elif choice == "5":
                print("Exiting the program. Goodbye!")
                break
            
            else:
                print("Invalid choice. Please try again.")


# Start the program by displaying the menu
assignment = Assignment1()
assignment.main()




