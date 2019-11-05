#!/usr/bin/env python3
import os
from aws_cdk import core

from domains.domain_stack import DomainStack
from vpcs.vpc_stack import VPCStack
from containers.ecr_stack import ECRStack
from containers.ecs_stack import ECSStack


default_env = {'account': os.getenv('AWS_ACCOUNT', os.getenv('CDK_DEFAULT_ACCOUNT', '')),
               'region': os.getenv('AWS_DEFAULT_REGION', os.getenv('CDK_DEFAULT_REGION', ''))}


app = core.App()
DomainStack(app, "DomainStack", env=default_env)
vpc = VPCStack(app, "VPCStack", env=default_env)
ECRStack(app, "ECRStack", env=default_env)
ECSStack(app, "ECSStack", env=default_env, vpc=vpc)

app.synth()
