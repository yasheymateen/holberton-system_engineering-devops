# Fixes type in wp-settings.php where extension is mispelled
exec { 'fix typo':
     command => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
     path    => ['/bin/']
}
