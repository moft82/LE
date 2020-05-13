#! /usr/bin/perl -w

use strict;
use warning;

my $cookie=cookie('LE_cookie') || 'NO Cookie Set';
my @cookie=split(/\+/, $cookie);

#$cookie[0] -> access
#$cookie[1] -> Id
my $user=$cookie[1];

print"Welcome $user";
