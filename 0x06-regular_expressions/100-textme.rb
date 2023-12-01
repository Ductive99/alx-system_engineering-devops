#!/usr/bin/env ruby
log_text = ARGV[0]

matched = log_text.match(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/)

puts "#{matched[1]},#{matched[2]},#{matched[3]}" if matched
