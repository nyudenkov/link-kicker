-- upgrade --
ALTER TABLE "statisticsrecord" ALTER COLUMN "intent" TYPE VARCHAR(10) USING "intent"::VARCHAR(10);
ALTER TABLE "user" ADD "mailing" BOOL NOT NULL  DEFAULT True;
-- downgrade --
ALTER TABLE "user" DROP COLUMN "mailing";
ALTER TABLE "statisticsrecord" ALTER COLUMN "intent" TYPE VARCHAR(10) USING "intent"::VARCHAR(10);
