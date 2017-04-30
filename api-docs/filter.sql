SELECT * FROM "APIimports_feature"
WHERE canonical_status != 'COMPLETE'
  AND canonical_status != 'COMPLETED'
  AND canonical_status != 'REQUESTED'
  AND canonical_status != 'CANCELED'
  AND canonical_status != 'DENIED'
  AND NOT isempty(canonical_daterange)
  AND neighborhood_id IS NOT NULL
  AND lower(canonical_daterange) >= '2015-01-01'
  AND upper(canonical_daterange) <= '2020-01-01'
ORDER BY canonical_daterange DESC;
