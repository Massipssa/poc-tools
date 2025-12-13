from fastavro import reader, json_writer

if __name__ == '__main__':

    in_path = "../warehouse/local/db_demo/metadata/snap-2869477313903844226-1-abf58eec-099e-4a18-a3d8-df20429efde5.avro"
    out_path = "data/snap-output.json"

    with open(in_path, "rb") as f_in:
        avro_reader = reader(f_in)
        schema = avro_reader.writer_schema
        records = list(avro_reader)

    with open(out_path, "w", encoding="utf-8") as f_out:
        json_writer(f_out, schema, records)

    print("✅ Conversion OK ->", out_path)
