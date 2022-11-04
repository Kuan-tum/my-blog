CREATE FUNCTION  fadd_quote( ) RETURNS trigger AS $$

BEGIN
if new.favourite_quote NOT IN (SELECT phrase FROM quote WHERE quote.author_id=new.author_id AND TRIM(LOWER(quote.phrase))=TRIM(LOWER(quote_text))) 
THEN
    INSERT INTO  quote(phrase,author_id,date_added) VALUES(quote_text,author_id,CURRENT_TIMESTAMP);
END IF;
RETURN NULL;
END;
$$ LANGUAGE 'plpgsql';


CREATE TRIGGER add_quote
AFTER INSERT OR UPDATE ON reveiw
EXECUTE PROCEDURE fadd_quote();
