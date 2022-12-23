import os.path
from distutils.core import setup

base_dir: str = os.path.dirname(os.path.abspath(__file__))
module_name: str = "retarfilib"
version: dict[str, str] = {}
with open(os.path.join(base_dir, module_name, "version.py")) as fp:
    exec(fp.read(), version)
# later on we use: version['__version__']
setup(
    name=module_name,
    version=version['__version__'],
    description="Frequently used functions",
    author="Masahiro Suzuki <msuzuki9609@gmail.com>",
    packages=[module_name],
    install_requires=open("requirements.txt").read().splitlines(),
)
