CREATE TABLE IF NOT EXISTS players
(
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name  VARCHAR(255),
    sex   int DEFAULT 1,
    old   int,
    score int
);

-- ADDING DATA
INSERT OR IGNORE INTO players (user_id, name, sex, old, score)
VALUES (121, 'Арсений', 1, 20, 70),
       (122, 'Максим', 1, 21, 65),
       (123, 'Даша', 2, 26, 70),
       (124, 'Настя', 2, 24, 60),
       (125, 'Андрей', 1, 22, 75),
       (126, 'Антон', 1, 23, 80),
       (127, 'Анна', 2, 25, 85),
       (128, 'Алексей', 1, 27, 50),
       (129, 'Александр', 1, 28, 95),
       (130, 'Александра', 2, 29, 100);

SELECT name FROM players;
SELECT name, score FROM players WHERE score > 65;
-- when there are several conditions, they are performs by ()
SELECT name FROM players WHERE old > 20 AND (score > 65 OR sex = 2);
-- SORTED BY SCORE (HIGH TO LOW)
SELECT name, score FROM players ORDER BY score DESC;
-- SORTED BY SCORE (LOW TO HIGH)
SELECT name, score FROM players ORDER BY score ASC;
--LIMIT 2
SELECT name, score FROM players ORDER BY score DESC LIMIT 2;
--OFFSET 2 (SKIP 2)
SELECT name, score FROM players ORDER BY score DESC LIMIT 2 OFFSET 2;
--UPDATE
UPDATE players SET score = 100 WHERE user_id = 121; -- SETTING SCORE 100 TO USER WITH ID 121 (Если убрать where, то все записи будут изменены)
UPDATE players SET score = score + 10 WHERE sex = 2 AND score <= 90; -- INCREASE SCORE BY 10 FOR ALL FEMALES
UPDATE players SET score = 10 WHERE name= 'Арсений'; -- SETTING SCORE 10 TO USER WITH NAME Арсений
UPDATE players SET score = 20 WHERE name= 'А%'; -- setting score 20 to all users with name starting with А
UPDATE players SET score = 50 WHERE name= 'А_е%'; -- setting score 50 to all users with name starting with А and 3rd letter is е
--DELETE
DELETE FROM players WHERE user_id = 121; -- DELETING USER WITH ID 121

SELECT COUNT(user_id) as count FROM players; -- COUNTING USERS
SELECT COUNT(user_id) as count FROM players WHERE score > 65; -- COUNTING USERS WITH SCORE > 65
SELECT min(score) as min, max(score) as max, avg(score) as avg FROM players; -- MIN, MAX, AVG

SELECT SUM(score) as sum FROM players; -- SUM OF ALL SCORES
-- GROUP BY sex scores
SELECT sex, sum(score) AS SUM FROM players GROUP BY sex;

INSERT OR IGNORE INTO players (user_id, name, sex, old, score) VALUES (121, 'Арсений', 1, 20, 50); -- добавляем вторую сдачу данного человека

CREATE TABLE IF NOT EXISTS results
(
    user_id   INTEGER PRIMARY KEY AUTOINCREMENT,
    date     DATE,
    time      INT
);
INSERT OR IGNORE INTO results (user_id, date, time) VALUES (121, '2020-01-01', 10); -- добавляем вторую сдачу данного человека
INSERT OR IGNORE INTO results (user_id, date, time) VALUES (121, '2020-01-02', 20); -- добавляем 3 сдачу данного человека
INSERT OR IGNORE INTO results (user_id, date, time) VALUES (122, '2020-01-01', 30); -- добавляем вторую сдачу данного человека
INSERT OR IGNORE INTO results (user_id, date, time) VALUES (125, '2020-01-03', 40); -- добавляем 3 сдачу данного человека


--JOIN
SELECT name, score, time, date FROM players JOIN results ON players.user_id = results.user_id;
--JOIN with WHERE
SELECT name, score, time, date FROM players JOIN results ON players.user_id = results.user_id WHERE score >= 65;
SELECT name, score,results.date FROM players, results; -- CROSS JOIN

--LEFT JOIN
SELECT name, score, time, date FROM players LEFT OUTER JOIN results ON players.user_id = results.user_id;

--UNION
SELECT name FROM players UNION SELECT user_id FROM results;

--NESTED QUERIES

-- SELECT score FROM players WHERE user_id = 121 AND sex = 1;
-- SELECT name, score FROM players
-- JOIN results ON results.user_id = players.user_id
-- WHERE score > 60;
SELECT score FROM players WHERE user_id = 121 AND sex = 1;
SELECT name, score FROM players
JOIN results ON results.user_id = players.user_id
WHERE score > (SELECT score FROM players WHERE user_id = 121 AND sex = 1);

--nested queries in UPDATE (МЕНЯЕМ ВСЕ ЗНАЧЕНИЯ ГДЕ ОЧКИ МЕНЬШЕ ИЛИ = 70)
UPDATE players SET score = 50 WHERE score < (SELECT score FROM players WHERE score <= 70);

-- УДАЛИТЬ СТУДЕНТОВ, ВОЗРАСТ КОТОРЫХ МЕНЬШЕ ЧЕМ У аАНТОНА(126)
DELETE FROM players WHERE old < (SELECT old FROM players WHERE user_id = 126);


SELECT * FROM players;
SELECT * FROM results;