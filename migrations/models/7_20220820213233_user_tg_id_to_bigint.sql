-- upgrade --
ALTER TABLE "user" ALTER COLUMN "tg_id" TYPE BIGINT USING "tg_id"::BIGINT;
-- downgrade --
ALTER TABLE "user" ALTER COLUMN "tg_id" TYPE INT USING "tg_id"::INT;
