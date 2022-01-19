-- upgrade --
ALTER TABLE "user" ADD "language_iso" VARCHAR(2);
-- downgrade --
ALTER TABLE "user" DROP COLUMN "language_iso";
