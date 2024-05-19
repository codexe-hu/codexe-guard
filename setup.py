from setuptools import setup, find_packages

setup(
    name='codexe-guard',
    version='0.1.0',
    namespace_packages=['codexe.guard'],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='',
    license='APACHE LICENSE, VERSION 2.0',
    author='Róbert Tóth',
    author_email='toth.robert@inf.unideb.hu',
    description='',
    python_requires='>=3.10.0',
    install_requires=[
    ],
    entry_points={
        'console_scripts': [
            'codexe-hlpl1 = codexe.guard.hlpl1:start_exam',
        ]
    }
)

