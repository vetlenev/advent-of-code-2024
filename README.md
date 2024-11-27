<h1 align="center">Python Project Template</h1>
<h3><p align="center">A template for new python projects.</p></h3>

<p align="center">
<a href="https://akerbp.sharepoint.com/sites/BU-OPS-FUTURE-OPERATIONS/SitePages/Defect.aspx?xsdata=MDV8MDF8fDBmOTgwMzVjZTRmODQ4ODdkYWU5MDhkYjYyYjc4NjI2fDNiN2U0MTcwODM0ODRhYTRiZmFlMDZhM2UxODY3NDY5fDB8MHw2MzgyMTIzMTI1NzIyODc3MjF8VW5rbm93bnxWR1ZoYlhOVFpXTjFjbWwwZVZObGNuWnBZMlY4ZXlKV0lqb2lNQzR3TGpBd01EQWlMQ0pRSWpvaVYybHVNeklpTENKQlRpSTZJazkwYUdWeUlpd2lWMVFpT2pFeGZRPT18MXxMMk5vWVhSekx6RTVPak5tTkRFeE5qUmxMVEZtTWprdE5ESTROeTA1T0Roa0xXVTJZVGt5WmpWaVpUZG1NMTlrTkRjM01HRTRPUzAxTmpnMUxUUmhZVEV0T0dZMU15MDVaVGRqTTJSa1lUUm1ZalJBZFc1eExtZGliQzV6Y0dGalpYTXZiV1Z6YzJGblpYTXZNVFk0TlRZek5EUTFOalk1TXc9PXxkOTIyN2E1OWQwNzY0YWFmZGFlOTA4ZGI2MmI3ODYyNnxhYjFlNDM4ZjAyNjE0Mzg0YTVlNWIyNTNlNDA0ODI2ZA%3D%3D&sdata=UEhKUUdvME82dUZJa0lyUlMyYWFnMGJocFdFK1ZLSDVxNXR5TUVhUFZwbz0%3D&ovuser=3b7e4170-8348-4aa4-bfae-06a3e1867469%2canett.stousland%40akerbp.com&OR=Teams-HL&CT=1685642608939&clickparams=eyJBcHBOYW1lIjoiVGVhbXMtRGVza3RvcCIsIkFwcFZlcnNpb24iOiIyNy8yMzA1MDEwMDQyMiIsIkhhc0ZlZGVyYXRlZFVzZXIiOmZhbHNlfQ%3D%3D"><img src="https://img.shields.io/badge/Developed_In-Center_of_Excellence_--_IOC-purple?style=for-the-badge"></a>
<br>
<a href="https://github.com/AkerBP/coe-ioc-template-python-project/actions/workflows/build_docs.yaml"><img src="https://github.com/AkerBP/coe-ioc-template-python-project/actions/workflows/build_docs.yaml/badge.svg"></a>
<a href="https://github.com/AkerBP/coe-ioc-template-python-project/actions/workflows/tests.yaml"><img src="https://github.com/AkerBP/coe-ioc-template-python-project/actions/workflows/tests.yaml/badge.svg"></a>
<a href="https://github.com/AkerBP/coe-ioc-template-python-project/actions/workflows/code_quality.yaml"><img src="https://github.com/AkerBP/coe-ioc-template-python-project/actions/workflows/code_quality.yaml/badge.svg"></a>

<br>

## Features
Github actions for
- Automatically build user guide and API reference with `sphinx`
- Automatically test code with `pytest`
- Automatically perform code quality checks with `ruff`


## How to use
The template has used genereic names for several variables that you need to
update:

1. Start a new project based on this template
2. Update the following files with correct information:
    - `pyproject.toml`
        - authors
        - project name
        - project description
        - dependencies
        - anything else you need

    - `docs/conf.py`
        - project name
        - copyright
        - author

    - `docs/source/api_main`
        - add `toctree` directive to your code

    - `docs/source/api_test`
        - add `toctree` directive to your test code

    - `.github/workflows/build_docs`
        - correct project name throughout
