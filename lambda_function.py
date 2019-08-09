import json
import boto3
# import psycopg2
import pg8000
def lambda_handler(event, context):
    
    # TODO implement
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_name = event['Records'][0]['s3']['object']['key']
    HOST='redshift-cluster-1.cntecmgvwt8l.us-west-2.redshift.amazonaws.com'
    DB_NAME='test'
    DB_USER='awsuser'
    DB_PASSWORD='Passw0rd'
    DB_PORT=5439
    ARN='arn:aws:iam::022331431550:role/dwhRole'
   
    try:
        conn = pg8000.connect(database=DB_NAME, host=HOST, port=DB_PORT, user=DB_USER, password=DB_PASSWORD, ssl=True)
        cur = conn.cursor()
    except Exception as err:
        print(err)
        
    try:
        cur.execute("DROP TABLE IF EXISTS address")
    except psycopg2.Error as e:
        print(e)
    conn.commit()
    try:
        cur.execute('''CREATE TABLE address(id INT IDENTITY(1,1),
                                    address TEXT,
                                    city TEXT,
                                    state TEXT,
                                    zip TEXT)''')
    except psycopg2.Error as e:
        print(e)
    conn.commit()
    
    qry = """
        copy address from 's3://{}/{}'
        credentials 
        'aws_access_key_id={};aws_secret_access_key={}'
         csv;
    """.format(bucket_name, file_name, <aws_access_key_id>, <aws_secret_access_key>)
    try:
        cur.execute(qry)
        print("Copy Command executed successfully")
    
    except psycopg2.Error as e:
        print(e)
    conn.commit()   
    delete_sql = '''delete from 
                    address
                    where id not in (select min(id) from address group by address,city,state,zip)'''

    try:
        cur.execute(delete_sql)
    except psycopg2.Error as e:
        print(e)
    conn.commit()
    conn.close()
    return {
        'statusCode': 200,
        'body': json.dumps('successfully worked')
    }
