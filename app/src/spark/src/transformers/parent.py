from module.utils.decorators import error_boundary

class SparkTransformer():
    """Base class for a transformer class, one for each channel"""

    @error_boundary
    def clean():
        """Clean the dataset"""
        raise NotImplementedError()

    @error_boundary
    def normalize():
        """Normalizes the dataset"""
        raise NotImplementedError()

    def trasnform():
        """Main course of action"""
        raise NotImplementedError()

    pass