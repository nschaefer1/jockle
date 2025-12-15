
with agg_table as (
	select
		inv_ck,
		sum(val) as item_count
	from ft_inventory 
	where char_ck = ?
	group by 1
)

select 
	a.inv_ck,
	a.inv_name,
	a.inv_desc,
	a.icon_path,
	coalesce(b.item_count, 0) as item_count
from dim_inventory as a
left join agg_table as b
	on a.inv_ck = b.inv_ck
order by 2;


