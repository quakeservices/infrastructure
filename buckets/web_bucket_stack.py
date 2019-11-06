from aws_cdk import core
import aws_cdk.aws_s3 as s3


class WebBucketStack(core.Stack):

  def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
       
        domains = ['quake.services',
                   'quake2.services',
                   'quake3.services']

        for domain in domains:
            name = f'apex_301_{domain}'
            s3.bucket(self, name,
                website_redirect={'hostname_name': f'www.{domain}'})
