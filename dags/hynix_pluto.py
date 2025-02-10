from airflow import DAG
import pendulum
from airflow.operators.python import PythonOperator
from airflow.providers.sftp.operators.sftp import SFTPHook, SFTPOperator

sftp_hook = SFTPHook(ssh_conn_id=None, username="SYP", remote_host="154.53.56.101", cmd_timeout=None)

with DAG(
        dag_id='hynix_pluto',
        start_date=pendulum.datetime(2024, 7, 1, tz='Asia/Seoul'),
        schedule=None,
        catchup=False
) as dag:
    
    put_file = SFTPOperator(
        task_id="put_file",
        ssh_hook = sftp_hook,
        local_filepath="/opt/airflow/config/10080.py",
        remote_filepath="10080.py",
        operation="get",
        create_intermediate_dirs=True,
        dag=dag
    )

put_file