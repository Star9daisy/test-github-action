import os


def test_root():
    import ROOT

    print(ROOT.__file__)


if __name__ == "__main__":
    print(os.environ["PYTHONPATH"])
    print(os.environ["LD_LIBRARY_PATH"])
