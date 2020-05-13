#! /usr/bin/perl -w

use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);
use utf8;

my $cookie_data =cookie('Le_cookie') || 'No Cookie Set';
my @data_cookie=split(/\+/, $cookie_data);

my $result="";
my $input_access="Y";
my $key=param('key');
my $title=param('title');
my $professor=param('professor');
my $date=param('date');
my $rate=param('grading');
my $text=param('text');
my $writer=@data_cookie[1];

my ($sec, $min, $hour, $mday, $mon, $year, $wday, $yday, $isdst) = localtime;
my $now = sprintf("%04d-%02d-%02d-%02d-%02d-%02d", $year + 1900, $mon + 1, $mday, $hour, $min, $sec);
$outd="data/lecture/$key";
$outd2="data/total";

open(OUT1,">$outd/$now.txt") or die "can't1";
open(OUT2,">$outd2/$now.txt") or die "can't write to $outd/total/$now.txt";
print OUT1 "$key\n$title\n$professor\n$date\n$rate\n$writer\n$text";
print OUT2 "$key\n$title\n$professor\n$date\n$rate\n$writer\n$text";
close(OUT1);
close(OUT2);
open(OUT4, ">$outd2/filetest.txt");
print OUT4 "text";
close(OUT4);

if($data_cookie[0] eq "Y"){
	$result="success"
}
else{
	$result="fail";
}


##############################################################
##########               HTML CODE             ###############
##############################################################
print header(-charset=>'utf8');
if($result eq "success"){

	print"<meta http-equiv=\"refresh\" content=\"0;url=list.cgi?key=$key\">";
}
else{
	print"<meta http-equiv=\"refresh\" content=\"0;url=login.cgi\"> "
}
