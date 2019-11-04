#!/usr/bin/env python3

from aws_cdk import core

from domains.domain_stack import DomainStack


app = core.App()
DomainStack(app, "DomainStack")

app.synth()
