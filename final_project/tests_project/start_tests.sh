#!/bin/bash

chmod -x tests
cd tests

ls -a

pytest -s -l -v "${PATH_TESTS}" -n "${THREADS}" --alluredir /tmp/allure --selenoid --vnc