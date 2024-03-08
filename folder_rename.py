
import os

def remove_word_from_folders(directory, word_to_remove):
    # List all entries in the directory
    for folder_name in os.listdir(directory):
        folder_path = os.path.join(directory, folder_name)

        # Check if it's a directory and the word is in the folder name
        if os.path.isdir(folder_path) and word_to_remove in folder_name:
            # Create new folder name without the specified word
            new_folder_name = folder_name.replace(word_to_remove, "")
            new_folder_path = os.path.join(directory, new_folder_name)

            # Rename the folder
            os.rename(folder_path, new_folder_path)
            print(f"Renamed '{folder_name}' to '{new_folder_name}'")

# Example usage
directory = '/Users/nebs/Desktop/Research/NA/2024-01-24/JEPG'  # Replace with the path to your directory
word_to_remove = '01'  # Replace with the word you want to remove
remove_word_from_folders(directory, word_to_remove)
