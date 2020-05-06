'''
This file will define a function that will launch an EC2 instance..
'''

import boto3

userdata = '''#!/bin/bash
cd home/ubuntu
sudo -u ubuntu mkdir results
git clone https://github.com/MathiasDarr/MIR.git 
sudo mkdir MIR/test && sudo mkdir MIR/train
pip install librosa --user
'''

def launchEC2():
    REGION = 'us-west-2' # region to launch instance.

    INSTANCE_TYPE = 't2.micro'      # Test with the micro
    #INSTANCE_TYPE = 'g3s.xlarge' # instance type to launch.
    AMI = 'ami-01a4e5be5f289dd12'

    ec2 = boto3.resource('ec2', region_name=REGION)
    instances = ec2.create_instances(
        ImageId=AMI,
        MinCount=1,
        MaxCount=1,
        KeyName='gpu-style',
        InstanceInitiatedShutdownBehavior='terminate',
        IamInstanceProfile={'Name':'S3fullaccess'},
        InstanceType=INSTANCE_TYPE,
        SecurityGroupIds=['sg-03915a624fb5bf7bd'],
        UserData = userdata
    )
