from setuptools import setup


setup(name='timeseriesdiff',
      version='0.1',
      description='Meaningful comparison of discrete two-dimensional curves.',
      author='Philipp S. Lang',
      author_email='philipp.s.lang@gmail.com',
      download_url='https://github.com/plang85/timeseriesdiff.git',
      install_requires=['numpy>=1.9',
                        'scipy>=0.14'],
      extras_require={
          'test': ['pytest',
                   'pytest-pep8',
                   'pytest-xdist',
                   'pytest-cov'],
      },
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'Intended Audience :: Developers',
          'Intended Audience :: Engineers',
          'Programming Language :: Python :: 3.6',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules'
      ],
      packages=['timeseriesdiff'])
