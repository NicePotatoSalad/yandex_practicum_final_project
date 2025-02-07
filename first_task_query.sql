SELECT 
    c.login, -- логин 
    -- c.id as "c. ID courier",
    -- o."courierId" as "o. ID courier",
    -- o."inDelivery",
    COUNT(o.id) AS "Orders In Delivery" -- кол-во заказов в статусе "в доставке"
FROM "Couriers" as c
JOIN "Orders" AS o ON c.id = o."courierId"
WHERE o."inDelivery" = true
GROUP BY c.login;
