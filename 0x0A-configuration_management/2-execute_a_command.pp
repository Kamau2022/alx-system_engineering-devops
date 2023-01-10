# This file is creating a manifest that kills a process named killmenow

exec { 'killmenow':
    command => 'pkill $(pgrep killmenow)',
    path    => '/bin/',
}
