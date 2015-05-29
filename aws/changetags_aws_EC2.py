#python ./changetags_aws_EC2.py aws_access_key_id aws_secret_access_key instanceID tag newValueTag

import sys
import boto.ec2

if len(sys.argv) != 6:
	print("ie: python ./changetags_aws_EC2.py aws_access_key_id aws_secret_access_key instanceID tag newValueTag")
	sys.exit()

tag = sys.argv[4]
connected = True

try:
	#conn=boto.ec2.connect_to_region("eu-west-1")
	conn=boto.ec2.connect_to_region("eu-west-1", aws_access_key_id=sys.argv[1], aws_secret_access_key=sys.argv[2])
except:
	connected = False
	print("Not connected!")

if connected:
	reservations = conn.get_all_instances(sys.argv[3])
	instance = reservations[0].instances[0]

	if instance is not None:
		try:
			instance.remove_tag(tag, instance.tags[tag])
			instance.add_tag(tag, sys.argv[5])
			print("Old tag - " + " Key: " + tag + " Value: " + instance.tags[tag])
			print("New tag - " + " Key: " + tag + " Value: " + sys.argv[5])
		except:
			print("Error!")
