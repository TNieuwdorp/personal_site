---
date: '2024-12-18T12:14:29+01:00'
draft: true
title: 'Moving to uv'
description: "A blog post detailing the features of uv, an extremely fast Python package installer and resolver, an explanation and examples of it's functionality, and a migration guide for switching to it."
keywords: ["Python", "software engineering", "development", "uv", "Rust"]
categories: [tool]
---
# Python Tools: `uv`

## I. Introduction: Meet `uv`, the Future of Python Tooling

In case you hadn't heard, `uv` is the new kid on the block.
It's a Python package installer and resolver written in Rust, developed by the team at Astral (who also made Ruff, a fast Python formatter written in Rust). 
It serves as a drop-in replacement for pip, venv, and pip-tools while offering dramatic performance improvements.

With installation speeds up to 10-100x faster than pip, `uv` represents a significant leap forward in Python tooling. 
This speed boost comes from its Rust implementation, parallel downloads, and efficient caching system. 
As example on the website, Astral shows installing Django and its dependencies takes just 1.2 seconds with `uv` compared to 12+ seconds with pip.

On top of that, `uv` recently incorporated managing venvs, including their python version.
This replaces both `virtualenv` and `pyenv`, that were the usual suspects for managing python version on a system.

This makes `uv` a tool that Python developers must have in their toolbox.

## II. Understanding the `uv` Ecosystem

Use Cases
Astral uv caters to a wide range of Python development scenarios:
Managing Packages: Efficiently install, update, and manage Python packages with significant speed improvements over traditional methods1.
Handling Projects: Streamline project setup, dependency management, and virtual environment creation for diverse project types1.
Working with Scripts: Simplify dependency management for individual scripts, ensuring consistent and isolated execution environments1.
Installing Tools: Install and manage command-line tools provided by Python packages, similar to pipx3.
Building and Publishing Projects: Facilitates building and publishing Python projects, even those not managed with uv3. For example, you can use uv to build and publish a project that uses a setup.py file.
Astral uv is licensed under either the Apache License, Version 2.0, or the MIT license, allowing for both commercial and open-source use.

## III. Step-by-Step Migration Guide

### A. Installation

The best way to install uv is by using it's standalone installer:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Alternative ways for installing for Windows, using pip(x), Cargo, Homebrew, WinGet, Scoop, Docker, or straight from Github are described in [the installation instructions.](https://docs.astral.sh/uv/getting-started/installation)

### B. Creating Virtual Environments

Create and activate a virtual environment:

```bash
uv venv
source .venv/bin/activate  # Unix
.venv\Scripts\activate     # Windows
```

Key virtual environment options:
- `--python` or `-p` : Specify Python version
- `--prompt`: Custom virtual environment prompt
- `--name`: Custom environment directory name
- `--seed`: Install core packages into the venv, like TODO

### C. Migrating requirements.txt

To install from existing requirements:
```bash
uv pip install -r requirements.txt
```

Consider migrating to `pyproject.toml` for modern dependency management, though `uv` works well with either approach.

### D. Migrating from pyproject.toml

Install project dependencies:
```bash
uv pip install .
# With extras:
uv pip install .[dev,test]
```

### E. Migrating from pip-tools

Generate requirements files:
```bash
uv pip compile pyproject.toml -o requirements.txt
# Install compiled dependencies:
uv pip sync requirements.txt
```

### F. Workflow Adaptations

Common workflow commands:
```bash
# Add new dependencies
uv pip install package_name

# Update dependencies
uv pip compile --upgrade

# Install in editable mode
uv pip install -e .
```

### G. CI/CD Integration

Example GitHub Actions configuration:
```yaml
steps:
  - uses: actions/checkout@v3
  - name: Install uv
    run: curl -LsSf https://astral.sh/uv/install.sh | sh
  - name: Set up Python
    uses: actions/setup-python@v4
    with:
      python-version: '3.10'
  - name: Install dependencies
    run: |
      uv venv
      source .venv/bin/activate
      uv pip sync requirements.txt
```

## IV. Advanced `uv` Usage and Considerations

`uv` implements an intelligent caching system that stores downloaded packages and wheel builds. Manage the cache using:
```bash
uv cache dir    # Show cache location
uv cache clear  # Clear cache
```

Current limitations:
- Some pip features still in development
- Limited platform support compared to pip
- Early-stage tool, expect ongoing changes

The roadmap includes expanded platform support, additional pip feature parity, and performance optimizations.

## V. Conclusion

`uv` represents a significant advancement in Python package management, offering:
- Dramatically improved installation speeds
- Drop-in compatibility with existing tools
- Reliable dependency resolution
- Modern architecture and active development

For more information:
- GitHub Repository: https://github.com/astral-sh/uv
- Documentation: https://github.com/astral-sh/uv/blob/main/README.md
- Community Discussions: https://github.com/astral-sh/uv/discussions

Consider trying `uv` in your next Python project to experience these benefits firsthand.