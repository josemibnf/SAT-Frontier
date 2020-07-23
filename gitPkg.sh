rm -rf Solvers && rm -rf for_build && rm -rf .git
for i in $(ls -C1)
do
touch -a --date="1988-02-15 01:00:17.547775198 +0300" $i
touch -m --date="2020-01-20 23:05:43.443117094 +0400" $i
done
