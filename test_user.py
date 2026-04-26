# Needed to import from wksrc without installing it as a package
import sys
sys.path.append("wksrc")

from wksrc.user import hello

def test_main():
    assert hello() == "Hello, World!"


