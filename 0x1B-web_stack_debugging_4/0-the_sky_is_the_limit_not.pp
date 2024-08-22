# Enhance Nginx server's capacity to handle more traffic

# Increase the ULIMIT in the Nginx default configuration
exec { 'adjust-nginx-ulimit':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
} ->

# Restart the Nginx service
exec { 'restart-nginx':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
