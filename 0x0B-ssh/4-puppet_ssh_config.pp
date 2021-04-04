# Made by Facundo Diaz to Holberton School 2021
file_line { 'change private key':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/holberton',
  match  => 'IdentityFile ~/.ssh/id_rsa',
}
file_line { 'no password':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  match  => 'PasswordAuthentication yes',
  line   => 'PasswordAuthentication no',
}