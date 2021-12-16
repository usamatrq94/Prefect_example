#!/usr/bin/env python3

import aws_cdk as cdk

from aws_cdk_learning.aws_cdk_learning_stack import AwsCdkLearningStack


app = cdk.App()
AwsCdkLearningStack(app, "aws-cdk-learning")

app.synth()
