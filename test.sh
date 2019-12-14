#!/bin/bash

cd "$(dirname "$0")" || exit 1

(
    cd Kod || exit 1
    python -m unittest discover -s tests
)
