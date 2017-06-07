#!/bin/bash

num_vpcs=$(aws ec2 describe-vpcs | grep -c VPCS)
echo "# VPC: $num_vpcs"

num_ec2=$(aws ec2 describe-instance-status | grep -c "INSTANCESTATUSES")
echo "# EC2: $num_ec2"

num_rds=$(aws rds describe-db-instances | grep -c ENDPOINT)
echo "# RDS: $num_rds"

num_dynamos=$(aws dynamodb list-tables | wc -l)
echo "# DynamoDB: $num_dynamos"

num_elasticache_memcached=$(aws elasticache describe-cache-clusters | grep CACHECLUSTERS | grep -c memcache)
echo "# ElastiCache/Memcache: $num_elasticache_memcached"

num_elasticache_redis=$(aws elasticache describe-cache-clusters | grep CACHECLUSTERS | grep -c redis)
echo "# ElastiCache/Redis: $num_elasticache_redis"

num_cloudsearch=$(aws cloudsearch describe-domains | grep -c SEARCHSERVICE)
echo "# CloudSearch: $num_cloudsearch"
