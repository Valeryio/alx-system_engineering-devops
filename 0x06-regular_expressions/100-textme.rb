#!/usr/bin/env ruby
puts ARGV[0].scan(/(?<=from:)(\w*)|(?<=to:)(\+\w*)|(?<=flags:)([\D,\w]{12})/).join
