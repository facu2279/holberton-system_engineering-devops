# Made by Facundo Diaz for Holberton School 2021

exec { 'pkill':
  command  => 'pkill -f killmenow',
  provider => 'shell',
}