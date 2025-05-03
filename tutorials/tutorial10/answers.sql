-- Exercise 1 (done for you): Selecting all columns
SELECT * FROM users;



-- Exercise 2 (done for you): Selecting some columns
SELECT id, first_name, last_name 
FROM users;



-- Exercise 3: Sorting
SELECT last_name, first_name FROM users ORDER BY last_name;



-- Exercise 4: Filtering
SELECT ID user_id, image_url 
FROM posts 
JOIN users ON user_id = id
WHERE first_name = 'Nicholas';



-- Exercise 5: Filtering with logical operators
SELECT ID user_id, image_url 
FROM posts 
JOIN users ON user_id = id
WHERE user_id = 26 or  user_id = 12;


-- Exercise 6: Using functions in a select statement

SELECT count(*) 
FROM posts
;


-- Exercise 7: Aggregating data
SELECT user_id, count(*) 
FROM comments
GROUP BY user_id
ORDER BY count(*) desc
;



-- Exercise 8: Joining: two tables
SELECT posts.id, posts.user_id, posts.image_url
FROM posts
JOIN users on posts.user_id = users.id
WHERE users.first_name = 'Nicholas' or users.first_name = 'Rebecca';



-- Exercise 9: More joining practice: two tables
SELECT posts.id, posts.pub_date, following.following_id
FROM posts
JOIN following on posts.user_id = following.following_id
WHERE following.user_id = 26 ; 



-- Exercise 10: More joining practice: three tables (Optional)
SELECT posts.id, posts.pub_date, following.following_id
FROM posts
JOIN following on posts.user_id = following.following_id
WHERE following.user_id = 26 ; 



-- Exercise 11: Inserting records
SELECT
FROM bookmarks
WHERE ;




-- Exercise 12: Deleting records




-- Exercise 13: Updating records




-- Exercise 14: More Querying Practice (Optional)
