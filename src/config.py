# Copyright | 2019 | All rights reserved
# MIHAIL BUTNARU
import os

class Config:

    def MYSQL_DB(self):
        """
        """
        return os.getenv('MYSQL_DB', None)

    