from __REPO_NAME__.__REPO_NAME__ import SampleClass
from __REPO_NAME__.__REPO_NAME__ import sample_func_subtract


def test_sample_method_add():
    sc = SampleClass()
    assert sc.sample_method_add(2, 4) == 6  # nosec


def test_sample_func_subtract():
    assert sample_func_subtract(4, 3) == 1  # nosec

