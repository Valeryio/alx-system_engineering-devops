# Code

# file { '/etc/default/nginx':
#   ensure  => 'present',
#  content => 'ULIMIT="n -4096"'
# }

exec { 'nginx-fail-fixing':
  command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:bin/',
}

exec { 'restart-the-engine':
  command => '/etc/init.d/nginx restart',
  path    => '/etc/init.d/',
}
