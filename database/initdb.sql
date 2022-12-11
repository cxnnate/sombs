CREATE TABLE IF NOT EXISTS tweets
(
    created_at VARCHAR NOT NULL,
    id VARCHAR NOT NULL,
    tweet VARCHAR NOT NULL,
    hashtags VARCHAR NOT NULL
    user_id VARCHAR NOT NULL

    PRIMARY KEY(name)
);

CREATE TABLE IF NOT EXISTS users
(
    created_at VARCHAR NOT NULL,
    id VARCHAR NOT NULL,
    tweet VARCHAR NOT NULL,
    hashtags VARCHAR NOT NULL

    PRIMARY KEY(name)
);
