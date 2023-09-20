import tkinter as tk
import os
import string
import winsound
import random

class SpookyApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()  # Hide the main window
        self.dialog_count = 0
        self.root.bind('<F9>', self.exit_app)  # Bind F9 key to exit function

    def create_string(self):
        return "".join([random.choice(string.ascii_letters) for x in range(random.randint(5, 20))])

    def spooky_beeps(self):
        for _ in range(10):  # Play 10 beeps
            freq = random.randint(200, 2000)  # Random frequency between 200 and 2000 Hz
            duration = random.randint(100, 500)  # Random duration between 100 and 500 ms
            winsound.Beep(freq, duration)
        
    def spooky_message(self):
        messages = [
            "I see you... \U0001F47B",  # Ghost emoji
            "Why did you run me? \U0001F480",  # Skull emoji
            "Do you believe in ghosts? \U0001F47B",
            "You can't escape... \U0001F63F",  # Crying cat face emoji
            "Happy Halloween! \U0001F383"  # Jack-o-lantern emoji
            ]
        return random.choice(messages)

    def fake_delete_files(self):
        base_directory = os.path.expanduser('~')  # Get the user's home directory

        # List of common file extensions for documents, images, etc.
        important_extensions = ['.doc', '.docx', '.pdf', '.jpg', '.jpeg', '.png', '.txt', '.xls', '.xlsx', '.ppt', '.pptx']

        # List of folders to search
        target_folders = ['Documents', 'Pictures', 'Desktop', 'Downloads']

        # Recursively search for files with the specified extensions in the target folders
        files = []
        for folder in target_folders:
            folder_path = os.path.join(base_directory, folder)
            if os.path.exists(folder_path):  # Check if the folder exists
                for dirpath, dirnames, filenames in os.walk(folder_path):
                    for filename in filenames:
                        if any(filename.endswith(ext) for ext in important_extensions):
                            files.append(os.path.join(dirpath, filename))

        if files:
            selected_file = random.choice(files)
            print(f"Deleting the following file because it is not scary: {selected_file} ...")
        else:
            print("No important-looking files found to delete!")
        
        self.root.after(2000, self.fake_delete_files)  # Schedule the next call



        
    def show_dialog(self):
        # self.spooky_beeps()
        dialog = tk.Toplevel(self.root)
        dialog.configure(bg='black')  # Spooky background color
        # Get screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Randomly determine x and y coordinates for the dialog
        x = random.randint(0, screen_width - 300)  # 300 is the width of the dialog
        y = random.randint(0, screen_height - 100)  # 100 is the height of the dialog
        dialog.geometry(f"300x100+{x}+{y}")  # Set the position and size of the dialog

        action = random.choice(['message1', 'message2', 'message3'])
        spooky_titles = ["Boo!", "Beware!", "Look Behind You!"]
        dialog.title(random.choice(spooky_titles))
        if action == 'message1':
            label = tk.Label(dialog, text=self.spooky_message(), fg="red", bg="black", font=("Chiller", 15))
        elif action == 'message2':
            label = tk.Label(dialog, text=self.spooky_message(), fg="blue", bg="black", font=("Chiller", 15))
        elif action == 'message3':
            label = tk.Label(dialog, text=self.spooky_message(), fg="white", bg="black", font=("Chiller", 15))

        label.pack(pady=20)
        button = tk.Button(dialog, text="OK", command=dialog.destroy, bg="grey", fg="white")
        button.pack(pady=10)

        # Random opacity for ghostly appearance
        alpha = random.uniform(0.3, 0.7)
        dialog.attributes('-alpha', alpha)

        # Eerie cursor
        dialog.config(cursor="pirate")

        self.dialog_count += 1

        if self.dialog_count < 50:
            self.root.after(5000, self.show_dialog)  # Show another dialog after 5 seconds
        else:
            self.exit_app(None)

    def exit_app(self, event):
        self.root.quit()

    def run(self):
        self.show_dialog()
        self.fake_delete_files()  # Start the fake file deletion process
        self.root.mainloop()


if __name__ == "__main__":
    app = SpookyApp()
    app.run()
