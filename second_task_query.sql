SELECT 
    track, -- трекер заказа (это ведь имеется в виду или его id?)
    -- finished,
    -- cancelled,
    -- "inDelivery",
    CASE
        WHEN finished = true THEN 2
        WHEN cancelled = true THEN -1
        WHEN "inDelivery" = true THEN 1
        ELSE 0
    END AS "Order Status"
FROM "Orders";
