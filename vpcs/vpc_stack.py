from aws_cdk import core
from aws_cdk.aws_ec2 import Vpc, SubnetType, SubnetConfiguration


class VPCStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
       
        subnet_conf = list()
        subnet_conf.append(SubnetConfiguration(cidr_mask=24, name='public', subnet_type=SubnetType.PUBLIC))

        vpc = Vpc(self, 'QuakeServicesVPC', 
                cidr='172.16.0.0/16',
                nat_gateways=0,
                subnet_configuration=subnet_conf)

