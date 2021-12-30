-- 	How many total messages are being sent every day?
SELECT date(createdat), count(createdat) as total_count 
FROM messages 
GROUP BY date(createdat)
ORDER BY count(createdat) DESC


--	Are there any users that did not receive any message?
select u.id from users u
left join messages m on u.id = m.receiverid 
where m.receiverid is null


-- How many active subscriptions do we have today?
select * from subscriptions s where s.status  = 'Active' and s.startdate <= CURRENT_DATE and s.enddate >= CURRENT_DATE


-- Are there users sending messages without an active subscription? 



-- Did you identified any inaccurate/noisy record that somehow could prejudice the data analyses? 
-- How to monitor it (SQL query)? Please explain how do you suggest to handle with this noisy data?

