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
- Quick links: [Certification page & exam guide](https://www.databricks.com/learn/certification/data-engineer-associate) · [Databricks Academy](https://customer-academy.databricks.com/) · [Free Edition](https://www.databricks.com/learn/free-edition) · [Databricks docs](https://docs.databricks.com/aws/en/) · [Databricks YouTube channel](https://www.youtube.com/@Databricks)
- Each day below has 📖 docs links and ▶️ YouTube searches (searches surface the newest videos — prefer recent uploads, since names changed: DLT → Lakeflow Declarative Pipelines, Workflows → Lakeflow Jobs).

---

## Week 1 — Platform & Delta Lake Foundations
*Goal: understand the lakehouse, navigate the workspace, master Delta Lake basics.*

- [ ] **Day 1 (2026-11-30)** — Lakehouse architecture: control plane vs. data plane, workspace tour, Free Edition setup. Read the exam guide end-to-end.
	- 📖 [High-level architecture](https://docs.databricks.com/aws/en/getting-started/high-level-architecture) · [Lakehouse architecture](https://docs.databricks.com/aws/en/lakehouse-architecture/) · [Free Edition setup](https://docs.databricks.com/aws/en/getting-started/free-edition) · [Exam guide / cert page](https://www.databricks.com/learn/certification/data-engineer-associate)
	- ▶️ [databricks lakehouse architecture control plane data plane](https://www.youtube.com/results?search_query=databricks+lakehouse+architecture+control+plane+data+plane) · [databricks free edition tutorial](https://www.youtube.com/results?search_query=databricks+free+edition+tutorial)
- [ ] **Day 2 (2026-12-01)** — Compute: all-purpose vs. job clusters, serverless compute, SQL warehouses, cluster modes/access modes, Photon, runtime versions. When to pick which.
	- 📖 [Compute overview](https://docs.databricks.com/aws/en/compute/) · [Serverless compute](https://docs.databricks.com/aws/en/compute/serverless/) · [SQL warehouses](https://docs.databricks.com/aws/en/compute/sql-warehouse/) · [Compute config & access modes](https://docs.databricks.com/aws/en/compute/configure) · [Photon](https://docs.databricks.com/aws/en/compute/photon)
	- ▶️ [databricks all purpose vs job cluster serverless](https://www.youtube.com/results?search_query=databricks+all+purpose+vs+job+cluster+serverless) · [databricks sql warehouse photon explained](https://www.youtube.com/results?search_query=databricks+sql+warehouse+photon+explained)
- [ ] **Day 3 (2026-12-02)** — Notebooks & dev tooling: magic commands (`%sql`, `%python`, `%run`, `%pip`), `dbutils`, widgets, Git folders (Repos), Databricks Connect.
	- 📖 [Notebooks](https://docs.databricks.com/aws/en/notebooks/) · [Magic commands / code](https://docs.databricks.com/aws/en/notebooks/notebooks-code) · [dbutils](https://docs.databricks.com/aws/en/dev-tools/databricks-utils) · [Widgets](https://docs.databricks.com/aws/en/notebooks/widgets) · [Git folders](https://docs.databricks.com/aws/en/repos/) · [Databricks Connect](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/)
	- ▶️ [databricks notebooks magic commands dbutils](https://www.youtube.com/results?search_query=databricks+notebooks+magic+commands+dbutils) · [databricks git folders repos tutorial](https://www.youtube.com/results?search_query=databricks+git+folders+repos+tutorial)
- [ ] **Day 4 (2026-12-03)** — Delta Lake core: transaction log (`_delta_log`), ACID, `CREATE TABLE`, managed vs. external tables, `DESCRIBE DETAIL/HISTORY`.
	- 📖 [What is Delta Lake](https://docs.databricks.com/aws/en/delta/) · [Managed tables](https://docs.databricks.com/aws/en/tables/managed) · [External tables](https://docs.databricks.com/aws/en/tables/external) · [Table details](https://docs.databricks.com/aws/en/tables/operations/table-details) · [Table history](https://docs.databricks.com/aws/en/tables/history)
	- ▶️ [delta lake transaction log explained](https://www.youtube.com/results?search_query=delta+lake+transaction+log+explained) · [databricks managed vs external tables](https://www.youtube.com/results?search_query=databricks+managed+vs+external+tables)
- [ ] **Day 5 (2026-12-04)** — Delta DML: `INSERT`, `UPDATE`, `DELETE`, `MERGE INTO` (upserts, SCD Type 1), `INSERT OVERWRITE` vs. `CREATE OR REPLACE`.
	- 📖 [MERGE (upserts)](https://docs.databricks.com/aws/en/delta/merge) · [MERGE INTO reference](https://docs.databricks.com/aws/en/sql/language-manual/delta-merge-into) · [INSERT reference](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-dml-insert-into)
	- ▶️ [databricks delta merge into upsert scd type 1](https://www.youtube.com/results?search_query=databricks+delta+merge+into+upsert+scd+type+1) · [databricks insert overwrite vs create or replace table](https://www.youtube.com/results?search_query=databricks+insert+overwrite+vs+create+or+replace+table)
- [ ] **Day 6 (2026-12-05)** — Delta maintenance: time travel (`VERSION AS OF`/`TIMESTAMP AS OF`), `RESTORE`, `OPTIMIZE`, Z-ordering, **liquid clustering**, `VACUUM` & retention, deletion vectors.
	- 📖 [Time travel / history](https://docs.databricks.com/aws/en/tables/history) · [OPTIMIZE](https://docs.databricks.com/aws/en/tables/operations/optimize) · [Liquid clustering](https://docs.databricks.com/aws/en/tables/clustering) · [Data skipping & Z-order](https://docs.databricks.com/aws/en/tables/data-skipping) · [VACUUM](https://docs.databricks.com/aws/en/tables/operations/vacuum) · [Deletion vectors](https://docs.databricks.com/aws/en/tables/features/deletion-vectors)
	- ▶️ [databricks delta time travel vacuum optimize zorder](https://www.youtube.com/results?search_query=databricks+delta+time+travel+vacuum+optimize+zorder) · [databricks liquid clustering explained](https://www.youtube.com/results?search_query=databricks+liquid+clustering+explained)
- [ ] **Day 7 (2026-12-06)** — Review + 15 practice questions on Weeks 1 topics. Note weak spots below.
	- 📖 [Exam guide / cert page](https://www.databricks.com/learn/certification/data-engineer-associate)
	- ▶️ [databricks data engineer associate practice questions](https://www.youtube.com/results?search_query=databricks+data+engineer+associate+practice+questions)

## Week 2 — Ingestion & Transformation (≈60% of the exam)
*Goal: get data in and reshape it fluently in SQL and PySpark.*

- [ ] **Day 8 (2026-12-07)** — Querying files directly (`SELECT * FROM json.\`path\``, `read_files`), CTAS, views vs. temp views vs. global temp views.
	- 📖 [Query data / files](https://docs.databricks.com/aws/en/query/) · [read_files](https://docs.databricks.com/aws/en/sql/language-manual/functions/read_files) · [Views](https://docs.databricks.com/aws/en/views/) · [CREATE TABLE [USING] / CTAS](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-ddl-create-table-using)
	- ▶️ [databricks query files directly read_files ctas](https://www.youtube.com/results?search_query=databricks+query+files+directly+read_files+ctas) · [databricks views vs temp views vs global temp views](https://www.youtube.com/results?search_query=databricks+views+vs+temp+views+vs+global+temp+views)
- [ ] **Day 9 (2026-12-08)** — `COPY INTO` (idempotent batch ingest) vs. **Auto Loader** (`cloudFiles`): schema inference, schema evolution, `rescued_data`, checkpoints.
	- 📖 [COPY INTO](https://docs.databricks.com/aws/en/ingestion/cloud-object-storage/copy-into/) · [Auto Loader](https://docs.databricks.com/aws/en/ingestion/cloud-object-storage/auto-loader/) · [Auto Loader schema inference & evolution](https://docs.databricks.com/aws/en/ingestion/cloud-object-storage/auto-loader/schema)
	- ▶️ [databricks auto loader tutorial schema evolution](https://www.youtube.com/results?search_query=databricks+auto+loader+tutorial+schema+evolution) · [databricks copy into vs auto loader](https://www.youtube.com/results?search_query=databricks+copy+into+vs+auto+loader)
- [ ] **Day 10 (2026-12-09)** — Lakeflow Connect / managed connectors, Lakehouse Federation, volumes (UC Volumes) for files.
	- 📖 [Lakeflow Connect](https://docs.databricks.com/aws/en/ingestion/lakeflow-connect/) · [Lakehouse Federation](https://docs.databricks.com/aws/en/query-federation/) · [UC Volumes](https://docs.databricks.com/aws/en/volumes/)
	- ▶️ [databricks lakeflow connect](https://www.youtube.com/results?search_query=databricks+lakeflow+connect) · [databricks lakehouse federation](https://www.youtube.com/results?search_query=databricks+lakehouse+federation) · [databricks unity catalog volumes](https://www.youtube.com/results?search_query=databricks+unity+catalog+volumes)
- [ ] **Day 11 (2026-12-10)** — Spark SQL transforms: joins, `GROUP BY`, window functions, CTEs, `PIVOT`, `CASE`, dedup (`DISTINCT`, `ROW_NUMBER`).
	- 📖 [Window functions](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-window-functions) · [CTEs](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-qry-select-cte) · [PIVOT](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-qry-select-pivot)
	- ▶️ [spark sql window functions row_number tutorial](https://www.youtube.com/results?search_query=spark+sql+window+functions+row_number+tutorial) · [databricks sql pivot cte](https://www.youtube.com/results?search_query=databricks+sql+pivot+cte)
- [ ] **Day 12 (2026-12-11)** — Complex data: structs, arrays, `explode`, `:` JSON path syntax, `from_json`, higher-order functions (`transform`, `filter`, `exists`), SQL UDFs.
	- 📖 [Query JSON (`:` syntax)](https://docs.databricks.com/aws/en/semi-structured/json) · [Complex types](https://docs.databricks.com/aws/en/semi-structured/complex-types) · [Higher-order functions](https://docs.databricks.com/aws/en/semi-structured/higher-order-functions) · [UDFs (incl. SQL UDFs)](https://docs.databricks.com/aws/en/udf/)
	- ▶️ [databricks explode from_json struct array](https://www.youtube.com/results?search_query=databricks+explode+from_json+struct+array) · [spark sql higher order functions transform filter](https://www.youtube.com/results?search_query=spark+sql+higher+order+functions+transform+filter)
- [ ] **Day 13 (2026-12-12)** — PySpark DataFrame API equivalents of Days 11–12; Python UDFs vs. pandas UDFs; when to avoid UDFs.
	- 📖 [PySpark on Databricks](https://docs.databricks.com/aws/en/pyspark/) · [DataFrames tutorial](https://docs.databricks.com/aws/en/getting-started/dataframes) · [Python UDFs](https://docs.databricks.com/aws/en/udf/python) · [pandas UDFs](https://docs.databricks.com/aws/en/udf/pandas)
	- ▶️ [pyspark dataframe api tutorial databricks](https://www.youtube.com/results?search_query=pyspark+dataframe+api+tutorial+databricks) · [pyspark pandas udf vs python udf performance](https://www.youtube.com/results?search_query=pyspark+pandas+udf+vs+python+udf+performance)
- [ ] **Day 14 (2026-12-13)** — Review + 20 practice questions on ingestion & transforms.
	- 📖 [Exam guide / cert page](https://www.databricks.com/learn/certification/data-engineer-associate)
	- ▶️ [databricks data engineer associate auto loader spark sql practice questions](https://www.youtube.com/results?search_query=databricks+data+engineer+associate+auto+loader+spark+sql+practice+questions)

## Week 3 — Streaming, Pipelines & Production
*Goal: build incremental pipelines and run them in production.*

- [ ] **Day 15 (2026-12-14)** — Structured Streaming: `readStream`/`writeStream`, triggers (`availableNow`, `processingTime`), output modes, checkpointing, exactly-once.
	- 📖 [Structured Streaming concepts](https://docs.databricks.com/aws/en/structured-streaming/concepts) · [Triggers](https://docs.databricks.com/aws/en/structured-streaming/triggers) · [Output modes](https://docs.databricks.com/aws/en/structured-streaming/output-mode) · [Checkpoints](https://docs.databricks.com/aws/en/structured-streaming/checkpoints)
	- ▶️ [databricks structured streaming tutorial checkpoint trigger availableNow](https://www.youtube.com/results?search_query=databricks+structured+streaming+tutorial+checkpoint+trigger+availableNow) · [spark structured streaming output modes](https://www.youtube.com/results?search_query=spark+structured+streaming+output+modes)
- [ ] **Day 16 (2026-12-15)** — Medallion architecture (bronze/silver/gold) — build a 3-hop pipeline with Auto Loader + streaming tables.
	- 📖 [Medallion architecture](https://docs.databricks.com/aws/en/lakehouse/medallion) · [Streaming tables](https://docs.databricks.com/aws/en/ldp/concepts/streaming-tables) · [Auto Loader](https://docs.databricks.com/aws/en/ingestion/cloud-object-storage/auto-loader/)
	- ▶️ [databricks medallion architecture bronze silver gold](https://www.youtube.com/results?search_query=databricks+medallion+architecture+bronze+silver+gold) · [databricks medallion pipeline auto loader demo](https://www.youtube.com/results?search_query=databricks+medallion+pipeline+auto+loader+demo)
- [ ] **Day 17 (2026-12-16)** — **Lakeflow Declarative Pipelines** (formerly DLT): streaming tables vs. materialized views, `CREATE OR REFRESH`, `STREAM()`, triggered vs. continuous, development vs. production mode.
	- 📖 [Lakeflow Declarative Pipelines](https://docs.databricks.com/aws/en/ldp/) · [Streaming tables](https://docs.databricks.com/aws/en/ldp/concepts/streaming-tables) · [Materialized views](https://docs.databricks.com/aws/en/ldp/concepts/materialized-views)
	- ▶️ [lakeflow declarative pipelines tutorial](https://www.youtube.com/results?search_query=lakeflow+declarative+pipelines+tutorial) · [delta live tables streaming table vs materialized view](https://www.youtube.com/results?search_query=delta+live+tables+streaming+table+vs+materialized+view)
- [ ] **Day 18 (2026-12-17)** — Pipeline expectations (`EXPECT ... ON VIOLATION DROP ROW / FAIL UPDATE`), event log, `APPLY CHANGES` / AUTO CDC (SCD Type 1 & 2).
	- 📖 [Expectations](https://docs.databricks.com/aws/en/ldp/expectations) · [Event log / observability](https://docs.databricks.com/aws/en/ldp/observability) · [AUTO CDC / APPLY CHANGES](https://docs.databricks.com/aws/en/ldp/cdc)
	- ▶️ [delta live tables expectations data quality](https://www.youtube.com/results?search_query=delta+live+tables+expectations+data+quality) · [databricks apply changes auto cdc scd type 2](https://www.youtube.com/results?search_query=databricks+apply+changes+auto+cdc+scd+type+2)
- [ ] **Day 19 (2026-12-18)** — **Lakeflow Jobs**: tasks, dependencies (DAGs), task values, retries, schedules & file-arrival triggers, repair runs, notifications.
	- 📖 [Lakeflow Jobs](https://docs.databricks.com/aws/en/jobs/) · [Task values](https://docs.databricks.com/aws/en/jobs/task-values) · [Triggers & schedules](https://docs.databricks.com/aws/en/jobs/triggers) · [File-arrival triggers](https://docs.databricks.com/aws/en/jobs/file-arrival-triggers) · [Repair runs](https://docs.databricks.com/aws/en/jobs/repair-job-failures) · [Notifications](https://docs.databricks.com/aws/en/jobs/notifications)
	- ▶️ [databricks lakeflow jobs workflows tutorial](https://www.youtube.com/results?search_query=databricks+lakeflow+jobs+workflows+tutorial) · [databricks jobs task values repair run](https://www.youtube.com/results?search_query=databricks+jobs+task+values+repair+run)
- [ ] **Day 20 (2026-12-19)** — **Databricks Asset Bundles** (DABs): `databricks.yml`, targets (dev/prod), `bundle validate/deploy/run`, CI/CD basics. Serverless jobs & cost/performance tips.
	- 📖 [Asset Bundles](https://docs.databricks.com/aws/en/dev-tools/bundles/) · [Bundle config (databricks.yml)](https://docs.databricks.com/aws/en/dev-tools/bundles/settings) · [CI/CD](https://docs.databricks.com/aws/en/dev-tools/ci-cd/)
	- ▶️ [databricks asset bundles tutorial](https://www.youtube.com/results?search_query=databricks+asset+bundles+tutorial) · [databricks asset bundles ci cd github actions](https://www.youtube.com/results?search_query=databricks+asset+bundles+ci+cd+github+actions)
- [ ] **Day 21 (2026-12-20)** — Review + 20 practice questions on streaming, pipelines & jobs.
	- 📖 [Exam guide / cert page](https://www.databricks.com/learn/certification/data-engineer-associate)
	- ▶️ [databricks data engineer associate streaming delta live tables jobs practice questions](https://www.youtube.com/results?search_query=databricks+data+engineer+associate+streaming+delta+live+tables+jobs+practice+questions)

## Week 4 — Governance, Quality & Exam Readiness
*Goal: close the governance gap, then drill full-length practice.*

- [ ] **Day 22 (2026-12-21)** — **Unity Catalog**: metastore → catalog → schema → table/view/volume/function; managed vs. external locations, storage credentials.
	- 📖 [Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/) · [External locations & storage credentials](https://docs.databricks.com/aws/en/connect/unity-catalog/cloud-storage/)
	- ▶️ [databricks unity catalog explained metastore catalog schema](https://www.youtube.com/results?search_query=databricks+unity+catalog+explained+metastore+catalog+schema) · [unity catalog external location storage credential](https://www.youtube.com/results?search_query=unity+catalog+external+location+storage+credential)
- [ ] **Day 23 (2026-12-22)** — UC security: `GRANT`/`REVOKE`, privileges (`USE CATALOG`, `USE SCHEMA`, `SELECT`, `MODIFY`), ownership, row filters & column masks, dynamic views.
	- 📖 [Manage privileges](https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-privileges/) · [Privileges reference](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/privileges-reference) · [Row filters & column masks](https://docs.databricks.com/aws/en/data-governance/unity-catalog/filters-and-masks) · [Dynamic views](https://docs.databricks.com/aws/en/views/dynamic)
	- ▶️ [unity catalog grant privileges tutorial](https://www.youtube.com/results?search_query=unity+catalog+grant+privileges+tutorial) · [databricks row filters column masks](https://www.youtube.com/results?search_query=databricks+row+filters+column+masks)
- [ ] **Day 24 (2026-12-23)** — Lineage, audit & **system tables**, Delta Sharing (open vs. Databricks-to-Databricks), data quality patterns.
	- 📖 [Data lineage](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-lineage) · [System tables](https://docs.databricks.com/aws/en/admin/system-tables/) · [Delta Sharing](https://docs.databricks.com/aws/en/delta-sharing/)
	- ▶️ [databricks unity catalog lineage system tables](https://www.youtube.com/results?search_query=databricks+unity+catalog+lineage+system+tables) · [databricks delta sharing explained](https://www.youtube.com/results?search_query=databricks+delta+sharing+explained)
- [ ] **Day 25 (2026-12-24)** — **Full practice exam #1** (45 Q, 90 min timed). Score it and log misses.
	- 📖 [Exam guide / cert page](https://www.databricks.com/learn/certification/data-engineer-associate)
	- ▶️ [databricks certified data engineer associate full practice exam](https://www.youtube.com/results?search_query=databricks+certified+data+engineer+associate+full+practice+exam)
- [ ] **Day 26 (2026-12-25)** — Review every miss from Exam #1; re-read docs for the weakest domain.
	- 📖 [Exam guide / cert page](https://www.databricks.com/learn/certification/data-engineer-associate)
	- ▶️ [databricks data engineer associate exam tips](https://www.youtube.com/results?search_query=databricks+data+engineer+associate+exam+tips)
- [ ] **Day 27 (2026-12-26)** — **Full practice exam #2** (timed). Target ≥ 80%.
	- 📖 [Exam guide / cert page](https://www.databricks.com/learn/certification/data-engineer-associate)
	- ▶️ [databricks certified data engineer associate practice exam questions answers](https://www.youtube.com/results?search_query=databricks+certified+data+engineer+associate+practice+exam+questions+answers)
- [ ] **Day 28 (2026-12-27)** — Final review: cheat sheet below, weak-spot list, light lab. Book/confirm exam slot.
	- 📖 [Exam guide / cert page](https://www.databricks.com/learn/certification/data-engineer-associate)
	- ▶️ [databricks data engineer associate exam review cram](https://www.youtube.com/results?search_query=databricks+data+engineer+associate+exam+review+cram)

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
