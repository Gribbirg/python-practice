from setuptools import setup

setup(
    name='my_package',
    version='0.0.1',
    description='my_package',
    package_data={'my_package': ['./my_package/data.json']},
    include_package_data=True,
    packages=['my_package']
)
