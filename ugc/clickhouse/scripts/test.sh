#!/bin/bash
set -e

clickhouse client -n <<-EOSQL
  CREATE DATABASE shard;
  CREATE TABLE shard.kafka_store (
      user_id UUID,
      film_id UUID,
      sec Int32,
      watched Boolean
    ) ENGINE = Kafka SETTINGS kafka_broker_list = 'broker:29092',
                              kafka_topic_list = 'movies_watch',
                              kafka_group_name = 'group1',
                              kafka_format = 'JSONEachRow';

  CREATE TABLE shard.view_store(
      user_id UUID,
      film_id UUID,
      sec Int32,
      watched Boolean)
    ENGINE = ReplicatedMergeTree('/clickhouse/tables/{shard}/view_store', 'replica_1')
    ORDER BY user_id;

  CREATE MATERIALIZED VIEW shard.materialized_store TO shard.view_store AS
    SELECT user_id, film_id, sec, watched FROM shard.kafka_store;
EOSQL
