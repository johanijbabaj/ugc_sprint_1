#!/bin/bash
set -e

clickhouse client -n <<-EOSQL
  CREATE DATABASE IF NOT EXISTS shard;
  CREATE DATABASE IF NOT EXISTS replica;

  CREATE TABLE IF NOT EXISTS shard.test (id Int64, event_time DateTime) Engine=ReplicatedMergeTree('/clickhouse/tables/shard1/test', 'replica_1') PARTITION BY toYYYYMMDD(event_time) ORDER BY id;

  CREATE TABLE IF NOT EXISTS replica.test (id Int64, event_time DateTime) Engine=ReplicatedMergeTree('/clickhouse/tables/shard2/test', 'replica_2') PARTITION BY toYYYYMMDD(event_time) ORDER BY id;

  CREATE TABLE IF NOT EXISTS default.test (id Int64, event_time DateTime) ENGINE = Distributed('company_cluster', '', test, rand());

EOSQL