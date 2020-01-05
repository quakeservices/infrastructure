from aws_cdk import core
from aws_cdk.aws_ec2 import Vpc, SubnetType, SubnetConfiguration, GatewayVpcEndpointAwsService


class VPCStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
       
        subnet_public = SubnetConfiguration(cidr_mask=24, name='public', subnet_type=SubnetType.PUBLIC)
        subnet_private = SubnetConfiguration(cidr_mask=24, name='private', subnet_type=SubnetType.PRIVATE)
        subnet_conf = [subnet_public, subnet_private]

        self.vpc = Vpc(self, 'QuakeServicesVPC', 
                       cidr='172.16.0.0/16',
                       nat_gateways=1,
                       max_azs=3,
                       subnet_configuration=subnet_conf)

        self.vpc.add_s3_endpoint('s3-endpoint', 
                                 subnets=[subnet_private])

        self.vpc.add_dynamo_db_endpoint('dynamo-endpoint',
                                        subnets=[subnet_private])

        """
        self.vpc.add_gateway_endpoint('ecr-endpoint',
                                      service=GatewayVpcEndpointAwsService('ecr-service', prefix='ecr'),
                                      subnets=[subnet_private])

        self.vpc.add_gateway_endpoint('ecs-endpoint',
                                      service=GatewayVpcEndpointAwsService('ecs-service', prefix='ecs'),
                                      subnets=[subnet_private])
        """
