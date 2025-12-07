
create table if not exists dim_icon (
    icon_path text primary key not null unique
);

create table if not exists dim_inventory (
    inv_ck integer primary key not null unique,
    inv_name text not null,
    inv_desc text,
    child_ind integer default 0,
    inv_type text,
    equip_location text,
    rarity text,
    icon_path text default 'uncertainty.png',
    weight_lbs integer,
    
    foreign key (icon_path) references dim_icon(icon_path) ON DELETE SET DEFAULT
);

create table if not exists dim_character (
    char_ck integer primary key not null unique,
    char_name text not null,

    str_score integer,
    dex_score integer,
    con_score integer,
    int_score integer,
    wis_score integer,
    cha_score integer,

    size_cat text check(size_cat in ('Fine','Diminutive','Tiny','Small','Medium','Large','Huge','Gargantuan','Colossal')),

    light_band integer,
    medium_band integer,
    heavy_band integer,

    created_at text default CURRENT_TIMESTAMP,
    updated_at text default CURRENT_TIMESTAMP
);

