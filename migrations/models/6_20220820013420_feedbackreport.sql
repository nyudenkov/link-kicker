-- upgrade --
CREATE TABLE IF NOT EXISTS "feedbackreport" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "dt_create" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "type" VARCHAR(7) NOT NULL,
    "text" TEXT NOT NULL
);
COMMENT ON COLUMN "feedbackreport"."type" IS 'BUG: bug\nFEATURE: feature';;
ALTER TABLE "statisticsrecord" ALTER COLUMN "intent" TYPE VARCHAR(10) USING "intent"::VARCHAR(10);
-- downgrade --
ALTER TABLE "statisticsrecord" ALTER COLUMN "intent" TYPE VARCHAR(10) USING "intent"::VARCHAR(10);
DROP TABLE IF EXISTS "feedbackreport";
