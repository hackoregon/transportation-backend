-- View: public.test_mat_view
DROP MATERIALIZED VIEW public.test_mat_view;
CREATE MATERIALIZED VIEW public.test_mat_view
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
    "APIimports_feature".neighborhood_id
   FROM "APIimports_feature"
  WHERE "APIimports_feature".canonical_status::text <> 'COMPLETE'::text AND "APIimports_feature".canonical_status::text <> 'COMPLETED'::text AND "APIimports_feature".canonical_status::text <> 'REQUESTED'::text AND "APIimports_feature".canonical_status::text <> 'CANCELED'::text AND "APIimports_feature".canonical_status::text <> 'DENIED'::text
WITH DATA;
ALTER TABLE public.test_mat_view
    OWNER TO transdev;
CREATE INDEX geom_gist
    ON public.test_mat_view USING gist
    (geom)
    TABLESPACE pg_default;
VACUUM ANALYZE test_mat_view;
