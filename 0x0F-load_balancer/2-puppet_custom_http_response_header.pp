# Install nginx and add a new header

class nginx {
  package { 'nginx':
    ensure => 'installed'
  }

  file { '/etc/nginx/sites-available/default':
    ensure => file,
    content => "server {
	listen 80 default_server;
	listen [::]:80 default_server;

	root /usr/share/nginx/html;

	# Add index.php to the list if you are using PHP
	index index.html index.htm index.nginx-debian.html;

	server_name _;

	location / {
		try_files \$uri \$uri/ =404;
		add_header  X-Served-By $(`hostname`);
	}",
    }

  exec { 'restarting':
    command => "service nginx restart",
  }

}
