#!/bin/bash
set -e

clickhouse client -n <<-EOSQL
  CREATE DATABASE shard;

  CREATE DATABASE replica;

  CREATE TABLE shard.test (id Int64, film_id UUID, user_id UUID, last_second_film Int64, event_time DateTime) Engine=ReplicatedMergeTree('/clickhouse/tables/shard3/test', 'replica_1') PARTITION BY toYYYYMMDD(event_time) ORDER BY id;

  CREATE TABLE replica.test (id Int64, event_time DateTime) Engine=ReplicatedMergeTree('/clickhouse/tables/shard1/test', 'replica_2') PARTITION BY toYYYYMMDD(event_time) ORDER BY id;

  CREATE TABLE default.test (id Int64, event_time DateTime) ENGINE = Distributed('company_cluster', '', test, rand());
EOSQL
