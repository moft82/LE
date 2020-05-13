#! /usr/bin/perl -w

use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);
use Digest::SHA qw(sha256_hex);
print header(-charset=>'utf8');
####################################################################
##############    Variables Declare              ###################
####################################################################
my $cgi = CGI->new;
my $input_Id=param('id');
my $input_PW=param('pw');
my @data=();
my $file="data/user.out";
my $line="";
my $access="N";
my $result="";
my $cgi = CGI->new;
$input_PW=sha256_hex("$input_PW");
######################################################################
################           Login Check          ######################
######################################################################
open(IN,"$file");
while($line=<IN>){
	@data=split(/\+/,$line);
	print"$input_Id  $input_PW<br>";
	print"$data[0] $data[1]<br>";
	if($input_Id eq $data[0] && $input_PW eq $data[1]){
		$access="Y";
		last;
	}
	elsif($input_Id ne $data[0]){
		$access="N";
		$result="Login denied. Please check your Id";
		
	}
	elsif($input_PW ne $data[1]){
		$access="N";
		$result="Login denied. Please check your Password";	
	}
}
close(IN);


######################################################
##########          Cookie  Set           ############
######################################################
my $cookie = $cgi->cookie(
		 -name  => 'Le_cookie',
		 -value => "$access+$data[0]",
		 -expire=> '+1h'
);
print $cgi->header( -cookie => $cookie );
my $cookie_data = $cgi->cookie('Le_cookie') || 'No Cookie Set';

######################################################################
################              HTML CODE         ######################
######################################################################
print"$result"