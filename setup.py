#!/usr/bin/env python3
"""
Setup script for Crypto Yield Optimizer
"""

from setuptools import setup, find_packages
import os

# Read the README file for long description
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Read requirements from requirements.txt
def read_requirements():
    requirements = []
    if os.path.exists("requirements.txt"):
        with open("requirements.txt", "r", encoding="utf-8") as fh:
            requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]
    return requirements

setup(
    name="crypto-yield-optimizer",
    version="1.0.0",
    author="DeFi Analytics Team",
    author_email="dev@crypto-yield-optimizer.com",
    description="A comprehensive DeFi analytics and yield optimization platform",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/wearedood/crypto-yield-optimizer",
    project_urls={
        "Bug Tracker": "https://github.com/wearedood/crypto-yield-optimizer/issues",
        "Documentation": "https://docs.crypto-yield-optimizer.com",
        "Source Code": "https://github.com/wearedood/crypto-yield-optimizer",
        "Discord": "https://discord.gg/crypto-yield-optimizer",
    },
    packages=find_packages(exclude=["tests*", "docs*"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Financial and Insurance Industry",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Office/Business :: Financial",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    python_requires=">=3.9",
    install_requires=[
        "web3>=6.0.0",
        "requests>=2.28.0",
        "pandas>=1.5.0",
        "numpy>=1.24.0",
        "aiohttp>=3.8.0",
        "asyncio-throttle>=1.0.0",
        "python-dotenv>=0.19.0",
        "pydantic>=1.10.0",
        "fastapi>=0.95.0",
        "uvicorn>=0.20.0",
        "sqlalchemy>=1.4.0",
        "alembic>=1.9.0",
        "redis>=4.5.0",
        "celery>=5.2.0",
        "psycopg2-binary>=2.9.0",
        "scikit-learn>=1.2.0",
        "tensorflow>=2.12.0",
        "plotly>=5.13.0",
        "dash>=2.8.0",
        "pytest>=7.2.0",
        "pytest-asyncio>=0.20.0",
        "black>=23.0.0",
        "flake8>=6.0.0",
        "mypy>=1.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.2.0",
            "pytest-cov>=4.0.0",
            "pytest-asyncio>=0.20.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "mypy>=1.0.0",
            "pre-commit>=3.0.0",
            "sphinx>=6.0.0",
            "sphinx-rtd-theme>=1.2.0",
        ],
        "ml": [
            "tensorflow>=2.12.0",
            "torch>=2.0.0",
            "transformers>=4.26.0",
            "scikit-learn>=1.2.0",
            "xgboost>=1.7.0",
            "lightgbm>=3.3.0",
        ],
        "monitoring": [
            "prometheus-client>=0.16.0",
            "grafana-api>=1.0.3",
            "sentry-sdk>=1.15.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "crypto-yield-optimizer=crypto_yield_optimizer.cli:main",
            "cyo=crypto_yield_optimizer.cli:main",
            "yield-optimizer=crypto_yield_optimizer.cli:main",
        ],
    },
    include_package_data=True,
    package_data={
        "crypto_yield_optimizer": [
            "data/*.json",
            "data/*.csv",
            "templates/*.html",
            "static/css/*.css",
            "static/js/*.js",
        ],
    },
    zip_safe=False,
    keywords=[
        "defi",
        "yield-farming",
        "cryptocurrency",
        "blockchain",
        "ethereum",
        "polygon",
        "bsc",
        "avalanche",
        "analytics",
        "optimization",
        "portfolio",
        "liquidity",
        "apy",
        "apr",
        "smart-contracts",
        "web3",
        "dex",
        "uniswap",
        "sushiswap",
        "curve",
        "balancer",
        "aave",
        "compound",
    ],
    license="MIT",
    platforms=["any"],
)
