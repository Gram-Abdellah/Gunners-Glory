-- How many matches did Arsenal play at home versus away?
SELECT Count(*)  AS Matches
FROM epl_results_2022_23 where HomeTeam =='Arsenal'
group by HomeTeam;

SELECT Count(*)  AS Matches
FROM epl_results_2022_23 where AwayTeam =='Arsenal'
group by AwayTeam;

-- What is the total number of goals scored by Arsenal in home matches versus away matches?

SELECT Sum(FTHG)  AS Matches
FROM epl_results_2022_23 where HomeTeam =='Arsenal'
group by HomeTeam;

SELECT SUM(FTHG)  AS Matches
FROM epl_results_2022_23 where AwayTeam =='Arsenal'
group by AwayTeam;

-- What is the average number of goals scored by Arsenal in home matches versus away matches?
SELECT AVG(FTHG)  AS Matches
FROM epl_results_2022_23 where HomeTeam =='Arsenal'
group by HomeTeam;

SELECT AVG(FTAG)  AS Matches
FROM epl_results_2022_23 where AwayTeam =='Arsenal'
group by AwayTeam;

-- How many wins, losses, and draws did Arsenal have in home matches versus away matches?

SELECT count(*)  AS Matches
FROM epl_results_2022_23 where HomeTeam =='Arsenal' and FTR ='H'
group by HomeTeam;

SELECT count(*)  AS Matches
FROM epl_results_2022_23 where HomeTeam =='Arsenal' and FTR ='D'
group by HomeTeam;

SELECT count(*) AS Matches
FROM epl_results_2022_23 where AwayTeam =='Arsenal' and FTR ='A'
group by AwayTeam;

SELECT count(*) AS Matches
FROM epl_results_2022_23 where AwayTeam =='Arsenal' and FTR ='D'
group by AwayTeam;

-- What is the highest number of goals scored by Arsenal in a single home match versus away match?
SELECT MAX(FTHG) , AwayTeam  AS Matches
FROM epl_results_2022_23 where HomeTeam =='Arsenal'
group by HomeTeam;

SELECT MAX(FTAG) , HomeTeam AS Matches
FROM epl_results_2022_23 where AwayTeam =='Arsenal'
group by AwayTeam;

--What is the average number of goals conceded by Arsenal in home matches versus away matches?

SELECT AVG(FTAG)   AS Matches
FROM epl_results_2022_23 where HomeTeam =='Arsenal'
group by HomeTeam;

SELECT AVG(FTHG)  AS Matches
FROM epl_results_2022_23 where AwayTeam =='Arsenal'
group by AwayTeam;

-- How many clean sheets did Arsenal keep in home matches versus away matches?
SELECT Count(*)  as Home_clean_sheet
FROM epl_results_2022_23 where HomeTeam =='Arsenal' and FTAG==0
group by HomeTeam;

SELECT Count(*) as Away_clean_sheet
FROM epl_results_2022_23 where AwayTeam =='Arsenal' and FTHG==0
group by AwayTeam;

-- Which opponent did Arsenal score the most goals against in home matches versus away matches?
SELECT max(FTAG) , AwayTeam
FROM epl_results_2022_23 where HomeTeam =='Arsenal'
group by HomeTeam;

SELECT max(FTHG) , HomeTeam
FROM epl_results_2022_23 where AwayTeam =='Arsenal'
group by AwayTeam;

-- How many yellow cards and red cards did Arsenal receive in home matches versus away matches?
SELECT sum(HY) , sum(HR)
FROM epl_results_2022_23 where HomeTeam =='Arsenal'
group by HomeTeam;

SELECT SUM(AY) , sum(AR)
FROM epl_results_2022_23 where AwayTeam =='Arsenal'
group by AwayTeam;

-- How does Arsenal's goal difference compare in home matches versus away matches?

select HomeTeam ,sum(FTHG) as Sum_Goals_home
from epl_results_2022_23 where AwayTeam in ('Arsenal','Man City')
group by HomeTeam
order by Sum_Goals_home desc;

select AwayTeam ,sum(FTAG) as Sum_Goals_home
from epl_results_2022_23
group by HomeTeam
order by Sum_Goals_home desc;

--How many times did Arsenal come from behind to win in home matches versus away matches?
SELECT *
FROM epl_results_2022_23 where HomeTeam =='Arsenal' and HTAG > HTHG and FTHG > FTAG
group by HomeTeam;

SELECT *
FROM epl_results_2022_23 where AwayTeam =='Arsenal' and HTHG > HTAG and FTAG > FTHG
group by AwayTeam;


