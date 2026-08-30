# Phase 3 Resource Map

## Python standard library
https://docs.python.org/3/

Use current docs for `pathlib`, `json`, `csv`, `argparse`, `logging`, `os`/environment, exceptions, and testing tools chosen by the academy.

## Requests
https://requests.readthedocs.io/en/latest/user/quickstart/

Focus on methods, params/headers/json, status codes, `raise_for_status`, exceptions, and **timeouts**.

## FastAPI
https://fastapi.tiangolo.com/tutorial/

Focus on first steps, request bodies/validation, status/errors, bigger-app structure only as needed, background-task boundaries, and testing. Security sections are preview/reference; full security is later.

## Rule
Library syntax changes. Keep the architectural contract—timeouts, validation, explicit errors, tests—even if the chosen HTTP/service library changes later.
## Maintenance metadata
- Python standard-library docs — **REFERENCE / REVIEW YEARLY** for version-specific details; concepts are durable.
- Requests Quickstart — **PRIMARY PRACTICE / REVIEW YEARLY**. Focus on requests, responses, status, exceptions, timeouts; skip exotic features.
- FastAPI Tutorial — **PRIMARY PRACTICE / REVIEW YEARLY**. Focus on small services, validation, errors, tests; defer advanced security/deployment.
