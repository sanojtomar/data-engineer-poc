-- 	How many total messages are being sent every day?
SELECT date(createdat), count(createdat) as total_count 
FROM messages 
GROUP BY date(createdat)
ORDER BY date(createdat) DESC


--	Are there any users that did not receive any message?
select u.id from users u
left join messages m on u.id = m.receiverid 
where m.receiverid is null


-- How many active subscriptions do we have today?
select count(id) from subscriptions s where s.status  = 'Active' and CURRENT_DATE between s.startdate and s.enddate


-- Are there users sending messages without an active subscription?
select distinct m.senderid from messages m left join subscriptions s  on m.senderid = s.userid
where  s.userid is NULL

-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~--
-- Did you identified any inaccurate/noisy record that somehow could prejudice the data analyses? 
-- How to monitor it (SQL query)? Please explain how do you suggest to handle with this noisy data?

-- *** birthdate is recent dates, these are invalid dates ***
-- *** how a new born can come to app and sent the messages? ***
select birthdate from users u ;

-- *** there are few records where subscription  createddt are after startdate
select * from subscriptions s where s.createdat > s.startdate ;

-- *** there is user who has sent messages without subscription
select distinct m.senderid from messages m left join subscriptions s  on m.senderid = s.userid
where  s.userid is NULL

-- Solution for inaccurate/noisy data:
   -- It varies case to case
   -- We are seeing recent dates for birthdate, that is for all users so we should notify this to data provider
   -- For subscription date issue, current data is very less; we can collect more data and then think the solution
            -- It is sure that in ideal case, createdt should be eariler or equal to startdate so we can update createdt same as startdate
            -- If lots of data is coming with same kind of inaccuracy then it can be escalated to the data provider
    -- Issue related to sending message without the subscription, it can be a business use case
        -- or the data itself can be inaccurate.. if data is too less it can be ignored/deleted





