# This is a puppet file used to install specific packages

package { 'install_flask':
  command => 'pip3 install Flask=2.1.0',
  unless  => '/usr/bin/pip3 show Flask',
  require => Package['python3-pip'],
}
