
copy-crdb-certs:
    # requires CRDBCerts env variable to set
	chmod +x ${PWD}/spark_bulk_data/crdb-copy-certs.sh
	${PWD}/spark_bulk_data/crdb-copy-certs.sh

