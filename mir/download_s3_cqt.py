import boto3
import os

s3_resource = boto3.resource('s3')
bucketName = 'maestro-transforms'
bucket = s3_resource.Bucket(bucketName)
for fileID in range(1281):
    print(fileID)
    if fileID == 835:
        continue
    prefix = 'train' if fileID < 1000 else 'test'
    os.mkdir('{}/fileID{}'.format(prefix, fileID))
    bucket.download_file('{}/fileID{}/cqt.npy'.format(prefix, fileID), '{}/fileID{}/cqt.npy'.format(prefix, fileID))
    bucket.download_file('{}/fileID{}/annotation_label.npy'.format(prefix, fileID),'{}/fileID{}/annotation.npy'.format(prefix, fileID))