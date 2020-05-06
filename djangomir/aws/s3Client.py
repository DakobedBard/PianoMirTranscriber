import sys
import boto3
import botocore
import logging
from botocore.exceptions import ClientError
import os
from django.contrib.auth import get_user_model
User = get_user_model()

class s3Client:
    def __init__(self, bucketname):
        self.bucket = bucketname



    def upload_file(self,file_name, object_name):
        """Upload a file to an S3 bucket
        :param file_name: File to upload
        :param bucket: Bucket to upload to
        :param object_name: S3 object name. If not specified then file_name is used
        :return: returns the document object if uploaded to S3.  If the upload fails will return a -1.
        """
        # If S3 object_name was not specified, use file_name
        if object_name is None:
            object_name = file_name

        # Upload the file
        s3_client = boto3.client('s3')
        try:
            with open("/usr/src/app" + file_name, "rb") as f:
                print("I open the file " + str(file_name))
                s3_client.upload_fileobj(f, self.bucket, object_name)

                return 1
        except ClientError as e:
            logging.error(e)
            print(e)
            return -1
        return -1

    def upload_directory(self, directory_name, object_name):


        pass


    def download(self, object_name ):
        """Upload a file to an S3 bucket
        :param file_name: File to upload
        :param bucket: Bucket to upload to
        :param object_name: S3 object name. If not specified then file_name is used
        :return: True if file was downloaded, else False
        """
        s3 = boto3.client('s3')
        try:
            s3.download_file(self.bucket, object_name, 'mediafiles/download.mp3')
        except ClientError as e:
            logging.error(e)
            print(e)
            return False
        return True

    def delete(self, object_name):
        s3 = boto3.resource('s3')
        #return s3.get_bucket_acl(Bucket='basedjango')
        try:
            obj = s3.Object(self.bucket, object_name)
            print("The objec name " + object_name)
            obj.delete()
            #s3.delete_object(Bucket=self.bucket, Key=object_name)
        except ClientError as e:
            logging.error(e)
            print(e)
            return False
        return True


    def setBucketName(self, bucketname):
        self.bucket = bucketname
        client = boto3.client('iam')




