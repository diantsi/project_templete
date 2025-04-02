import pandas as pd
import pytest

from app.io.input import input_from_file, input_from_file_by_pandas


@pytest.fixture
def setup_text_file(tmp_path):
    """Create content for txt file"""
    file_path = tmp_path / "test.txt"
    file_path.write_text("Bombordini crocodili")
    return file_path

@pytest.fixture
def setup_csv_file(tmp_path):
    """Create content for csv file"""
    file_path = tmp_path / "test.csv"
    df = pd.DataFrame({"1": [1, 2], "2": ["a", "b"]})
    df.to_csv(file_path, index=False)
    return file_path

def test_input_from_file_success(setup_text_file):
    """Test successful reading from text file"""
    content = input_from_file(setup_text_file)
    assert content == "Bombordini crocodili"

def test_input_from_file_not_found():
    """Test FileNotFoundError is raised when file doesn't exist"""
    with pytest.raises(FileNotFoundError):
        input_from_file("nonexistent_file.txt")



def test_input_from_file_by_pandas_success(setup_csv_file):
    """Test reading from csv file"""
    df = input_from_file_by_pandas(str(setup_csv_file))
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (2, 2)
    assert df["1"].tolist() == [1, 2]
    assert df["2"].tolist() == ["a", "b"]


def test_input_from_file_by_pandas_not_found():
    """Test FileNotFoundError is raised when file doesn't exist"""
    with pytest.raises(FileNotFoundError):
        input_from_file_by_pandas("nonexistent_file.csv")