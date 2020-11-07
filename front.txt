import os
import subprocess
print("\t\t\t\t\tNAMASTE")
print("\t\t\t!!Welcome to our menu script program!!")
print("Menu")
print("1)Hadoop\n 1.1) Setup Cluster\n\n2)AWS ")


print("3)SSH(connect remotely)\n\n4)SCP(transfer files)")
print("\n5)Configure Webserver")
p = input("\t\t\t    Enter your requirement:")
if int(p) == 1:
	print('\t\t\t "Welcome to Hadoop environment"')
	z = input("want to setup hadoop cluster(y/n)?")
	if z == "y":
		print("For hadoop cluster")
		print("Namenode\nstarting namenode service")
		os.system("ssh 192.168.43.98 hadoop-daemon.sh start namenode")
		os.system("ssh 192.168.43.98 systemctl stop firewalld")
		print("Your Namenode Started")
		print("Datanode\nstarting datanode service")
		t = int(input("Number of datanode you need(1/2/3)?"))
		if t == 1:
			os.system("hadoop-daemon.sh start datanode")
		elif t == 2:
			os.system("hadoop-daemon.sh start datanode")
			os.system("ssh ip hadoop-daemon.sh start datanode")
		else :
			os.system("hadoop-daemon.sh start datanode")
			os.system("ssh ip hadoop-daemon.sh start datanode")
			os.system("ssh ip hadoop-daemon.sh start datanode")
		print("check your cluster")
		os.system("ssh 192.168.43.98 hadoop dfsadmin -report | less")
elif int(p) == 2:
	print(" 2.1) Create a Key pair\n 2.2) Create a security Group\n 2.3) Launch a new instance\n 2.4) Create EBS volume\n 2.5) Attach the EBS volume to the instance\n 2.6) Create a new bucket")

	print(" 2.7) Upload object to a bucket \n 2.8) Set up cloud front network\n 2.9) List details of all instances\n 2.10)List details of all Security groups\n 2.11) List details of all Keypairs\n 2.12) List all the buckets.\n 2.13) List details of volumes\n 2.14) exit\n\n\n")
	n = float(input("Enter your choice:"))
	if(n == 2.1):
		kname = input("Enter a name for your key:")
		z = subprocess.getoutput( "aws ec2 create-key-pair --key-name {}".format(kname))
		print(z)
	elif(n==2.2):
        	sname=input("Give a name to security group:")
        	desc=input("give a description(please give description in " "):")
        	vpc=input("enter vpcid for creating security group:")
        	z=subprocess.getoutput("aws ec2 create-security-group --group-name {} --description {} --vpc-id {}".format(sname,desc,vpc))
        	print(z)
	elif(n==2.3):
        	img_id=input("please enter image id:")
        	instance_type=input("please enter Instance type:")
        	kname=input("please enter key name:")
        	sg_id=input("please enter security group_id:")
        	count=int(input("enter number of instances:"))
        	s_id=input("please enter subnet id:")
        	z=subprocess.getoutput("aws ec2 run-instances --image-id {} --instance-type {} --key-name {} --security-group-ids {} --count {} --subnet-id {} ".format(img_id,instance_type,kname,sg_id,count,s_id))
        	print(z)
	elif(n==2.4):
        	az=input("please enter availability zone:")
        	v_type=input("please enter volume (gp2,standard,io1,1o2,etc.) type:")
        	size=int(input("enter size of the volume:"))
        	z=subprocess.getoutput("aws ec2 create-volume --availability-zone {} --size {}  --volume-type {}".format(az,size,v_type))
        	print(z)
	elif(n==2.5):
        	instance_id=input("please enter id of the instance to connect:")
        	volume_id=input("please enter id of the volume to be connected:")
        	z=subprocess.getoutput("aws ec2 attach-volume --volume-id {} --instance-id {}".format(instance_id,volume_id))
        	print(z)
	elif(n==2.6):
        	print("Bucket will be launched with the public access")
        	bname=input("please enter a unique bucket name:")
        	region=input("please enter region of the bucket:")
        	z=subprocess.getoutput("aws s3api create-bucket --bucket {} --region {} --acl public-read".format(bname,region))
        	print(z)
	elif(n==2.7):
        	print("It will be more preferred  to put the file to be uploaded be in the same location and directly use the file name\n\n")
        	bname=input("please enter bucket name:")
        	floc=input("please enter full path location of the file:")
        	z=subprocess.getoutput("aws s3 cp {} s3://{} --acl public-read".format(floc,bname))
        	print(z)
	elif(n==2.8):
        	dname=input("please enter domain name to create cloudfront:")
        	z=subprocess.getoutput("aws cloudfront create-distribution --origin-domain-name {}".format(dname))
        	print(z)
	elif(n==2.9):
        	z=subprocess.getoutput("aws ec2 describe-instances ")
        	print(z) 
	elif(n==2.10):
        	z=subprocess.getoutput("aws ec2 describe-security-groups ")
        	print(z)
	elif(n==2.11):
        	z=subprocess.getoutput("aws ec2 describe-key-pairs ")
        	print(z)
	elif(n==2.12):
        	z=subprocess.getoutput("aws ec2 s3api list-buckets ")
        	print(z)
	elif(n==2.13):
        	z=subprocess.getoutput("aws ec2 describe-volumes ")
        	print(z)
	elif(n==2.14):
        	exit()

elif int(p) == 3:
	print("Connect Remotely")
	ip = input("Enter your ip here:")
	os.system("ssh {}".format(ip))

elif int(p) == 4:
	print("transfer files")
	ip = input("Enter your ip here:")
	fl = input("Enter file location:")
	os.system("scp {} {}:/root".format(fl,ip))
elif int(p) == 5:
	print("Configure Webserver")
	print("""a. Start Webserver\nb. Stop Webserver\nc. Create a Webpage \nd. ReStart Webserver""")
	_in = input("Enter Your Choice:")
	
	if _in == "a":
		os.system("systemctl start httpd")
	elif _in == "b":
		os.system("systemctl stop httpd")
	elif _in == "c":
		filein = input("Enter File Name:")
		os.system("vi /var/www/html/ {0}".format(filein))
	elif _in == "d":
		os.system("systemctl restart httpd")
	else:
		print("Wrong Input or Error")
else:
	print("sorry:)")




	








		

