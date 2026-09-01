-- Задание 1
-- Логины курьеров и количество заказов в статусе «В доставке»

SELECT
    c."login",
    COUNT(o."id") AS orders_count
FROM "Couriers" AS c
LEFT JOIN "Orders" AS o
    ON c."id" = o."courierId"
    AND o."inDelivery" = true
GROUP BY c."id", c."login"
ORDER BY c."login";


-- Задание 2
-- Трекеры заказов и их статусы

SELECT
    "track",
    CASE
        WHEN "finished" = true THEN 2
        WHEN "cancelled" = true THEN -1
        WHEN "inDelivery" = true THEN 1
        ELSE 0
    END AS status
FROM "Orders";