select
    --p.name as "Product", 
  psubcat."name" as "Sub-category",
  pcat."name" as "Category",
  min(p.listprice) as "Lowest Price",
  max(p.listprice) as "Max Price",
  max(p.listprice) - min(p.listprice) as "Price Difference"
from
    production.productsubcategory as psubcat
join production.productcategory as pcat on
    pcat.productcategoryid = psubcat.productcategoryid
join production.product as p on
    psubcat.productsubcategoryid = p.productsubcategoryid
GROUP BY
    psubcat.name, pcat."name"--, p.name
ORDER BY
psubcat."name";