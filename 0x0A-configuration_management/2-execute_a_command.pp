# This is a puppet file used to install specific packages

exec { 'pkill_killmenow':
  command => 'pkill -9 killmenow',
}
