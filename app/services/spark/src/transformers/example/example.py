from parent import SparkTransformer
from .models import TwitterResponse, Tweet, User

from module.spark.normalization import minmax_normalization

class ExampleSparkTransformer(SparkTransformer):
    """Example Spark Transformer"""
    def on_clean(self) -> None:
        self.df = self.df.dropna()

    def on_normalize(self) -> None:
        self.df = minmax_normalization(self.df)

    pass

if __name__ == '__main__':
    # Example of usage
    ExampleSparkTransformer.trasnform()