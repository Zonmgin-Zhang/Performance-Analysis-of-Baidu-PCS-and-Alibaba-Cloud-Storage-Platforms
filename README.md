# Performance-Analysis-of-Baidu-PCS-and-Alibaba-Cloud-Storage-Platforms

Here is a guideline to achieve our experiments before on Baidu PCS and Alibaba Cloud:

## Baidu PCS:
1. Install the required package by running the script under the bypy-master directory:
<img width="245" alt="image" src="https://user-images.githubusercontent.com/85326183/235118543-7501e58c-7ba8-41be-838c-45dc02b47744.png">
Or
<img width="245" alt="image" src="https://user-images.githubusercontent.com/85326183/235118430-927adc51-bab2-4dd9-bfb4-a56378418606.png">

2.	Login to your Baidu account by running the below command under the bypy-master directory:

<img width="234" alt="image" src="https://user-images.githubusercontent.com/85326183/235118633-a37450cf-dc7b-406b-a2e5-8a22ae5d6cce.png">

Then, you will see the message below: 

<img width="420" alt="image" src="https://user-images.githubusercontent.com/85326183/235118620-8bae0cc6-e35b-4b85-94d9-ce723f58b1b3.png">
 Go to the link above (https://openapi.baidu.com/oauth/2.0/authorize?client_id=q8WE4EpCsau1oS0MplgMKNBn&response_type=code&redirect_uri=oob&scope=basic+netdisk), and log in your account.
 
 
3.	Test uploading and downloading by running the following command, and you can customer different data size for testing:
<img width="350" alt="image" src="https://user-images.githubusercontent.com/85326183/235118725-71703e7d-d9c6-4d7a-8992-5dcdbd6b32e1.png">
 Then, you can see the results of the duration time in the terminal, which are similar to those below:
 <img width="420" alt="image" src="https://user-images.githubusercontent.com/85326183/235118892-61fce0d7-fac0-45e9-85fc-91010abced7c.png">

## Alibaba Cloud:
1. Install the required package by running the script under the aliyunapi directory:
<img width="244" alt="image" src="https://user-images.githubusercontent.com/85326183/235118975-b58eed85-d3c3-4e3f-98ba-eb18528cbbd1.png">

2. Login to your Baidu account by running the below command under the aliyunapi directory:
<img width="196" alt="image" src="https://user-images.githubusercontent.com/85326183/235119027-0fce54b1-1e67-4264-bbd2-a04b49b2493c.png">
It will pop up a QR code to scan to log in shown below: 
<img width="206" alt="image" src="https://user-images.githubusercontent.com/85326183/235119054-6cce076a-8a7c-468e-bd67-e5fa3c712e2b.png">

3. Run the command to test uploading and downloading as below, and you can customer different data size for testing:
<img width="196" alt="image" src="https://user-images.githubusercontent.com/85326183/235119106-c39e43dc-e381-4550-8241-c910ea3ecbeb.png">
When it starts, you will see the following result; when it finishes, it will say "finished."
<img width="193" alt="image" src="https://user-images.githubusercontent.com/85326183/235119148-f2f7788b-ad28-4cd3-a09e-290acb2fef06.png">





