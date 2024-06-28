# This is a puppet file used to install specific packages
# Variables pour les chemins
$python3_cmd = '/usr/bin/python3'
$pip3_cmd = '/usr/bin/pip3'

# Installation de Python 3
package { 'python3':
  ensure => installed,
}

# Installation de pip pour Python 3
package { 'python3-pip':
  ensure   => installed,
  provider => 'apt',
  require  => Package['python3'],
}

package { 'install_flask':
  command => 'pip3 install Flask=2.1.0',
  unless  => '/usr/bin/pip3 show flask',
  require => Package['python3-pip'],
}
