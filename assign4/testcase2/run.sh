cp murphy_strikes_check.py ../src/evaluate
pushd ..
paver run < testcase2/input.txt
/bin/rm -f src/evaluate/murphy_strikes_check.py
popd
