from setuptools import setup, find_packages

setup(
    name='PyomoSolvers',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
    ],
    package_data={'': ['solvers_lin64/Invitation_FR.pdf']},
    zip_safe=False,
)

