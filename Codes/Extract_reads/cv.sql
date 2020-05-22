create VIEW BIO AS
    select DISTINCT *
    from (startPOS left join sam on S_Header = REFNAME);
