from setuptools import setup, find_packages

setup(
    name='economic_agents',
    version='0.1',
    description='A Python package for the paper "Large Language Models as Simulated Economic Agents: What Can We Learn from Homo Silicus?"',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Max Hager',
    author_email='maxhager28@gmail.com',
    packages=find_packages(),
    install_requires=[
        'openai',
        'matplotlib',
        'numpy',
        'pandas'
    ],
)