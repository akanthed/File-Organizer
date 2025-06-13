from setuptools import setup, find_packages

setup(
    name='File-Organizer',
    version='0.1.0',
    packages=find_packages(),
    description='Automatically organizes your files into folders based on file type.',
    author='Akshay Kanthed',
    author_email='your-email@example.com',
    entry_points={
        'console_scripts': [
            'organize-files=fileorganizer_ai.cli:main'
        ],
    },
    install_requires=[],
    python_requires='>=3.6',
)