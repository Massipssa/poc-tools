import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
import argparse

class Options(PipelineOptions):
    @classmethod
    def _add_argparse_args(cls, parser):
        parser.add_argument('--input')
        parser.add_argument('--output')


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input-path",
        default="data/test.txt",
        help="Input path"
    )
    beam_options = PipelineOptions()
    with beam.Pipeline() as pipeline:
        #lines = pipeline | "ReadTextFile" >> beam.io.ReadFromText(file_path)
        # create in-memory PCollection
        in_memory_lines = (
                pipeline
                | "Create elements" >> beam.Create(["line1", "line2", "line3"])
                | "Print elements" >> beam.Map(print))
        pipeline.run().wait_until_finish()



