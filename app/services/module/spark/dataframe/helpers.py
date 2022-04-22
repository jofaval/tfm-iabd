from typing import List

def get_df_columns(
    df: pyspark.sql.DataFrame
) -> List[str]:
    """Returns the columns from a Spark DataFrame"""
    columns = df.columns

    return columns