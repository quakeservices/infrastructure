from aws_cdk import core
import aws_cdk.aws_s3 as s3
import aws_cdk.aws_ec2 as ec2
import aws_cdk.aws_elasticloadbalancingv2 as elb
import aws_cdk.aws_autoscaling as autoscaling


class NLBStack(core.Stack):

  def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
     
        master_port = 27900
        master_check = 8080

        vpc = ec2.Vpc.from_lookup(self,
                                  'QuakeServicesVPC',
                                  vpc_name='VPCStack/QuakeServicesVPC')

        lb = elb.NetworkLoadBalancer(self, 'QuakeServicesNLB',
            vpc=vpc,
            internet_facing=True,
            cross_zone_enable=True)

        listener = lb.add_listener('Listener',
            port=master_port,
            protocol=elb.Protocol.UDP)

        health_check = elb.HealthCheck('HealthCheck', 
            healthy_http_codes='200',
            port=master_check,
            protocol=elb.Protocol.HTTP)

        listener.add_targets('Target',
            port=master_port,
            proxy_protocol_v2=True,
            health_check=health_check)
