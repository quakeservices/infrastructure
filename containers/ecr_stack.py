from aws_cdk import core
import aws_cdk.aws_ecr as ecr


class ECRStack(core.Stack):

    def __init__(self,
                 scope: core.Construct,
                 id: str,
                 prefix: str,
                 **kwargs) -> None:

        super().__init__(scope, id, **kwargs)

        repos = [
            {'name': 'master', 'removal_policy': core.RemovalPolicy.DESTROY}
        ]

        for repo in repos:
            self.create_repo(name=repo['name'],
                             removal_policy=repo['removal_policy'])

    def create_repo(self,
                    name: str,
                    removal_policy,
                    image_count: int = 3):
        repo_name = '_'.join(['quakeservices', name])

        repository = ecr.Repository(
            self,
            repo_name,
            repository_name=repo_name,
            removal_policy=removal_policy
        )

        repository.add_lifecycle_rule(max_image_count=image_count)
