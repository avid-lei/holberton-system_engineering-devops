# exec a command

exec { 'kill'
    command => 'pkill killmenow',
    path => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games',
}