# This file is creating a manifest that kills a process named killmenow

exec { 'killmenow':
    command  => 'pkill'
    provider => 'shell'
}
