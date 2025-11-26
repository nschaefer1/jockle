

create table if not exists dim_inventory (
    inv_ck integer primary key not null unique,
    inv_name text not null,
    inv_desc text,
    child_ind integer default 0,
    inv_type text,
    equip_location text,
    rarity text
);