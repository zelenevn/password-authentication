CREATE TABLE users (
    id      SERIAL          PRIMARY KEY,
    nickname    VARCHAR(40)     NOT NULL    UNIQUE
);


CREATE TABLE password (
    id          SERIAL          PRIMARY KEY,
    value       VARCHAR(40)     NOT NULL,
    user_id     INT             NOT NULL    UNIQUE      REFERENCES users (id) ON DELETE CASCADE
);


CREATE TABLE time_between_presses (
    id              BIGSERIAL          PRIMARY KEY,
    gap_number      INT                NOT NULL,
    time            INT                NOT NULL,
    password_id     INT                NOT NULL         REFERENCES password (id) ON DELETE CASCADE
);

CREATE TABLE key_press_time (
    id              BIGSERIAL          PRIMARY KEY,
    gap_number      INT                NOT NULL,
    time            INT                NOT NULL,
    password_id     INT                NOT NULL         REFERENCES password (id) ON DELETE CASCADE
);

DROP TABLE key_press_time;
DROP TABLE time_between_presses;
DROP TABLE password;
DROP TABLE users;