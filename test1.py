
import shutil

def copy_file(source_path, destination_path):
    try:
        shutil.copy(source_path, destination_path)
        print(f"File '{source_path}' copied to '{destination_path}' successfully.")
    except Exception as e:
        print(f"Error: {e}")

# Example usage:
source_path = r"C:\Users\David\Downloads\55.jpg"  # Replace with your source file path
destination_path = r'C:\Users\David\OneDrive\Desktop'  # Replace with your destination folder path

copy_file(source_path, destination_path)