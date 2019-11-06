#!/usr/bin/env python3
import os
from aws_cdk import core

from domains.domain_stack import DomainStack
from vpcs.vpc_stack import VPCStack
from containers.ecr_stack import ECRStack
from containers.ecs_stack import ECSStack


app = core.App()

global_route53 = DomainStack(app, "DomainStack", env=us_west_2_env)

us_west_2 = dict()
us_west_2['env'] = {'account': os.getenv('AWS_ACCOUNT', os.getenv('CDK_DEFAULT_ACCOUNT', '')),
                    'region': os.getenv('AWS_DEFAULT_REGION', os.getenv('CDK_DEFAULT_REGION', ''))}

us_west_2['vpc'] = VPCStack(app, "VPCStack", env=us_west_2['env'])
us_west_2['ecr'] = ECRStack(app, "ECRStack", env=us_west_2['env'])
us_west_2['ecs'] = ECSStack(app, "ECSStack", env=us_west_2['env'], vpc=us_west_2['vpc'])

app.synth()
