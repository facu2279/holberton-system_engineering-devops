#!/usr/bin/env ruby
# Facundo Diaz cohort 13 Holberton School 2021
puts ARGV[0].scan(/\[(?:from:|to:|flags:)(.*?)\]/).join(',')