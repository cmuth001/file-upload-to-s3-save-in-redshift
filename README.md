# file-upload-to-s3-save-in-redshift


In this tutorial I will explain how to upload a CSV file into S3 bucket, trigger lambda function extract the CSV file from S3 and copy all the unique values in Apache Redshift cluster.

I will split this tutorial into three sections:

* Setting up permissions for S3 bucket  and trigger functions.
* Uploading a CSV file into AWS S3 bucket using Node.js.
* Lambda function: processing the CSV file and storing it onto Redshift cluster.

# Setting up permissions for S3 bucket  and trigger functions.
### Setting up AWS-S3 Bucket

1. Login to [AWS console](https://aws.amazon.com). Click Services and select **S3** .

    <p align="center">
        <img
          alt="AWS-S3 Service"
          src="images/1.png"
          width="800"
        />
    </p>

2. Click **Create Bucket** and follow screenshots as shown below.
    <p align="center">
        <img
          alt="Create Bucket"
          src="images/2.png"
          width="800"
        />
    </p>
    <p align="center">
        <img
          alt="Bucket Name"
          src="images/3.png"
          width="800"
        />
    </p>
    <p align="center">
        <img
          alt="Configure Options"
          src="images/4.png"
          width="800"
        />
    </p>
    <p align="center">
        <img
          alt="Bucket Permissions"
          src="images/5.png"
          width="800"
        />
    </p>
    <p align="center">
        <img
          alt="Review Bucket settings"
          src="images/6.png"
          width="800"
        />
    </p>
    
3. Select the created bucket in the bucket list.
    
    <p align="center">
        <img
          alt="Inside Created Bucket"
          src="images/7.png"
          width="800"
        />
    </p>
    
4. Click **Permissions**
    
    **Bucket Policy**  as shown in the figure below. 
     
     Copy the below Json into Bucket Policy.
     
     ```json
     {
        "Version": "2012-10-17",
        "Id": "Policy1488494182833",
        "Statement": [
            {
                "Sid": "Stmt1488493308547",
                "Effect": "Allow",
                "Principal": {
                    "AWS": "arn:aws:iam::022331431550:user/salesboomerang-user"
                },
                "Action": [
                    "s3:ListBucket",
                    "s3:ListBucketVersions",
                    "s3:GetBucketLocation",
                    "s3:Get*",
                    "s3:Put*"
                ],
                "Resource": "arn:aws:s3:::samplebucket-001"
            }
        ]
    }
    ```
      <p align="center">
          <img
            alt="Permissions"
            src="images/8.png"
            width="800"
          />
      </p>
    
      
    
    **CORS Configuration**  as shown in the figure below.
    
    Copy the below Json into CORS Configuration.
    
    ```xml
    <?xml version="1.0" encoding="UTF-8"?>
    <CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
    <CORSRule>
        <AllowedOrigin>*</AllowedOrigin>
        <AllowedMethod>GET</AllowedMethod>
        <AllowedMethod>POST</AllowedMethod>
        <AllowedMethod>PUT</AllowedMethod>
        <MaxAgeSeconds>3000</MaxAgeSeconds>
        <AllowedHeader>Authorization</AllowedHeader>
    </CORSRule>
    </CORSConfiguration>
    ```

      <p align="center">
          <img
            alt="CORS Configuration"
            src="images/9.png"
            width="800"
          />
      </p>
   
### Setting up AWS-S3 Bucket

1. Now click Services then go to **IAM** services.

  <p align="center">
    <img
        alt="CORS Configuration"
        src="images/iam-1.png"
        width="800"
    />
  </p>
  
2. Now on the left side click **Users**

   <p align="center">
        <img
        alt="CORS Configuration"
        src="images/iam-2.png"
        width="800"
    />
  </p>
  
3. Now click **Add user**  and follow the below steps to create a user.

    <p align="center">
        <img
            alt="CORS Configuration"
            src="images/iam-2.png"
            width="800"
        />
    </p>

    <p align="center">
        <img
            alt="CORS Configuration"
            src="images/iam-3.png"
            width="800"
        />
    </p>
    
    <p align="center">
        <img
            alt="CORS Configuration"
            src="images/iam-4.png"
            width="800"
        />
    </p>
    
    <p align="center">
        <img
            alt="CORS Configuration"
            src="images/iam-5.png"
            width="800"
        />
    </p>
    <p align="center">
        <img
            alt="CORS Configuration"
            src="images/iam-6.png"
            width="800"
        />
    </p>
    <p align="center">
        <img
            alt="CORS Configuration"
            src="images/iam-7.png"
            width="800"
        />
    </p>
    <p align="center">
        <img
            alt="CORS Configuration"
            src="images/iam-8.png"
            width="800"
        />
    </p>
    <p align="center">
        <img
            alt="CORS Configuration"
            src="images/iam-9.png"
            width="800"
        />
    </p>
    <p align="center">
        <img
            alt="CORS Configuration"
            src="images/iam-10.png"
            width="800"
        />
    </p>
    <p align="center">
        <img
            alt="CORS Configuration"
            src="images/iam-11.png"
            width="800"
        />
    </p>
    <p align="center">
        <img
            alt="CORS Configuration"
            src="images/iam-12.png"
            width="800"
        />
    </p>
    <p align="center">
        <img
            alt="CORS Configuration"
            src="images/iam-13.png"
            width="800"
        />
    </p>
    <p align="center">
        <img
            alt="CORS Configuration"
            src="images/iam-14.png"
            width="800"
        />
    </p>
    <p align="center">
        <img
            alt="CORS Configuration"
            src="images/iam-15.png"
            width="800"
        />
    </p>
    <p align="center">
        <img
            alt="CORS Configuration"
            src="images/iam-16.png"
            width="800"
        />
    </p>
    <p align="center">
        <img
            alt="CORS Configuration"
            src="images/iam-17.png"
            width="800"
        />
    </p>
    <p align="center">
        <img
            alt="CORS Configuration"
            src="images/iam-18.png"
            width="800"
        />
    </p>
    <p align="center">
        <img
            alt="CORS Configuration"
            src="images/iam-19.png"
            width="800"
        />
    </p>
    <p align="center">
        <img
            alt="CORS Configuration"
            src="images/iam-20.png"
            width="800"
        />
    </p>
## Uploading a CSV file into AWS S3 bucket using Node.js:

### Installing dependency
    > npm install aws-sdk --save
In the next few steps I will be explaining how to build a node.js application which will helps in uploading a local file into S3 bucket.

1. Create a project directory using below command.
    > mkdir file-upload-to-s3-save-in-redshift
2. Running this command in **file-upload-to-s3-save-in-redshift**  will initialize node project.
    > npm init
3. Lets create a index.js which will be useful for writing a node.js code to upload csv file to S3.
    > touch index.js
4. Install dependency package called aws-sdk from node package manager(npm)
    > npm install --save aws-sdk

