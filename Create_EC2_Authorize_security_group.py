#1a) ) Aws credentials which has acces key & Secret key must be saved in respective home directory to access aws acccount from command line

# b)  #Script to launch ec2 & authorize security_group using boto

import boto3

#To Create a conn object to connect ec2 session 
conn=boto3.client('ec2')
response=conn.create_security_group(GroupName='mydefalultsecgroup' , Description='testEC2Instancegroup')
print response #will get Group ID

#authorize security group
conn.authorize_security_group_ingress(
           GroupID=response['GroupID'], 
           IpProtocol='tcp', CidrIp='0.0.0.0/0', 
           FromPort=22, 
           ToPort=22
           )
#To create Key Pair Object
keypair=conn.create_keypair(KeyName='webkey')

#To Create Ec2 resource  Object
ec2_conn = boto3.resource('ec2')
instance = ec2_conn.create_instances(
      ImageId='ami-e13739f6',
      MinCount=1,
      MaxCount=2,
      SecurityGroups=[
        'mydefalultsecgroup',
      ],
       KeyName='webkey', InstanceType='t2.micro')

print instance