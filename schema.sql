CREATE TABLE users (
        id INTEGER NOT NULL,
        username VARCHAR,
        password VARCHAR,
        PRIMARY KEY (id)
);
CREATE TABLE symbols (
        id INTEGER NOT NULL,
        name VARCHAR,
        symbol VARCHAR,
        PRIMARY KEY (id)
);
CREATE TABLE watchlists (
        id INTEGER NOT NULL,
        user_id INTEGER,
        name VARCHAR,
        description VARCHAR,
        PRIMARY KEY (id),
        FOREIGN KEY(user_id) REFERENCES users (id)
);
CREATE TABLE watchlist_items (
        id INTEGER NOT NULL,
        watchlist_id INTEGER,
        symbol_id INTEGER,
        PRIMARY KEY (id),
        FOREIGN KEY(watchlist_id) REFERENCES watchlists (id),
        FOREIGN KEY(symbol_id) REFERENCES symbols (id)
);