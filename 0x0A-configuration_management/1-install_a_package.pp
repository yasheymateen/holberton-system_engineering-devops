# Install puppet-lint using puppet manifest

package { 'puppet-lint':
    ensure   => '2.1.1',
    provider => 'gem',
}
