import sys
import boto3
import botocore
import logging
filename = sys.argv[1]
outputfilename = sys.argv[2]
S3_BUCKET= sys.argv[3]

s3_resource = boto3.resource('s3')
try:
    s3_resource.Bucket(S3_BUCKET).download_file(filename, outputfilename)
except botocore.exceptions.ClientError as e:
    logging.error(e)
