# Increase the resource limit for file requests
exec { 'limit':
  command => "sed -i -e 's/15/4096/g' /etc/default/nginx; service nginx restart",
  path    => ['/bin', '/usr/bin', '/usr/sbin']
}
