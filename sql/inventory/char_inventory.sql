

select
    a.inv_ck,

    b.inv_name,
    b.inv_desc,

    c.icon_path,

    sum(val) as item_count

from ft_inventory as a
left join dim_inventory as b
    on a.inv_ck = b.inv_ck
left join dim_icon as c
    on b.icon_ck = c.icon_ck
where a.char_ck = ?
group by 1,2,3,4
having item_count <> 0
order by 2;