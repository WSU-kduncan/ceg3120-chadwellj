# Part 1 - Build a VPC

**1.Create a VPC.**
![VPC](images/VPC.png)
- VPC is a Virtual Network Cloud dedicated for our AWS accounts. It allows for launching of AWS recourses into a virtual network. Resembles a traditional network.

 **2.Create a subnet.**
![Subnet](images/SUBNET.png)
-

 **3.Create an internet gateway**
 ![gw](images/GW.png)

**4.Create a route table**
 ![RT](images/RT.png)

**5.Create a security group**
 ADD SCREENSHOT AFTER MODIFYING RULE ALLOWING FOR INSTANCE IN VBC


 # Part 2 - EC2 instances

 **1.Create a new instance. Give a write up of the following information:**
 - AMI selected: Ubuntu Linux/UNIX AMI
    - default username of the instacnce type selected: ubuntu
 ![default un](images/Capture.PNG)
- Instance type - t2.micro

 **2.Attach the instance to your VPC. As discussed there are different pathways to doing this. Say how you did it.**
 - On step 3 of setting up the instance "Configure Instance Details" we are able to select our previously made VPC, which is in the "Network" selection. Additionally, we slect our subnet. This attaches the VPC with our instance

  **3.Determine whether a Public IPv4 address will be auto-assigned to the instance. Justify your choice to do so (or not do so)**
  - We should not auto-assign IP when creating the instance. This is due to AWS potentially assigning and re-assigning a different IP at any time. Furthermore, we will be configuring / reserving an Elastic IP that will be associated with the instance. This IP will be static and will not have the chance of changing.

  **4.Attach a volume to your instance. As discussed there are different pathways to doing this. Say how you did it.**
  - In step 4 of instance creation "Add Storage" we are able to select the storage volume based off of what we had selected earlier. You have the options of multiple choices for volume types. This will attach the selected volume with the instance.

  **5.Tag your instance with a "Name" of "YOURLASTNAME-instance". Say how you did it..**
  - 




 







