from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in student/__init__.py
from student import __version__ as version

setup(
	name="student",
	version=version,
	description="Register Student And Convert Into User",
	author="Mohammed Nasser",
	author_email="nasser@nasserx.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
