-- Script to insert new attribute and return/display the table
INSERT INTO second_table (score, name) VALUES (18, "Aria"), (12, "Aria");
SELECT score, name FROM second_table  WHERE score >= 10 ORDER BY score DESC;
