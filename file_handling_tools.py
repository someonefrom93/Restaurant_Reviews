import os
import zipfile

class FileHandling:
    """
    A class for handling file operations, such as unzipping folders.

    Attributes:
    - dir_in (str): The input directory containing files to be processed.
    - dir_out (str): The output directory where the contents will be extracted.
    """


    def __init__(self, dir_in, dir_out):
        """
        Initialize the FileHandling instance with input and output directories.

        Parameters:
        - dir_in (str): The input directory containing files to be processed.
        - dir_out (str): The output directory where the contents will be extracted.
        """
        self.dir_in = dir_in
        self.dir_out = dir_out

    def unzip_folders(self):
        """
        Unzip folders in the input directory and save the contents in the output directory.

        Iterates over each file in the input directory, checks if it is a zip file,
        creates a directory to unzip the contents, and extracts the files.

        Note: This method assumes that the input directory contains zip files to be processed.
        """
        # Iterate over each file in the input directory
        for root, _, files in os.walk(self.dir_in):
            for file in files:
                file_path = os.path.join(root, file)
                
                # Check if the file is a zip file
                if file.endswith(".zip"):
                    # Create a directory to unzip the contents
                    output = os.path.join(self.dir_out, os.path.splitext(file)[0])
                    os.makedirs(output, exist_ok=True)

                    # Unzip the file
                    with zipfile.ZipFile(file_path, 'r') as zip_ref:
                        zip_ref.extractall(output)