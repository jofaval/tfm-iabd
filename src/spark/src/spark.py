from conf import config

class SparkExecutor():
    """The main Spark's cluster's executor"""

    instance = None
    """Global instance of the executor"""

    # TODO: properly set the return type
    def get_spark_context(self):
        """Returns the spark context"""
        # TODO: implement
        raise NotImplementedError()

    def boot(self) -> None:
        """Boots the spark cluster"""
        raise NotImplementedError()

    # TODO: properly set the return type
    @classmethod
    def get_instance():
        """Returns the SparkExecutor instance"""
        if SparkExecutor.instance is None:
            SparkExecutor.instance = SparkExecutor()

        return SparkExecutor.instance

if __name__ == '__main__':
    SparkExecutor.get_instance().boot()