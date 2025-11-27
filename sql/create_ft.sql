
create table if not exists ft_inventory (
    inv_trans_ck integer primary key not null unique,
    inv_ck integer not null,
    char_ck integer not null,
    val integer not null,

    foreign key (inv_ck) references dim_inventory(inv_ck) on delete cascade,
    foreign key (char_ck) references dim_character(char_ck) on delete cascade
);

