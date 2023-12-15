import os

from google.cloud import storage

from src.gcp.composer.util import read_variables_file_from_bucket, write_file_to_bucket, write_tmp_file

BUCKET_NAME = "testmkeimport"
BASE_DIR = "data"
FILE_NAME_1 = "var_file_1.json"
FILE_NAME_2 = "var_file_2.json"
OUTPUT_FILE = "fusion_composer_variables.json"

if __name__ == "__main__":

    gcs_client = storage.Client()
    variables_composer_2 = {}

    # get variables file
    variable_content_1 = read_variables_file_from_bucket(gcs_client, BUCKET_NAME, BASE_DIR, FILE_NAME_1)
    variable_content_2 = read_variables_file_from_bucket(gcs_client, BUCKET_NAME, BASE_DIR, FILE_NAME_2)

    # compute different keys
    different_keys = set(variable_content_1.keys()) ^ set(variable_content_2.keys())
    different_items = {key: variable_content_1[key] for key in different_keys if key in variable_content_1} \
                      | {key: variable_content_2[key] for key in different_keys if key in variable_content_2}

    # add different keys in dict
    for key, value in different_items.items():
        variables_composer_2[key] = value

    # compute same keys
    common_elements = list(set(variable_content_1).intersection(variable_content_2))
    for k in common_elements:
        # same keys different values
        if variable_content_1[k] != variable_content_2[k]:
            # don't prefix variable coming from file1
            key_var_1 = k
            variables_composer_2[key_var_1] = variable_content_1[k]

            # prefix variable coming from file2
            key_var_2 = f"{k}_2"
            variables_composer_2[key_var_2] = variable_content_2[k]

        # same keys, same values
        else:
            variables_composer_2[k] = variable_content_1[k]

    # create tmp file
    write_tmp_file(OUTPUT_FILE, variables_composer_2)

    # write files to bucket
    write_file_to_bucket(gcs_client, BUCKET_NAME, BASE_DIR, OUTPUT_FILE)

    # delete tmp file
    if os.path.exists(OUTPUT_FILE):
        os.remove(OUTPUT_FILE)
