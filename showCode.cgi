#!/usr/bin/perl -w

use utf8;
use CGI qw(:standard -debug);
use CGI::Carp(fatalsToBrowser);

my $file = param('file');

print header(-type => "text/plain");

open(IN, $file);

while($line = <IN>){
	print $line;
}

close(IN);