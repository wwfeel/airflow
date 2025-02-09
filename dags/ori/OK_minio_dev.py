from minio import Minio

client = Minio(
    "127.0.0.1:9000",
    access_key="hHGFCTLsiSbZ6eMPA4JZ",
    secret_key="2LmSJEGsk6y8LAvMIzfofSzNxdwq5hLWA7W5qHXW",
    secure=False
)

buckets = client.list_buckets()
for bucket in buckets:
    print(bucket.name, bucket.creation_date)

# List objects information.
objects = client.list_objects("pluto-fps")
for obj in objects:
    print(obj)    