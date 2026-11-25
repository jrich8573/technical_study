---
title: Databricks Certified Data Engineer Associate – 4-Week Study Plan
start_date: 2026-11-30
daily_minutes: 60
exam_target: 2026-12-28
tags: [study, databricks, certification]
---

# Databricks Certified Data Engineer Associate — 4-Week Plan

**Commitment:** 1 hour/day, 28 days. Start **Mon 2026-11-30** → exam week of **2026-12-28**.
**How progress is tracked:** check off each day (`- [x]`) when done. The daily reminder agent reads this file each morning, counts completed vs. expected days, and texts you today's task.

> [!info] Exam at a glance
> - 45 scored multiple-choice questions · 90 minutes · ~$200 USD · online proctored (Kryterion/Webassessor)
> - No prerequisites; ~6 months hands-on recommended
> - Domains (approx. weights):
>   1. **Databricks Intelligence Platform** — ~10%
>   2. **Development & Ingestion** — ~30%
>   3. **Data Processing & Transformations** — ~31%
>   4. **Productionizing Data Pipelines** — ~18%
>   5. **Data Governance & Quality** — ~11%
> - Always confirm the latest exam guide on the Databricks certification page before booking — weights/terminology shift (e.g. DLT → **Lakeflow Declarative Pipelines**, Workflows → **Lakeflow Jobs**).

## Resources
- **Databricks Free Edition** (hands-on workspace, free) — do every lab here
- Databricks Academy: *Data Engineering with Databricks* learning path (free self-paced)
- Official exam guide (PDF) on the certification page
- Databricks docs: Delta Lake, Unity Catalog, Auto Loader, Lakeflow Declarative Pipelines, Lakeflow Jobs, Asset Bundles
- Practice exams: official practice test + one reputable third-party set (Udemy etc.)

---

## Week 1 — Platform & Delta Lake Foundations
*Goal: understand the lakehouse, navigate the workspace, master Delta Lake basics.*

- [ ] **Day 1 (2026-11-30)** — Lakehouse architecture: control plane vs. data plane, workspace tour, Free Edition setup. Read the exam guide end-to-end.
- [ ] **Day 2 (2026-12-01)** — Compute: all-purpose vs. job clusters, serverless compute, SQL warehouses, cluster modes/access modes, Photon, runtime versions. When to pick which.
- [ ] **Day 3 (2026-12-02)** — Notebooks & dev tooling: magic commands (`%sql`, `%python`, `%run`, `%pip`), `dbutils`, widgets, Git folders (Repos), Databricks Connect.
- [ ] **Day 4 (2026-12-03)** — Delta Lake core: transaction log (`_delta_log`), ACID, `CREATE TABLE`, managed vs. external tables, `DESCRIBE DETAIL/HISTORY`.
- [ ] **Day 5 (2026-12-04)** — Delta DML: `INSERT`, `UPDATE`, `DELETE`, `MERGE INTO` (upserts, SCD Type 1), `INSERT OVERWRITE` vs. `CREATE OR REPLACE`.
- [ ] **Day 6 (2026-12-05)** — Delta maintenance: time travel (`VERSION AS OF`/`TIMESTAMP AS OF`), `RESTORE`, `OPTIMIZE`, Z-ordering, **liquid clustering**, `VACUUM` & retention, deletion vectors.
- [ ] **Day 7 (2026-12-06)** — Review + 15 practice questions on Weeks 1 topics. Note weak spots below.

## Week 2 — Ingestion & Transformation (≈60% of the exam)
*Goal: get data in and reshape it fluently in SQL and PySpark.*

- [ ] **Day 8 (2026-12-07)** — Querying files directly (`SELECT * FROM json.\`path\``, `read_files`), CTAS, views vs. temp views vs. global temp views.
- [ ] **Day 9 (2026-12-08)** — `COPY INTO` (idempotent batch ingest) vs. **Auto Loader** (`cloudFiles`): schema inference, schema evolution, `rescued_data`, checkpoints.
- [ ] **Day 10 (2026-12-09)** — Lakeflow Connect / managed connectors, Lakehouse Federation, volumes (UC Volumes) for files.
- [ ] **Day 11 (2026-12-10)** — Spark SQL transforms: joins, `GROUP BY`, window functions, CTEs, `PIVOT`, `CASE`, dedup (`DISTINCT`, `ROW_NUMBER`).
- [ ] **Day 12 (2026-12-11)** — Complex data: structs, arrays, `explode`, `:` JSON path syntax, `from_json`, higher-order functions (`transform`, `filter`, `exists`), SQL UDFs.
- [ ] **Day 13 (2026-12-12)** — PySpark DataFrame API equivalents of Days 11–12; Python UDFs vs. pandas UDFs; when to avoid UDFs.
- [ ] **Day 14 (2026-12-13)** — Review + 20 practice questions on ingestion & transforms.

