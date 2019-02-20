Language : python3
Infra : AWS LAMBDA FUNCTION

Prerequisite:
1. You must have AWS account.
2. Create lambda function , select python3 as infra.
3. Create a policy which has access to poweron and poweroff ec2 instances. 
   - Please find required policy in this folder.
4. Create a role for Lambda function and attach this policy.


Use Cases:

1. To poweroff all running instances after certain amount of time.
=> We can also use this as auto poweroff scheduler. 
   Steps:
         a. Create rule in cloudwatch.
         b. Select Fixed rate of and enter duration.
         c. Add this lambda function in Target section

2. To poweroff instances after office timing.
=> Steps are similar to first use case. You just need select instead of Fixed rate of.

## There can be many more. 

