import mysql.connector
from sshtunnel import SSHTunnelForwarder
import paramiko

# SSH details
ssh_host = 'compsci.adelphi.edu'  # The SSH server IP or hostname
ssh_port = 22  # SSH port, usually 22
ssh_user = 'larrymoreno'
ssh_key_path = ""  # Path to your private key for SSH authentication - insert the path to the private key
ssh_password = ''#insert password here

# MySQL details
mysql_host = '127.0.0.1'  # MySQL server hostname (can be localhost if running on the same server)
mysql_port = 3306  # MySQL port, usually 3306
mysql_user = 'larrymoreno'
mysql_password = ''
mysql_database = 'collinheaney'

# SSH tunneling setup
with SSHTunnelForwarder(
    (ssh_host, ssh_port),
    ssh_username=ssh_user,
    ssh_pkey=ssh_key_path,
    ssh_password=ssh_password,
    remote_bind_address=(mysql_host, mysql_port)
) as tunnel:
    # Now the local port `tunnel.local_bind_port` is forwarded to the MySQL server over SSH
    print(f'SSH Tunnel opened on local port {tunnel.local_bind_port}')
    
    # Connecting to the MySQL database through the SSH tunnel
    conn = mysql.connector.connect(
        user=mysql_user,
        password=mysql_password,
        host='127.0.0.1',  # Connect to the local end of the SSH tunnel
        port=tunnel.local_bind_port,  # Local bind port from the tunnel
        database=mysql_database
    )
    
    # Perform database operations
    cursor = conn.cursor()
    cursor.execute('use collinheaney;')
    cursor.execute('SELECT * from dept;')
    result = cursor.fetchall()
    cursor.close()

    print(result)
    
    # Close the connection
    conn.close()
