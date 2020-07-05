from aws_cdk import core
import aws_cdk.aws_route53 as route53


class DomainStack(core.Stack):

    def __init__(self,
                 scope: core.Construct,
                 id: str,
                 prefix: str,
                 domains: dict,
                 **kwargs) -> None:

        super().__init__(scope, id, **kwargs)

        for domain_name in [domain['domain'] for domain in domains]:
            route53.PublicHostedZone(
                self,
                domain_name,
                zone_name=domain_name
            )
