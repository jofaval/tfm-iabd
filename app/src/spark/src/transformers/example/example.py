from parent import SparkTransformer
from .models import TwitterResponse, Tweet, User

class ExampleSparkTransformer(SparkTransformer):
    """Example Spark Transformer"""
    pass

if __name__ == '__main__':
    # Example of usage
    ExampleSparkTransformer.trasnform()