create table logs (
    id  INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
    log        text,
    tag        text,
    created_at datetime default current_date,
    updated_at datetime default current_date
);

create index logs_create_index
    on logs (created_at);

create index logs_id_index
    on logs (id);

create index logs_tags_index
    on logs (tag);


