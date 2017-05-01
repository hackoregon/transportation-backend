CREATE MATERIALIZED VIEW public.features_with_geography
TABLESPACE pg_default
AS
 SELECT "APIimports_feature".id,
    "APIimports_feature".geom,
    "APIimports_feature".orig_daterange,
    "APIimports_feature".canonical_daterange,
    "APIimports_feature".orig_status,
    "APIimports_feature".canonical_status,
    "APIimports_feature".source_name,
    "APIimports_feature".data,
    "APIimports_feature".source_ref_id,
    "APIimports_feature".neighborhood_id,
    geography("APIimports_feature".geom) AS geog
   FROM "APIimports_feature"
WITH DATA;
