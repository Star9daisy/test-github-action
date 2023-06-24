import os


def test_root():
    print(os.environ["ROOTSYS"])
    import ROOT

    print(ROOT.__file__)
