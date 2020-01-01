from aws_cdk import core
import aws_cdk.aws_route53 as route53
import aws_cdk.aws_certificatemanager as certificatemanager


class DomainStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        regions = ['us-west-2', 'us-east-1']

        primary_domain = 'quake.services'
        secondary_domains = ['quake2.services',
                             'quake3.services']

        domains = [primary_domain] + secondary_domains

        subject_alt = secondary_domains + ['*.' + x for x in domains]
        print(subject_alt)

        zones = dict()
        for domain in domains:
            zones[domain] = route53.PublicHostedZone(self, domain, zone_name=domain)

        for region in regions:
            certificate = certificatemanager.DnsValidatedCertificate(self, 'wildcard_' + region,
                    hosted_zone=zones[primary_domain],
                    region=region,
                    domain_name=primary_domain,
                    subject_alternative_names=subject_alt,
                    validation_method=certificatemanager.ValidationMethod.DNS)
