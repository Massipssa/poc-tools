import json


def read_variables_file_from_bucket(client, bucket_name: str, base_dir: str, file_name: str):
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(f"{base_dir}/{file_name}")
    file_contents = blob.download_as_text()
    return json.loads(file_contents)


def write_file_to_bucket(client, bucket_name: str, base_dir: str, file_name: str):
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(f"{base_dir}/{file_name}")
    blob.upload_from_filename(file_name)


def write_tmp_file(file_name: str, dict_variables):
    with open(file_name, "w") as file:
        json.dump(dict_variables, file)
