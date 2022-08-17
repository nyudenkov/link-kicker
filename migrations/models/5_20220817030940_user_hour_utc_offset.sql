-- upgrade --
ALTER TABLE "statisticsrecord" ALTER COLUMN "intent" TYPE VARCHAR(10) USING "intent"::VARCHAR(10);
ALTER TABLE "user" ADD "hour_utc_offset" SMALLINT;
-- downgrade --
ALTER TABLE "user" DROP COLUMN "hour_utc_offset";
ALTER TABLE "statisticsrecord" ALTER COLUMN "intent" TYPE VARCHAR(10) USING "intent"::VARCHAR(10);
