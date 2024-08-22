# Another script

exec { 'ulimit':
  command => 'ulimit -n 4096'
  path    => '/usr/local/bin/:/bin/'
}

