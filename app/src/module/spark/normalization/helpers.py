from pyspark.ml.feature import VectorAssembler, MinMaxScaler, StandardScaler
from pyspark.ml import Pipeline
from ..dataframe import get_df_columns
from .constants import CONSTANTS


def scaler_pipeline(
    df: pyspark.sql.DataFrame,
    scaler_class,
) -> pyspark.sql.DataFrame:
    """
    The scaler pipeline to apply

    df : pyspark.sql.DataFrame
        The dataframe
    scaler_class
        The scaler to use

    returns pyspark.sql.DataFrame
    """
    assembler = VectorAssembler(
        inputCols=get_df_columns(df),
        outputCol=CONSTANTS['COLS']['VECTORIZED_COL'],
    )

    scaler = scaler_class(
        inputCol=CONSTANTS['COLS']['VECTORIZED_COL'],
        outputCol=CONSTANTS['COLS']['SCALED_COL'],
    )

    pipeline = Pipeline(stages=[
        assembler,
        scaler,
    ])

    scaler_model = pipeline.fit(df)
    scaled_data = scaler_model.transform(df)

    return scaled_data


def minmax_normalization(
    df: pyspark.sql.DataFrame,
) -> pyspark.sql.DataFrame:
    """
    Applies MinMax Normalization to a Spark DataFrame

    df : pyspark.sql.DataFrame
        The dataframe

    returns pyspark.sql.DataFrame
    """
    scaled = scaler_pipeline(
        df=df,
        scaler_class=MinMaxScaler,
    )

    return scaled


def standard_normalization(
    df: pyspark.sql.DataFrame,
) -> pyspark.sql.DataFrame:
    """
    Applies MinMax Normalization to a Spark DataFrame

    df : pyspark.sql.DataFrame
        The dataframe

    returns pyspark.sql.DataFrame
    """
    scaled = scaler_pipeline(
        df=df,
        scaler_class=StandardScaler,
    )

    return scaled
