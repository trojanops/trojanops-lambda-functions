Note: This function works on python3.

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

