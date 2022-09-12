"""Module for obtaining ranking data
"""

import cfbd


class Ranker:
    """Class used to obtain ranking data based on parameters provided"""

    api_config: cfbd.Configuration

    def __init__(self, year: int, week: int):
        pass

    @property
    def off_yds_wt(self) -> float:
        """Weight assigned to total offensive yards

        Returns:
            float
        """
        return self.off_yds_wt

    @off_yds_wt.setter
    def off_yds_wt(self, value: float) -> None:
        self.off_yds_wt = value

    @property
    def def_yds_wt(self) -> float:
        """Weight assigned to total defensive yards

        Returns:
            float
        """
        return self.def_yds_wt

    @def_yds_wt.setter
    def def_yds_wt(self, value: float) -> None:
        self.def_yds_wt = value
