# This script is Fixing the nginx requests limit
exec { 'fix nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/bin/'
}

# Restart Nginx
exec { 'restart':
  command => 'service nginx restart',
  path    => '/usr/bin/'
}
