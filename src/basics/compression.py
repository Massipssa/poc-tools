import logging
import tempfile

log = logging.getLogger(__name__)


def uncompress_file():
    pass


def create_temp_file():
    line_1 = b"line_1"
    line_2 = b"line_2"
    line_3 = b"line_3"

    tmp_dir = tempfile.mkdtemp(prefix="temp_dir_")
    with tempfile.NamedTemporaryFile(mode='wb+', dir=tmp_dir, delete=False) as tmp_file:
        log.debug(f"Tmp file name {tmp_file.name}")
        tmp_file.writelines([line_1, line_2, line_3])
