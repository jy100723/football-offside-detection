from setuptools import setup, find_packages

setup(
    name='football-offside-detection',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # Add your project dependencies here
    ],
    entry_points={
        'console_scripts': [
            # Define entry points for command line tools here
        ],
    },
    author='Your Name',
    author_email='your_email@example.com',
    description='A project for detecting offside in football matches',
    license='MIT',
    url='https://github.com/jy100723/football-offside-detection',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)