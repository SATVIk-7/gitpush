import os
import subprocess
print("\n\n\t\t\t\t\t\t Welcome to AWS Configuration\n\n")
print("IMPORTANT::Your command prompt or terminal should be AWS cofigured\n\n\n")
while(True):

    print("Please select any of the option:\n\n\n1.Create a Key pair\n2.Create a security Group\n3.Launch a new instance\n4.Create EBS volume\n5.Attach the EBS volume to the instance\n6.Create a new bucket")
    print("7.Upload object to a bucket \n8.Set up cloud front network\n9.List details of all instances\n10.List details of all Security groups\n11.List details of all Keypairs\n12.List all the buckets.\n13.List details of volumes\n14.exit\n\n\n")
n = int(input("Enter your choice:"))
if(n == 1):
kname = input("Enter a name for your key:")
z = subprocess.getoutput( "aws ec2 create-key-pair --key-name {}".format(kname))
print(z)
    elif(n==2):
        sname=input("Give a name to security group:")
        desc=input("give a description(please give description in " "):")
        vpc=input("enter vpcid for creating security group:")
        z=subprocess.getoutput("aws ec2 create-security-group --group-name {} --description {} --vpc-id {}".format(sname,desc,vpc))
        print(z)
    elif(n==3):
        img_id=input("please enter image id:")
        instance_type=input("please enter Instance type:")
        kname=input("please enter key name:")
        sg_id=input("please enter security group_id:")
        count=int(input("enter number of instances:"))
        s_id=input("please enter subnet id:")
        z=subprocess.getoutput("aws ec2 run-instances --image-id {} --instance-type {} --key-name {} --security-group-ids {} --count {} --subnet-id {} ".format(img_id,instance_type,kname,sg_id,count,s_id))
        print(z)
    elif(n==4):
        az=input("please enter availability zone:")
        v_type=input("please enter volume (gp2,standard,io1,1o2,etc.) type:")
        size=int(input("enter size of the volume:"))
        z=subprocess.getoutput("aws ec2 create-volume --availability-zone {} --size {}  --volume-type {}".format(az,size,v_type))
        print(z)
    elif(n==5):
        instance_id=input("please enter id of the instance to connect:")
        volume_id=input("please enter id of the volume to be connected:")
        z=subprocess.getoutput("aws ec2 attach-volume --volume-id {} --instance-id {}".format(instance_id,volume_id))
        print(z)
    elif(n==6):
        print("Bucket will be launched with the public access")
        bname=input("please enter a unique bucket name:")
        region=input("please enter region of the bucket:")
        z=subprocess.getoutput("aws s3api create-bucket --bucket {} --region {} --acl public-read".format(bname,region))
        print(z)
    elif(n==7):
        print("It will be more preferred  to put the file to be uploaded be in the same location and directly use the file name\n\n")
        bname=input("please enter bucket name:")
        floc=input("please enter full path location of the file:")
        z=subprocess.getoutput("aws s3 cp {} s3://{} --acl public-read".format(floc,bname))
        print(z)
    elif(n==8):
        dname=input("please enter domain name to create cloudfront:")
        z=subprocess.getoutput("aws cloudfront create-distribution --origin-domain-name {}".format(dname))
        print(z)
    elif(n==9):
        z=subprocess.getoutput("aws ec2 describe-instances ")
        print(z)
    elif(n==10):
        z=subprocess.getoutput("aws ec2 describe-security-groups ")
        print(z)
    elif(n==11):
        z=subprocess.getoutput("aws ec2 describe-key-pairs ")
        print(z)
    elif(n==12):
        z=subprocess.getoutput("aws ec2 s3api list-buckets ")
        print(z)
    elif(n==13):
        z=subprocess.getoutput("aws ec2 describe-volumes ")
        print(z)
    elif(n==14):
        exit()
