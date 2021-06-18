#!/bin/sh -l

export SWIFTLINT_RESULT_PATH=${1}
export XCODE_TESTS_RESULT_PATH=${2}
export AUTHOR=${3}

python3 /main.py "${SWIFTLINT_RESULT_PATH}" "${XCODE_TESTS_RESULT_PATH}" "${AUTHOR}"
