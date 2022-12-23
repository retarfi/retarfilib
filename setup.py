from distutils.core import setup

import retarfilib

module_name: str = "retarfilib"
setup(
    name=module_name,
    version=retarfilib.__version__,
    description="",
    author="Masahiro Suzuki",
    packages=[module_name],
    install_requires=open("requirements.txt").read().splitlines(),
)
