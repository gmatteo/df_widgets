import io
from setuptools import setup, find_packages


# Get the long description from the relevant file
with io.open('README.md', encoding='utf-8') as f:
    long_description = f.read()


setup(name='df_widgets',
      version='0.0.1',
      description="Ipython widgets for Pandas Dataframes.",
      long_description=long_description,
      classifiers=[],
      keywords='',
      author="Matteo Giantomassi",
      author_email='gmatteo@gmail.com',
      url='https://github.com/gmatteo/df_widgets',
      license='GNU',
      packages=find_packages(exclude=['examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          "ipywidgets",
          "pandas",
          "seaborn",
          #"matplotlib",
      ],
      #extras_require={
      #    'test': ['pytest'],
      #},
      )
