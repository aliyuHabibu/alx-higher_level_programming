-- Script that groups base on number of appearance of score
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score;
