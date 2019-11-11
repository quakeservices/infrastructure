from aws_cdk import core
import aws_cdk.aws_ecs as ecs
import aws_cdk.aws_ec2 as ec2


class MasterTaskStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
       
        vpc = ec2.Vpc.from_lookup(self,
                                  'QuakeServicesVPC',
                                  vpc_name='VPCStack/QuakeServicesVPC')


        cluster = ecs.from_cluster_attributes(self, 'QuakeServices',
                cluster_name='QuakeServicesECS',
                vpc=vpc)

        task = ecs.Ec2TaskDefinition(self, 'QuakeMasterTask',
            network_mode=ecs.NetworkMode.HOST,
            compatibility=ecs.Compatibility.EC2)

        task.add_container('Master',
            image='TBD')

        service = ecs.Ec2Service(self, 'QuakeMasterService',
            cluster=cluster,
            task_definition=task)
