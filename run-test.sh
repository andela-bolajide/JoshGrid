#!/bin/bash

build_back_end() {
    python manage.py makemigrations
    python manage.py migrate
}

run_back_end_tests() {
  build_back_end
  python manage.py test
}

run_front_end_tests() {
  if ! [ -d "node_modules" ]; then
    # run npm install to install dependencies
    yarn install
  fi
  yarn test
}

if [[ $1 == "backend" ]]; then
    shift
    run_back_end_tests $@
elif [[ $1 == "frontend" ]]; then
    run_front_end_tests
else
    run_back_end_tests $@
    backend_rc=$?
    run_front_end_tests
    frontend_rc=$?
    echo

    if [[ $backend_rc == 0 && $frontend_rc == 0 ]]; then
        echo "All tests pass!!!"
        exit 0
    else
        echo "FAIL FAIL FAIL FAIL FAIL FAIL FAIL FAIL. Some tests failed, see above for details."
        exit 1
    fi
fi
