import boto3

session = boto3.Session(
aws_access_key_id="AKIAQI43KM7IESNEJQKK",
aws_secret_access_key="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"
)

# Print out bucket names
s3 = session.resource('s3')
for bucket in s3.buckets.all():
    print(bucket.name)

data = open('gitimage.png','rb')
s3.Bucket('abhi1bucket').put_object(Key='gitimage.png', Body=data)