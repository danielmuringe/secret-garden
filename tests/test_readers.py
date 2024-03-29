"""Test reader classes"""

# Second-party imports
from . import secret_garden


def test_file_reader(final_data, data_dir, file_formats, excluded_vars):
    """Test the file reader"""
    for format_ in file_formats:
        vars_ = secret_garden.parsers.FileParser(
            data_dir / f"env.{format_}", format_
        ).vars
        assert vars_ == final_data

    for excluded_var in excluded_vars:
        assert excluded_var not in vars_


def test_environ_reader(final_data, included_vars, excluded_vars):
    """Test the environ reader"""

    vars_ = secret_garden.parsers.EnvironParser(included_vars).vars
    assert vars_ == final_data

    for excluded_var in excluded_vars:
        assert excluded_var not in vars_
