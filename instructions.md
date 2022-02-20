##### To complete this hands-on part of the interview please submit the end result (reports), code/SQL and a short description how you solved the problem.

● Download the linked data files, which contain anonymized music consumption data.

● Load the data into your favorite database, for example Postrges running on Docker

● Validate that you have 521974 records in the consumptions dataset, and 1125 records
in the feed_station_mapping dataset.

● Warm up:answer the following questions about the data:

- How many unique stations are there in the data set?
- How many unique artists are there in the data set? 
- How many unique tracks are there in the data set? 
- Who are the top 3 artists based number of consumption events per artist? 
- Which are the top 3 tracks?

● Report:

Create a de-normalized consumption table with timestamp (not text), track, artist,
c.feed_id, feed_name, station_id and insert the data into that table by joining it
from the two tables
- Create a report with the top 2 tracks per feed id
- List the tracks in order of how much they have played by on each station. Which
are the top 2 tracks on smp_station_name_01?
- Which were the top 2 tracks on 2019-01-16 and how many times were they
played? Would this change if we would look at CET instead of UTC time?
- (bonus) Create a report with the top 2 tracks per station id