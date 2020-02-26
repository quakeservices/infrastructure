from aws_cdk import core
import aws_cdk.aws_ec2 as ec2


class VPCStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
       
        subnet_public = ec2.SubnetConfiguration(cidr_mask=24, name='public', subnet_type=ec2.SubnetType.PUBLIC)
        subnet_private = ec2.SubnetConfiguration(cidr_mask=24, name='private', subnet_type=ec2.SubnetType.PRIVATE)
        subnet_conf = [subnet_public, subnet_private]

        self.vpc = ec2.Vpc(self, 'QuakeServicesVPC',
                           cidr='172.16.0.0/16',
                           nat_gateways=1,
                           max_azs=3,
                           subnet_configuration=subnet_conf)

        self.vpc.add_gateway_endpoint(
                's3-endpoint',
                service=ec2.GatewayVpcEndpointAwsService('s3'))

        self.vpc.add_gateway_endpoint(
                'dynamo-endpoint',
                service=ec2.GatewayVpcEndpointAwsService('dynamodb'))

        self.vpc.add_flow_log("FlowLog")

        """
        self.vpc.add_gateway_endpoint('ecr-endpoint',
                                      service=GatewayVpcEndpointAwsService('ecr-service', prefix='ecr'),
                                      subnets=[subnet_private])

        self.vpc.add_gateway_endpoint('ecs-endpoint',
                                      service=GatewayVpcEndpointAwsService('ecs-service', prefix='ecs'),
                                      subnets=[subnet_private])
        """
