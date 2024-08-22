# Another script

exec { 'ulimit-hard':
  command => "sed -i '/^holberton hard/s/5/5000' /etc/security/limits.conf",
  path    => '/usr/local/bin/:/bin/'
}

exec { 'ulimit-soft':
  command => "sed -i '/^holberton soft/s/5/5000' /etc/security/limits.conf",
  path    => '/usr/local/bin/:/bin/'
}
