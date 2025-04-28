import os
current_directory = os.getcwd()
print("Current Directory:", current_directory)
from pathlib import Path
current_directory = Path.cwd()
print(current_directory)
