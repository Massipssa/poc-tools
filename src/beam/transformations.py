import apache_beam as beam


class ComputeWordLengthFn(beam.DoFn):

    def process(self, elements):
        return [len(elements)]

if __name__ == '__main__':
    words = ["The first line", "The second line in the list", "And this is the last line"]

    # custom DoFn
    rst = words | beam.ParDo(ComputeWordLengthFn())
    print(rst)

    # flatMap
    rst = words | beam.FlatMap(lambda word: [len(word)])
    print(rst)
    """
    with beam.Pipeline() as pipeline:
        word_lengths = (pipeline
                       | "Count " >> beam.ParDo(ComputeWordLengthFn()))
    """