import boto3
import logging

#define the connection
ec2 = boto3.client('ec2')
regions = ec2.describe_regions().get('Regions',[] )
all_regions = [region['RegionName'] for region in regions]

def lambda_handler(event, context):
    # Use the filter() method of the instances collection to retrieve
    # all running EC2 instances.
    filters = [{
            'Name': 'instance-state-name', 
            'Values': ['running']
        }
    ]
    for region_name in all_regions:
            print('Instances in EC2 Region {0}:'.format(region_name))
            ec2 = boto3.resource('ec2', region_name=region_name)
            #filter the instances
            instances = ec2.instances.filter(Filters=filters)

            #locate all running instances
            RunningInstances = [instance.id for instance in instances]
            
            #print RunningInstances 
            
            #to make sure there are actually instances to shut down. 
            if len(RunningInstances) > 0:
                #perform the shutdown
                shuttingDown = ec2.instances.filter(InstanceIds=RunningInstances).stop()
                print (shuttingDown)
            else:
                print ("Nothing to see here")