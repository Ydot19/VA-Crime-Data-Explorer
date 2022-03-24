#!/bin/bash
set -x

export HOST_CERTS_DIR="./spark_bulk_data/temp/certs"
mkdir -p "$HOST_CERTS_DIR"
cp -r "$CRDB_CERTS"/*  "$HOST_CERTS_DIR"

set +x