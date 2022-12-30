from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in ec_portal/__init__.py
from ec_portal import __version__ as version

setup(
	name="ec_portal",
	version=version,
	description="Esycommerce Portal",
	author="Shashank Shirke",
	author_email="shashank@esycommerce.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
