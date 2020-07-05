from aws_cdk import core
import aws_cdk.aws_ecr as ecr


class ECRStack(core.Stack):

    def __init__(self,
                 scope: core.Construct,
                 id: str,
                 prefix: str,
                 **kwargs) -> None:

        super().__init__(scope, id, **kwargs)

        repository = ecr.Repository(
            self,
            'quakeservices',
        )

        repository.add_lifecycle_rule(
            max_image_count=10
        )

