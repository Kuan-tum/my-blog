CREATE TABLE IF NOT EXISTS author(
        author_id serial,
        first_name varchar(150) NOT NULL,
        last_name varchar(150) NOT NULL,
        date_added DATE,
        country varchar(100) NOT NULL,
        town varchar(100) NOT NULL,
        profile_pic varchar(200),
        CONSTRAINT author_pk PRIMARY KEY(author_id),
        CONSTRAINT check_empty_string CHECK (TRIM(' .' FROM first_name) <> '' AND TRIM(' .' FROM last_name) <> '' AND TRIM(town) <> '' AND TRIM(country) <> '') 
        
);
CREATE TABLE IF NOT EXISTS book(
    book_id serial,
    author_id int,
    title varchar(500) NOT NULL,
    genre varchar(200) NOT NULL,
    date_added DATE,
    pages int ,
    location varchar(300),
    book_cover varchar(200),

    description text,



    CONSTRAINT book_primary_key PRIMARY KEY(book_id),
    CONSTRAINT author_foreghn_key FOREIGN KEY(author_id) REFERENCES author(author_id),
    CONSTRAINT check_description CHECK(LENGTH(title)>30)

);
CREATE TABLE IF NOT EXISTS quote(
    quote_id serial,
    author_id  int,
    book_id int,
    phrase varchar(1000),

    CONSTRAINT author_quote_fk FOREIGN KEY(author_id) REFERENCES author(author_id),
    CONSTRAINT quote_book_id_fk FOREIGN KEY(book_id)REFERENCES book(book_id),
    CONSTRAINT quote_pk PRIMARY KEY(quote_id)
);
CREATE TABLE IF NOT EXISTS reveiw(
    book_id int NOT NULL,
    finished BOOL,
    date_started DATE,
    date_finished DATE,
    favourite_quote varchar(300),
    reader_views text,

    CONSTRAINT reveiw_book_id_fk FOREIGN KEY(book_id) REFERENCES book(book_id)

);
