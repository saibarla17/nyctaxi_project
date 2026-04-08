from pyspark.sql import DataFrame
from pyspark.sql.functions import current_timestamp

def add_processed_timestamp(df: DataFrame) -> DataFrame:
    """
    Adds a 'process_timestamp' column to the DataFrame with the current timestamp.

    Parameters:
        df (DataFrame): The input Spark DataFrame.

    Returns:
        DataFrame: The DataFrame with an additional 'process_timestamp' column.
    """
    return df.withColumn("process_timestamp", current_timestamp())
