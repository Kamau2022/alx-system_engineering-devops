# This file is creating a manifest that kills a process named killmenow

exec { 'killmenow':
    command     => 'pkill',
    path        => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
    subscribe   => File['/root/Backup/deploy'],
    refreshonly => true,
}
