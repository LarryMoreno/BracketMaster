import mysql.connector
from sshtunnel import SSHTunnelForwarder
import paramiko

# SSH details
ssh_host = 'compsci.adelphi.edu'  # The SSH server IP or hostname
ssh_port = 22  # SSH port, usually 22
ssh_user = 'collinheaney'
ssh_key_path = ""  # Path to your private key for SSH authentication - insert the path to the private key
ssh_password = ''#insert password here

# MySQL details
mysql_host = '127.0.0.1'  # MySQL server hostname (can be localhost if running on the same server)
mysql_port = 3306  # MySQL port, usually 3306
mysql_user = 'collinheaney'
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
    cursor.execute('SHOW TABLES;')
    result = cursor.fetchone()

    # If no database is selected, print a message.
    if result[0] is None:
        print("Connected, but no database selected.")
    else:
        print(f"Connected to database: {result[0]}")
    
    # Close the connection
    cursor.close()
    conn.close()
