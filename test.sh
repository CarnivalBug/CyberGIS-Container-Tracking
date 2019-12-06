#!/bin/bash
cat /home/flu8/track_log/curr.txt > /home/flu8/track_log/prev.txt
sudo docker node ps |tail -n +2 > /home/flu8/track_log/curr.txt
date >> /home/flu8/track_log/tracking.log
diff /home/flu8/track_log/prev.txt /home/flu8/track_log/curr.txt >> /home/flu8/track_log/tracking.log
echo "Finish One" >> /home/flu8/track_log/tracking.log
