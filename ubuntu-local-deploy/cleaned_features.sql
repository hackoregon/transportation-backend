CREATE MATERIALIZED VIEW public.cleaned_features
TABLESPACE pg_default
AS
  SELECT features_with_geography.id,
    features_with_geography.geom,
    features_with_geography.orig_daterange,
    features_with_geography.canonical_daterange,
    features_with_geography.orig_status,
    features_with_geography.canonical_status,
    features_with_geography.source_name,
    features_with_geography.data,
    features_with_geography.source_ref_id,
    features_with_geography.neighborhood_id,
    features_with_geography.geog
  FROM features_with_geography
  WHERE canonical_status != 'COMPLETE'
    AND canonical_status != 'COMPLETED'
    AND canonical_status != 'REQUESTED'
    AND canonical_status != 'CANCELED'
    AND canonical_status != 'DENIED'
    AND NOT isempty(canonical_daterange)
    AND neighborhood_id IS NOT NULL
    AND lower(canonical_daterange) >= '2015-01-01'
    AND upper(canonical_daterange) <= '2020-01-01'
WITH DATA;
