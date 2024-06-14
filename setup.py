from setuptools import setup, find_packages

setup(
    name='siwp2005_varlent_sort',
    version='0.1.3',
    description='Package that includes multiple sorting method',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Varlent-2023/siwp2005-varlent-sort.git',
    author='Varlent AG',
    author_email='varlent.422023028@civitas.ukrida.ac.id',
    license='MIT',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    python_requires='>=3.8',
)