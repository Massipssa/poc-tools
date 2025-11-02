from fastavro import reader, json_writer

if __name__ == '__main__':

    in_path = "warehouse/db/persons/metadata/snap-2093926769621697207-1-d9b53757-55a3-4f7e-80b6-926ce7edac4b.avro"
    out_path = "output.json"

    with open(in_path, "rb") as f_in:
        avro_reader = reader(f_in)
        schema = avro_reader.writer_schema
        records = list(avro_reader)

    with open(out_path, "w", encoding="utf-8") as f_out:
        json_writer(f_out, schema, records)

    print("✅ Conversion OK ->", out_path)
