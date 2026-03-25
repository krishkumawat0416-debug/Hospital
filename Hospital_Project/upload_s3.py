import boto3
import os


# bucket create karne ka function
def create_bucket(client, name, region):
    try:
        client.create_bucket(
            Bucket=name,
            CreateBucketConfiguration={"LocationConstraint": region}
        )
        print("Bucket created:", name)
    except Exception as e:
        print("Bucket error:", e)


# file upload karne ka function
def upload(client, path, bucket):
    file_name = os.path.basename(path)
    try:
        client.upload_file(path, bucket, file_name)
        print("Uploaded:", file_name)
    except Exception as e:
        print("Upload error:", e)


# main function
def main():
    bucket = input("Bucket: ")
    path = input("File path: ")

    # 🔑 user se credentials lena
    access_key = input("Access Key: ")
    secret_key = input("Secret Key: ")

    # boto3 client with user-defined credentials
    s3 = boto3.client(
        "s3",
        region_name="ap-south-1",
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key
    )

    create_bucket(s3, bucket, "ap-south-1")
    upload(s3, path, bucket)


if __name__ == "__main__":
    main()