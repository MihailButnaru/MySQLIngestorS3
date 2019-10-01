# Copyright | 2019 | All rights reserved
# MIHAIL BUTNARU
from src.serializers.serializer_factory import factory

class Serializer:
    """
    Generic implementation of the format serializer
    """
    def serializer(self, serializable, service):
        """
        This is responsable to decide which service will run based
        on the requirements.
            Args:
                serializable (str) : data that needs to be serialized
                service (str) : usually the format type
        """
        serializer = factory.get_serializer(service)
        return serializer.serialize(serializable)

serialize = Serializer()