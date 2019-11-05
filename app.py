#!/usr/bin/env python3
import os
from aws_cdk import core

from domains.domain_stack import DomainStack
from vpcs.vpc_stack import VPCStack


default_env = {'account': os.getenv('AWS_ACCOUNT', os.getenv('CDK_DEFAULT_ACCOUNT', '')),
               'region': os.getenv('AWS_DEFAULT_REGION', os.getenv('CDK_DEFAULT_REGION', ''))}


app = core.App()
DomainStack(app, "DomainStack", env=default_env)
VPCStack(app, "VPCStack", env=default_env)

app.synth()
