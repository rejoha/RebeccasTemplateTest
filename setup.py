from setuptools import find_packages, setup

setup(
    name="templatetest", # no hyphens!
    version="0.1.0",
    description="A Minimal Template Python Package",
    url="https://github.com/RealityBending/TemplatePythonPackage",
    author="Rebecca Johannessen",
    author_email="rjohannessen@live.no",
    license="MIT",
    install_requires=["numpy", "pandas", "scipy", "matplotlib"], # or a requirements.txt file
    packages=find_packages(),
    zip_safe=False,
)
