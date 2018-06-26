try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()

setup(name='algorithmic_toolbox',
      version='2018.06.25',
      description=("An Algorithmic Toolbox"),
      author="necromuralist",
      platforms=['linux'],
      url="https://necromuralist.github.io/algorithmic-toolbox/",
      author_email="necromuralist@protonmail.com",
      packages=find_packages(),
      )
