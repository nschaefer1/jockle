
create table if not exists dim_icon (
    icon_ck integer primary key not null unique,
    icon_path text
);

create table if not exists dim_inventory (
    inv_ck integer primary key not null unique,
    inv_name text not null,
    inv_desc text,
    child_ind integer default 0,
    inv_type text,
    equip_location text,
    rarity text,
    icon_ck integer default 1,
    
    foreign key (icon_ck) references dim_icon(icon_ck)
);

create table if not exists dim_character (
    char_ck integer primary key not null unique,
    char_name text not null,
    created_at text default CURRENT_TIMESTAMP,
    updated_at text default CURRENT_TIMESTAMP
);

