- How many unique stations are there in the data set?
- How many unique artists are there in the data set? 
- How many unique tracks are there in the data set? 
- Who are the top 3 artists based number of consumption events per artist? 
- Which are the top 3 tracks?



select count(distinct f.station_id)
from consumptions c
left join feed_station_mapping f on f.feed_id = c.feed_id
>> 1122

select count(distinct c.artist)
from consumptions c
>>> 8

select artist, count(stamp)
from consumptions
group by artist
order by count(stamp) desc
limit 3
>>> artist_03,180794
artist_07,172805
artist_02,44145

select track, count(stamp)
from consumptions
group by track
order by count(stamp) desc
limit 3
>>> Song_05,180794
Song_04,172805
Song_01,44145

>>> top 2 track per feed

select feed_id,
       track,
       listens,
       rank_id
from (select distinct feed_id,
       track,
       listens,
       rank() OVER (PARTITION BY feed_id ORDER BY listens DESC) as rank_id
from (select distinct a.feed_id,
       a.track,
       count(stamp) OVER (PARTITION BY feed_id, track) as listens
        from (select c.*, fsm.station_id
                from consumptions c
                left join feed_station_mapping fsm on c.feed_id = fsm.feed_id) as a
) as b
group by feed_id, track
order by feed_id) c
where rank_id <3

>>>top 2 track per station id

select station_id,
       artist,
       track,
       listens,
       rank_id
from (select distinct station_id,
                      artist,
       track,
       listens,
       rank() OVER (PARTITION BY station_id ORDER BY listens DESC) as rank_id
from (select distinct a.station_id,
                      a.artist,
       a.track,
       count(stamp) OVER (PARTITION BY station_id, artist, track) as listens
        from (select c.*, fsm.station_id
                from consumptions c
                left join feed_station_mapping fsm on c.feed_id = fsm.feed_id) as a
        where station_id is not null
) as b
group by station_id, artist, track
order by station_id) c
where rank_id <3

>>> how much track is played per station

select distinct a.station_id,
                      a.artist,
       a.track,
       count(stamp) OVER (PARTITION BY station_id, artist, track) as listens
        from (select c.*, fsm.station_id
                from consumptions c
                left join feed_station_mapping fsm on c.feed_id = fsm.feed_id) as a
        where station_id is not null

order by station_id asc, listens desc