--Q1. How many total messages are being sent every day?
select DATE(created_at) AS "Date_Sent",
    COUNT(*) AS "Count_of_message"
from message
group by DATE(created_at);
--Q2. Are there any users that did not receive any message? --
select usr.id AS "user_not_receiving_any_message_today"
from public.user "usr"
where usr.id NOT IN (
        select CAST(msg.receiver_id as integer)
        from public.message "msg"
        where DATE(msg.created_at) = CURRENT_DATE
    );
-- Q3. How many active subscriptions do we have today?
select COUNT(*) AS "count_of_active_subscription"
from public.subscription scpn
where DATE(scpn.end_date) >= CURRENT_DATE
    and scpn.status = 'Active';
-- Q4. Are there users sending messages without an active subscription? 
select distinct(msg.sender_id) "users_sending_message_without_active_subscription"
from public.message msg
where CAST(sender_id as integer) not in (
        select user_id
        from public.subscription scpn
        where scpn.status = 'Active'
            and DATE(scpn.end_date) >= CURRENT_DATE
    );
-- Q5.How much is the average subscription amount (sum amount subscriptions / count subscriptions) breakdown by year/month (format YYYY-MM)?
select to_char(end_date, 'MM-YYYY') "month_year_end_date",
    SUM(amount) / COUNT(*) "monthly_aveage"
from subscription
group by to_char(end_date, 'MM-YYYY');