const fs = require('fs');
const AWS = require('aws-sdk');

const BUCKET_NAME = '';
const IAM_USER_KEY = '';
const IAM_USER_SECRET = '';
const s3 = new AWS.S3({
    accessKeyId: IAM_USER_KEY,
    secretAccessKey:IAM_USER_SECRET,
});

const fileName = 'address.csv';

  fs.readFile(fileName,"utf8", (err, data) => {
    //   console.log(data)
     if (err) throw err;
     const params = {
         Bucket: BUCKET_NAME,
         Key: fileName, 
         Body: data,
     };
     s3.upload(params, function(s3Err, data) {
         if (s3Err) throw s3Err
         console.log(`CSV file is uploaded successfully at ${data.Location}`)
     });
  });
