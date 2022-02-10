docker exec -ti clickhouse-node1 bash /tmp/init-db_shard1.sh
docker exec -ti clickhouse-node3 bash /tmp/init-db_shard2.sh
docker exec -ti clickhouse-node5 bash /tmp/init-db_shard3.sh