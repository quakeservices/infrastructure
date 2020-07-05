from aws_cdk import core
import aws_cdk.aws_route53 as route53
import aws_cdk.aws_certificatemanager as certificatemanager


class CertificateStack(core.Stack):

    def __init__(self,
                 scope: core.Construct,
                 id: str,
                 prefix: str,
                 domains: dict,
                 **kwargs) -> None:

        super().__init__(scope, id, **kwargs)

        regions = ['ap-southeast-2', 'us-east-1']

        primary_domain = [domain['domain'] for domain in domains if domain['primary']].pop()
        primary_zone = self.fetch_zone(primary_domain)
        secondary_domains = [domain['domain'] for domain in domains if not domain['primary']]

        subject_alt = secondary_domains + [domain['wildcard'] for domain in domains]

        for region in regions:
            certificate = certificatemanager.DnsValidatedCertificate(
                self,
                prefix + '_wildcard_' + region,
                hosted_zone=primary_zone,
                region=region,
                domain_name=primary_domain,
                subject_alternative_names=subject_alt,
                validation_method=certificatemanager.ValidationMethod.DNS
            )

    def fetch_zone(self, domain):
        return route53.HostedZone.from_lookup(
            self,
            'primary_zone',
            domain_name=domain
        )

