from aws_cdk import core
import aws_cdk.aws_s3 as s3


class WebBucketStack(core.Stack):

  def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
       
        domains = ['quake.services',
                   'quake2.services',
                   'quake3.services']

        s3.Bucket(self, 'www.quake.services',
            bucket_name='www.quake.services')

        for domain in domains:
            name = f'apex_301_{domain}'
            s3.Bucket(self, name,
                bucket_name=domain,
                website_redirect=s3.RedirectTarget(host_name='www.quake.services'))
