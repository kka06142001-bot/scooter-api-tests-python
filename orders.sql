SELECT
    c."login",
    COUNT(o."id") AS orders_count
FROM "Couriers" AS c
LEFT JOIN "Orders" AS o
    ON c."id" = o."courierId"
    AND o."inDelivery" = true
GROUP BY c."id", c."login"
ORDER BY c."login";