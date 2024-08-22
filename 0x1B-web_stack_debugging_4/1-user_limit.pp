#this manuscript enable the user holberton to login and oprn file without error

#increase hard file limit for user holberton

exec { 'increase-hard-file-limit-for-holberton-user':
  command => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.confi',
  path    => '/usr/local/bin/:/bin/'

}

#increase soft file limit for user holberton
exec{ 'increase-soft-file-limit-for-holberton-user
 command => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf',
 path => '/usr/local/bin/:/bin/'

}