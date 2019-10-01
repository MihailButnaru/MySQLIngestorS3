# Copyright | 2019 | All rights reserved
# MIHAIL BUTNARU

class SerializerFactory:
    """
    Serializer interface, customized behaviour
    based on different type object, different format
    """
    def get_serializer(self, format):
        """
        It evaluates the value of the format and decides the 
        concrete implementation to create and return
            Args:
                format (str): type of the format
        """
        if format == 'csv':
            pass
        else:
            raise ValueError(format)

factory = SerializerFactory()