from aws_cdk import core
import aws_cdk.aws_ecr as ecr


class ECRStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        repo = ecr.Repository(self, 'quakeservices')

