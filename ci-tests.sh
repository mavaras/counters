function pytestf() {
    echo "\n\npytest ..."
    pytest
}
function mypyf() {
    echo "mypy ..."
    mypy counters/counters.py \
         counters/cvars.py \
         counters/utils.py
}

mypyf
pytestf
