# Create a file in /tmp.
file { '/tmp/holberton':
  ensure   => file,
  path     => '/tmp/holberton',
  mode     => '0744',
  owner    => 'www-data',
  group    => 'I love Puppet'
}
