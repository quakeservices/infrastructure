from aws_cdk import core
import aws_cdk.aws_ecs as ecs
import aws_cdk.aws_ec2 as ec2


class ECSStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, vpc=None, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
       
        cluster = ecs.Cluster(self, 'QuakeServices',
                cluster_name='QuakeServicesECS',
                vpc=vpc)

        cluster.add_capacity('DefaultAutoScalingGroupCapacity',
                instance_type=ec2.InstanceType('t3.micro'),
                desired_capacity=3,
                max_capacity=6,
                min_capacity=2)

