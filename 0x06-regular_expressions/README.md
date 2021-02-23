<p align="center"><img src="https://github.com/facu2279/holberton-system_engineering-devops/blob/master/0x06-regular_expressions/holberton-logo.png"/></p>
# 0x06. Regular expression
# Background Context

For this project, you have to build your regular expression using Oniguruma, a regular expression library that which is used by Ruby by default. Note that other regular expression libraries sometimes have different properties.

Because the focus of this exercise is to play with regular expressions (regex), here is the Ruby code that you should use, just replace the regexp part, meaning the code in between the //:

```
facundodiaz@holberton$ cat example.rb
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
facundodiaz@holberton$
facundodiaz@holberton$ ./example.rb 127.0.0.2
127.0.0.2
facundodiaz@holberton$ ./example.rb 127.0.0.1
127.0.0.1
facundodiaz@holberton$ ./example.rb 127.0.0.a
```

# Requirements
General
----------
Allowed editors: vi, vim, emacs

All your files will be interpreted on Ubuntu 14.04 LTS

All your files should end with a new line

A README.md file, at the root of the folder of the project, is mandatory

All your Bash script files must be executable

The first line of all your Bash scripts should be exactly #!/usr/bin/env ruby

All your regex must be built for the Oniguruma library

# File Manifest:
- 0-simply_match_holberton.rb
- 
- 1-repetition_token_0.rb
- 2-repetition_token_1.rb
- 3-repetition_token_2.rb
- 4-repetition_token_3.rb
- 5-beginning_and_end.rb
- 6-phone_number.rb
- 7-OMG_WHY_ARE_YOU_SHOUTING.rb
- 100-textme.rb
- 101-passed_linkedin_regex_challenge.jpg

# Authors
Made by [Facundo Diaz](https://github.com/facu2279) to Holberton School 2021

Social Networks
-------------------
- [Linkedin](https://www.linkedin.com/in/facundo-d%C3%ADaz-720110149/)
- [Twitter](https://twitter.com/facudiazuy)