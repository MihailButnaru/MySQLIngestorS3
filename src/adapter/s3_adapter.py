# Copyright | 2019 | All rights reserved
# MIHAIL BUTNARU
import boto3

def init_aws_connection(config):
    """
    Set up a connection to access AWS services
        Args:
            config : list of configurations
        Returns:
            aws client instance
    """
    return boto3.client(
        config.AWS_SERVICE,
        aws_access_key_id=config.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY
    )
