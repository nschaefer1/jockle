
select 
	a.inv_ck,
	b.inv_name,
	b.inv_desc,
	b.icon_path,
	sum(a.val) as item_count
from ft_inventory as a
right join dim_inventory as b
	on a.inv_ck = b.inv_ck
where a.char_ck = ?
group by 1,2,3,4
order by 2;
