import os


def get_project_path():
    """Returns the absolute path to the project directory."""
    # Get the current working directory
    current_path = os.path.abspath(__file__)

    # Traverse up the directory tree until we find the project root directory
    while not os.path.exists(os.path.join(current_path, 'README.md')):
        current_path = os.path.dirname(current_path)

    return current_path

