from constructs import Construct
from aws_cdk import (
    Stack,
    aws_sns_subscriptions as subs,
    aws_s3 as s3,
    aws_ec2 as ec2,
    aws_ecs as ecs,
    aws_ecs_patterns as ecs_patterns
)


class AwsCdkLearningStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # queue = sqs.Queue(
        #     self, "AwsCdkLearningQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )

        # topic = sns.Topic(
        #     self, "AwsCdkLearningTopic"
        # )

        # topic.add_subscription(subs.SqsSubscription(queue))

        bucket = s3.Bucket(self, "MyFirstBucket-2021-cvfbsb")

        amzn_linux = ec2.MachineImage.latest_amazon_linux(
            generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX,
            edition=ec2.AmazonLinuxEdition.STANDARD,
            virtualization=ec2.AmazonLinuxVirt.HVM,
            storage=ec2.AmazonLinuxStorage.GENERAL_PURPOSE,
            cpu_type=ec2.AmazonLinuxCpuType.X86_64
        )

        ec2_instances = ec2.Instance(self, "Instance",
            vpc = ec2.Vpc(self, "VPC"),
            instance_type = ec2.InstanceType("t2.micro"),
            machine_image = amzn_linux,
        )

        cluster = ecs.Cluster(self, "MyCluster", vpc=ec2.Vpc(self, "MyVpc", max_azs=3))

        ecs_patterns.ApplicationLoadBalancedFargateService(self, "MyFargateService",
            cluster=cluster,
            cpu=512,
            desired_count=6,
            task_image_options=ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
                image=ecs.ContainerImage.from_registry("amazon/amazon-ecs-sample")),
            memory_limit_mib=2048,
            public_load_balancer=True)



