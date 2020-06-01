cp community_service_check.py ../src/evaluate
pushd ..
paver run < testcase1/input.txt
/bin/rm -f src/evaluate/community_service_check.py
popd