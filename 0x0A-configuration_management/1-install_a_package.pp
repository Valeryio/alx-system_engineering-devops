# This is a puppet file used to install specific packages

package { 'flask':
  command => 'pip3 install Flask=2.1.0',
  unless  => '/usr/bin/pip3 show flask',
  require => Package['python3-pip'],
}
