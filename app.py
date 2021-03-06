#!/usr/bin/env python3
import os
from aws_cdk import core

from domains.domain_stack import DomainStack
from certificates.certificate_stack import CertificateStack
from containers.ecr_stack import ECRStack


app = core.App()

ap_southeast_2 = dict()
ap_southeast_2['env'] = {
    'account': os.getenv('AWS_ACCOUNT', os.getenv('CDK_DEFAULT_ACCOUNT', '')),
    'region': os.getenv('AWS_DEFAULT_REGION', os.getenv('CDK_DEFAULT_REGION', ''))
}

stack_prefix = "QuakeServices"

domains = [
    {'domain': 'quake.services',  'wildcard': '*.quake.services', 'primary': True},
    {'domain': 'quake2.services', 'wildcard': '*.quake2.services', 'primary': False},
    {'domain': 'quake3.services', 'wildcard': '*.quake3.services', 'primary': False}
]

global_route53 = DomainStack(
    app,
    stack_prefix + "Domains",
    prefix=stack_prefix,
    domains=domains,
    env=ap_southeast_2['env']
)

certificates = CertificateStack(
    app,
    stack_prefix + "Certificates",
    prefix=stack_prefix,
    domains=domains,
    env=ap_southeast_2['env']
)
    
ecr = ECRStack(
    app,
    stack_prefix + "ECR",
    prefix=stack_prefix,
    env=ap_southeast_2['env']
)

app.synth()
