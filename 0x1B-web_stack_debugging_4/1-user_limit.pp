# Another script

exec { 'ulimit':
  command => 'ulimit -n 4096'
}

