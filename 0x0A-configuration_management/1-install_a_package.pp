# This is a puppet file used to install specific packages

exec { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
