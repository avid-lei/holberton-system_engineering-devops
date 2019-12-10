# exec a command

exec {
    command => 'pkill killmenow',
    path => '/usr/bin',
}