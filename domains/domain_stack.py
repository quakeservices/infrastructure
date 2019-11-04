from aws_cdk import core
import aws_cdk.aws_route53 as route53


class DomainStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        domains = ['quake.services',
                   'quake2.services',
                   'quake3.services']

        for domain in domains:
            route53.PublicHostedZone(self, domain, zone_name=domain)
