# Fixes type in wp-settings.php where extension is mispelled
exec { 'mv class-wp-locale.php class-wp-locale.phpp':
  path => ['/bin'],
  cwd  => '/var/www/html/wp-includes',

  }
