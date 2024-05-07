#!/usr/bin/env ruby
# A script that accepts one arg and pass it to regex
puts ARGV[0].scan(/hbt{2,5}n/).join
