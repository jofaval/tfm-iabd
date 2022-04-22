from pydantic import BaseModel
from typing import List

class SparkTransformer(BaseModel):
    """Base class for a transformer class, one for each channel"""
    df: pyspark.sql.DataFrame
    """The dataframe to transform"""
    cleaned: bool = False
    """Has it been cleaned?"""
    normalized: bool = False
    """Has it been normalized?"""
    standarized: bool = False
    """Has it been standarized?"""
    transformed: bool = False
    """Has it been transformed?"""

    def on_clean_start(
        self
    ) -> None:
        """Before cleansing starts"""
        pass

    def on_clean(
        self
    ) -> None:
        """Executes the cleansing"""
        pass

    def on_clean_end(
        self
    ) -> None:
        """After cleansing ends"""
        pass

    def clean(
        self
    ) -> bool:
        """Cleans the dataset, no more missing values from this point onward"""
        if self.cleaned:
            return True

        success: bool = True

        self.on_clean_start()

        try:
            self.on_clean()
            success = True
        except Exception as e:
            success = False

        self.on_clean_end()

        self.cleaned = success

        return success

    def on_standarize_start(
        self
    ) -> None:
        """Before standarization starts"""
        pass

    def on_standarize(
        self
    ) -> None:
        """Executes the standarization"""
        pass

    def on_standarize_end(
        self
    ) -> None:
        """After standarization ends"""
        pass

    def standarize(
        self
    ) -> bool:
        """Standarizes the dataset, all the data is where expected, how it is expected to be"""
        if self.standarized:
            return True

        success: bool = True

        self.on_standarize_start()

        try:
            self.on_standarize()
            success = True
        except Exception as e:
            success = False

        self.on_standarize_end()

        self.standarized = success

        return success

    def on_normalize_start(
        self
    ) -> None:
        """Before normalization starts"""
        pass

    def on_normalize(
        self
    ) -> None:
        """Executes the normalization"""
        pass

    def on_normalize_end(
        self
    ) -> None:
        """After normalization ends"""
        pass

    def normalize(
        self
    ) -> bool:
        """Normalizes the dataset, no more different scales and too much difference between values"""
        if self.normalized:
            return True

        success: bool = True

        self.on_normalize_start()

        try:
            self.on_normalize()
            success = True
        except Exception as e:
            success = False

        self.on_normalize_end()

        self.normalized = success

        return success

    def on_transform_start(
        self
    ) -> bool:
        """Before transformation starts"""
        return True

    def on_transform(
        self,
        order: List[callable] = None,
    ) -> bool:
        """
        Executes the transformation

        order : List[callable]
            Represents the order of the actions

        returns bool
        """
        success: bool = True

        if order:
            for action in order:
                if action:
                    success &= action()
        else:
            success &= self.clean()
            success &= self.standarize()
            success &= self.normalize()

        return success

    def on_transform_end(
        self
    ) -> bool:
        """After transformation ends"""
        return True

    def transform(
        self,
        order: List[callable] = None,
    ) -> bool:
        """Main course of action of the transformer"""
        if self.transformed:
            return True

        # Backups up the current DataFrame, just in case
        df_backup: pyspark.sql.DataFrame = self.df.alias('df_backup')

        success: bool = True

        success &= self.on_transform_start()

        try:
            success &= self.on_transform(order)
        except Exception as e:
            success = False

        success &= self.on_transform_end()

        # If the transformation, for whatever reason, wasn't successful retore the backup
        if not success:
            self.df: pyspark.sql.DataFrame = df_backup

        self.transformed = success

        return success