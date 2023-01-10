# This Puppet is  creating a file in /tmp
class filetest {
file { '/tmp/school':
  ensure  => file,
  content => 'I love Puppet',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
  }
}
