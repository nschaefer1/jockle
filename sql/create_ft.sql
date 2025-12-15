
create table if not exists ft_inventory (
    inv_trans_ck integer primary key not null unique,
    inv_ck integer not null,
    char_ck integer not null,
    val integer not null,

    foreign key (inv_ck) references dim_inventory(inv_ck) on delete cascade,
    foreign key (char_ck) references dim_character(char_ck) on delete cascade
);

create table if not exists ft_item_stats (
    stat_ck integer primary key,
    
    inv_ck integer not null,
    stat_name text not null,

    val integer not null,
    
    foreign key (inv_ck) references dim_inventory(inv_ck) on delete cascade,
    unique(inv_ck, stat_name) -- enforcing no duplicates for future updates
);

-- TODO, ensure this is added in when doing inserts
-- insert into ft_item_stats (inv_ck, stat_name, val)
-- values (?, ?, ?)
-- on conflict (inv_ck, stat_name) do update set val = excluded.val;
