# Cognitive-TextAnalytics-Python
Python SDK for the Microsoft Text Analytics API, part of Congitive Services

## Installation

```bash
pip install cognitive_textanalytics
```

## Development

### Dev Setup

NOTE: Assumes you've already run `virtualenv venv`.

```bash
# Initial setup
. ./venv/bin/activate

# Install requirements
make init

# Validate
make test
```

## Installation from Source Code

```bash
make install
```

## Foundation
This uses Swagger-CodeGen for interfacing to the Cognitive Services API.

https://github.com/swagger-api/swagger-codegen

Developer Note:  I am usually opposed to auto-generated code; however, it allows us to better remediate errors as API changes have the potential to break and we want to reduce the amount of time spent fixing.