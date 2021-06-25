from src.basics.data_struct import upper_names


def test_upper_names(names_list):
    assert(upper_names(names_list) == ["NAME1", "NAME2", "NAME5"])
