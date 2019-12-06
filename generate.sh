true > tracking.log
python ./generate_log.py
now=$(date)
mv log "$now"
touch log
