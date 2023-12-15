def hash_partition(data, num_partitions):
    partitions = {}
    for entry in data:
        hash_code = hash(entry) % num_partitions
        if hash_code not in partitions:
            partitions[hash_code] = []
        partitions[hash_code].append(entry)
    return partitions


if "__name__" == "__main__":

    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    num_partitions = 3

    result = hash_partition(data, num_partitions)
    print(result)