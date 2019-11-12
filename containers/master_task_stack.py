from aws_cdk import core
import aws_cdk.aws_ecs as ecs


class MasterTaskStack(core.Stack):

  def __init__(self, scope: core.Construct, id: str, cluster: ecs.Cluster, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
       
        self.cluster = cluster

        task = ecs.Ec2TaskDefinition(self, 'QuakeMasterTask',
            network_mode=ecs.NetworkMode.HOST)

        task.add_container('Master',
            image=ecs.ContainerImage.from_registry("amazon/amazon-ecs-sample"),
            memory_reservation_mib=256)

        service = ecs.Ec2Service(self, 'QuakeMasterService',
            cluster=self.cluster,
            task_definition=task)
