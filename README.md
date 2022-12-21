# Zapytanie wyciągające dane dla banana
```sql
SELECT ps_stock_available.* FROM ps_stock_available, ps_product
WHERE ps_stock_available.id_product =  ps_product.id_product
AND ps_product.reference = "food_2";
```
