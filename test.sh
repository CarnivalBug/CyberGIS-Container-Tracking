#!/bin/bash

for i in {1..10};
do
	cat curr.txt > prev.txt
	sudo docker ps |tail -n +2 > curr.txt;
	date >> tracking.log;
	diff prev.txt curr.txt >> tracking.log;
	echo "Finish One" >> tracking.log;
	sleep 10;
done
	
echo "Done" >> tracking.log
