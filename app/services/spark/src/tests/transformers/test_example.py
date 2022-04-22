import unittest
from ....src.transformers.example import ExampleSparkTransformer
from pyspark.sql.functions import *
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, StringType, LongType
from datetime import datetime
from pyspark.sql import SparkSession


class SparkExampleTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.spark = (
            SparkSession
            .builder
            .master("local[*]")
            .appName("Unit-tests")
            .getOrCreate()
        )

    def test_example(self):
        # 1. Prepare an input data frame that mimics our source data.
        input_schema = StructType([
            StructField('StoreID', IntegerType(), True),
            StructField('Location', StringType(), True),
            StructField('Date', StringType(), True),
            StructField('ItemCount', IntegerType(), True)
        ])
        input_data = [
            (1, "Bangalore", "2021-12-01", 5),
            (2, "Bangalore", "2021-12-01", 3),
            (5, "Amsterdam", "2021-12-02", 10),
            (6, "Amsterdam", "2021-12-01", 1),
            (8, "Warsaw", "2021-12-02", 15),
            (7, "Warsaw", "2021-12-01", 99)
        ]
        input_df = self.spark.createDataFrame(
            data=input_data,
            schema=input_schema
        )
        # 2. Prepare an expected data frame which is the output that we expect.
        expected_schema = StructType(
            [
                StructField('Location', StringType(), True),
                StructField('TotalItemCount', LongType(), True)
            ]
        )

        expected_data = [
            ("Bangalore", 8),
            ("Warsaw", 114),
            ("Amsterdam", 11),
        ]
        expected_df = self.spark.createDataFrame(
            data=expected_data,
            schema=expected_schema
        )

        # 3. Apply our transformation to the input data frame
        transformer = ExampleSparkTransformer(
            df=input_df
        )
        transformer.transform()
        transformed_df = transformer.df

        # 4. Assert the output of the transformation to the expected data frame.
        def field_list(fields): return (
            fields.name,
            fields.dataType,
            fields.nullable
        )

        fields1 = [
            *map(
                field_list,
                transformed_df.schema.fields
            )
        ]
        fields2 = [
            *map(
                field_list,
                expected_df.schema.fields
            )
        ]
        # Compare schema of transformed_df and expected_df
        res = set(fields1) == set(fields2)

        # assert
        self.assertTrue(res)
        # Compare data in transformed_df and expected_df
        self.assertEqual(
            sorted(
                expected_df.collect()
            ),
            sorted(
                transformed_df.collect()
            )
        )

    @classmethod
    def tearDownClass(cls):
        cls.spark.stop()
