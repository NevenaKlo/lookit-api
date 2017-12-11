import sys
import boto3
import botocore
from project import settings


def get_all_study_attachments(study_uuid):
    '''
    Get all video responses to a study by fetching all objects in the bucket with
    key name videoStream_<study_uuid>
    '''
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(settings.BUCKET_NAME)
    return bucket.objects.filter(Prefix=f'videoStream_{study_uuid}')


def get_consent_videos(study_uuid):
        '''
        Get all consent videos for a particular study
        '''
        s3 = boto3.resource('s3')
        bucket = s3.Bucket(settings.BUCKET_NAME)
        return [att for att in bucket.objects.filter(Prefix=f'videoStream_{study_uuid}_1-video-consent') if 'PREVIEW_DATA_DISREGARD' not in att.key]


def get_download_url(video_key):
    '''
    Generate a presigned url for the video that expires in 60 seconds.
    '''
    s3Client = boto3.client('s3')
    return s3Client.generate_presigned_url('get_object', Params = {'Bucket': settings.BUCKET_NAME, 'Key': video_key}, ExpiresIn = 60)


def get_study_attachments(study, orderby='key', match=None):
    '''
    Fetches study attachments from s3
    '''
    sort = 'last_modified' if 'date_modified' in orderby else 'key'
    attachments = [att for att in get_all_study_attachments(str(study.uuid)) if 'PREVIEW_DATA_DISREGARD' not in att.key]
    if match:
        attachments = [att for att in attachments if match in att.key]
    return sorted(attachments, key=lambda x: getattr(x, sort), reverse=True if '-' in orderby else False)