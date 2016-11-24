from setuptools import setup, find_packages

setup(name='minecraft-py',
      version='0.0.2',
      description='Python3 bindings for Malmo',
      url='https://github.com/tambetm/minecraft-py34-ubuntu1404',
      author='Tambet Matiisen',
      author_email='tambet.matiisen@gmail.com',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False
)
