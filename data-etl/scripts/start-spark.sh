#!/bin/bash
## CREDIT: https://dev.to/mvillarrealb/creating-a-spark-standalone-cluster-with-docker-and-docker-compose-2021-update-6l4
. "/opt/spark/bin/load-spark-env.sh"
# When the spark work_load is master run class org.apache.spark.deploy.master.Master
if [ "$SPARK_WORKLOAD" == "master" ];
then

SPARK_MASTER_HOST="$(hostname)"
export SPARK_MASTER_HOST

# shellcheck disable=SC2153
cd /opt/spark/bin && ./spark-class org.apache.spark.deploy.master.Master --ip "$SPARK_MASTER_HOST" --port "$SPARK_MASTER_PORT" --webui-port "$SPARK_MASTER_WEBUI_PORT" >> "$SPARK_MASTER_LOG"

elif [ "$SPARK_WORKLOAD" == "worker" ];
then
# When the spark work_load is worker run class org.apache.spark.deploy.master.Worker
# shellcheck disable=SC2086
cd /opt/spark/bin && ./spark-class org.apache.spark.deploy.worker.Worker --webui-port $SPARK_WORKER_WEBUI_PORT "$SPARK_MASTER" >> $SPARK_WORKER_LOG

elif [ "$SPARK_WORKLOAD" == "submit" ];
then
    echo "SPARK SUBMIT"
else
    echo "Undefined Workload Type $SPARK_WORKLOAD, must specify: master, worker, submit"
fi