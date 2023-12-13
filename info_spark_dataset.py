from pyspark.sql import DataFrame

class InfoDataSet(DataFrame):
    """
    A specialized class for handling and displaying information about a PySpark DataFrame.

    This class extends the functionality of the pyspark.sql DataFrame to include additional
    methods for displaying information about the DataFrame.

    Attributes:
    - Inherits all attributes from the PySpark DataFrame class.

    Methods:
    - display_columns(): Display the columns of the DataFrame along with their index.
      This method prints the column names in a formatted manner with their corresponding indices.
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor for the InfoDataSet class.

        Parameters:
        - *args: Positional arguments to be passed to the PySpark DataFrame constructor.
        - **kwargs: Keyword arguments to be passed to the PySpark DataFrame constructor.

        Note: This constructor inherits the constructor of the PySpark DataFrame class.
        """
        super(InfoDataSet, self).__init__(*args, **kwargs)
    
    def display_columns(self):
        """
        List column names

        This method prints the column names in a formatted manner with their corresponding indices.
        Example:
            Column:
                1. Column1
                2. Column2
                3. Column3
        """
        columns = self.columns
        print('Column:')
        for index, column in enumerate(columns, start=1):
            print(f"\t{index}.- {column}")