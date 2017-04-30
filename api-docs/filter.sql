SELECT * FROM "APIimports_feature"
WHERE canonical_status != 'COMPLETE'
  AND canonical_status != 'COMPLETED'
  AND canonical_status != 'REQUESTED'
  AND canonical_status != 'CANCELED'
  AND canonical_status != 'DENIED';
