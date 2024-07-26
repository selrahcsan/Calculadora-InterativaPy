from setuptools import setup, find_packages

setup(
    name="calculadora_interativa_py",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "colorama>=0.4.6"
    ],
    entry_points={
        "console_scripts": [
            "meu_projeto=meu_projeto.main:main",
        ],
    },
    author="Charles Santana",
    author_email="charlesstna@proton.me",
    description="projeto de uma calculadora interativa em python para aprendizado",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/seu_usuario/meu_projeto",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)