## Week 3 — Streaming, Pipelines & Production
*Goal: build incremental pipelines and run them in production.*

- [ ] **Day 15 (2026-12-14)** — Structured Streaming: `readStream`/`writeStream`, triggers (`availableNow`, `processingTime`), output modes, checkpointing, exactly-once.
- [ ] **Day 16 (2026-12-15)** — Medallion architecture (bronze/silver/gold) — build a 3-hop pipeline with Auto Loader + streaming tables.
- [ ] **Day 17 (2026-12-16)** — **Lakeflow Declarative Pipelines** (formerly DLT): streaming tables vs. materialized views, `CREATE OR REFRESH`, `STREAM()`, triggered vs. continuous, development vs. production mode.
- [ ] **Day 18 (2026-12-17)** — Pipeline expectations (`EXPECT ... ON VIOLATION DROP ROW / FAIL UPDATE`), event log, `APPLY CHANGES` / AUTO CDC (SCD Type 1 & 2).
- [ ] **Day 19 (2026-12-18)** — **Lakeflow Jobs**: tasks, dependencies (DAGs), task values, retries, schedules & file-arrival triggers, repair runs, notifications.
- [ ] **Day 20 (2026-12-19)** — **Databricks Asset Bundles** (DABs): `databricks.yml`, targets (dev/prod), `bundle validate/deploy/run`, CI/CD basics. Serverless jobs & cost/performance tips.
- [ ] **Day 21 (2026-12-20)** — Review + 20 practice questions on streaming, pipelines & jobs.

## Week 4 — Governance, Quality & Exam Readiness
*Goal: close the governance gap, then drill full-length practice.*

- [ ] **Day 22 (2026-12-21)** — **Unity Catalog**: metastore → catalog → schema → table/view/volume/function; managed vs. external locations, storage credentials.
- [ ] **Day 23 (2026-12-22)** — UC security: `GRANT`/`REVOKE`, privileges (`USE CATALOG`, `USE SCHEMA`, `SELECT`, `MODIFY`), ownership, row filters & column masks, dynamic views.
- [ ] **Day 24 (2026-12-23)** — Lineage, audit & **system tables**, Delta Sharing (open vs. Databricks-to-Databricks), data quality patterns.
- [ ] **Day 25 (2026-12-24)** — **Full practice exam #1** (45 Q, 90 min timed). Score it and log misses.
- [ ] **Day 26 (2026-12-25)** — Review every miss from Exam #1; re-read docs for the weakest domain.
- [ ] **Day 27 (2026-12-26)** — **Full practice exam #2** (timed). Target ≥ 80%.
- [ ] **Day 28 (2026-12-27)** — Final review: cheat sheet below, weak-spot list, light lab. Book/confirm exam slot.

---

## Cheat Sheet (fill in as you go)
| Concept | Key point |
|---|---|
| `COPY INTO` vs Auto Loader | COPY INTO = idempotent batch, thousands of files; Auto Loader = incremental/streaming, millions of files, schema evolution |
| Managed vs external table | `DROP` on managed deletes data; external keeps files |
| Streaming table vs MV | ST = append/incremental from streaming source; MV = recomputed/incrementally refreshed query result |
| `VACUUM` | Default retention 7 days; breaks time travel to older versions |
| Expectations | warn (default) · `DROP ROW` · `FAIL UPDATE` |
| Job cluster vs all-purpose | Job = ephemeral, cheaper, for prod; all-purpose = interactive dev |

## Weak Spots Log
- 

## Practice Exam Scores
| Date | Source | Score | Weakest domain |
|---|---|---|---|
| | | | |
