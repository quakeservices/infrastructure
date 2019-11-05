from aws_cdk import core
import aws_cdk.aws_ecr as ecr


class ECRStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        images = ['master', 'web-backend']
        lifecycle_rules = list()

        for image in images:
            lifecycle_rules.append(ecr.LifecycleRule(tag_prefix_list=[image], max_image_count=20))


        repo = ecr.Repository(self, 'quakeservices',
                lifecycle_rules=lifecycle_rules)

