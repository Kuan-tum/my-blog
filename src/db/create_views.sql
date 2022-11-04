CREATE VIEW mini_author (gender,first_name,last_name ) AS (SELECT gender,first_name,last_name FROM author );
CREATE VIEW mini_book (title,location,author_name) AS ( SELECT b.title,b.location,(CONCAT(CONCAT(a.first_name,' '),a.last_name)) FROM book b  INNER JOIN author a ON (a.author_id=b.book_id) );