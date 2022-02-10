-- upgrade --
ALTER TABLE "statisticsrecord" ALTER COLUMN "intent" TYPE VARCHAR(10) USING "intent"::VARCHAR(10);
-- downgrade --
ALTER TABLE "statisticsrecord" ALTER COLUMN "intent" TYPE VARCHAR(10) USING "intent"::VARCHAR(10);
