from setuptools import setup, find_packages



setup(name='Veggies',
      version='0.0.1',
      description='A veggies api.',
      author='Mark',
      packages=find_packages(include=['python', 'python.*']),
      python_requires='>=3.6, <4',
      install_requires=['flask', 'pandas', 'flask_restful', 'flask_cors', 'bs4', 'pathlib', 'requests', 'xlrd', 'openpyxl'])