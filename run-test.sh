build_front_end() {
    cd /joshgrid/mail_app/static
    yarn install
}

run_back_end_tests() {
  python manage.py test
}

run_front_end_tests() {
  build_front_end
  cd /joshgrid/mail_app/static
  yarn test
}

if [[ $1 == "backend" ]]; then
    shift
    run_back_end_tests $@
    rc=$?
elif [[ $1 == "frontend" ]]; then
    run_front_end_tests
    rc=$?
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
