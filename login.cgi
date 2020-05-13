#! /usr/bin/perl -w

use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);
use Digest::SHA qw(sha256_hex);

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
	
	if($input_Id eq $data[0] && $input_PW eq $data[1]){
		$access="Y";
		$result="Login successful.\nWelcome $data[0]";
		
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
print"<!DOCTYPE HTML>
		<html>
		<head>
		<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, user-scalable=no\" />
		<!--[if lte IE 8]><script src=\"assets/js/ie/html5shiv.js\"></script><![endif]-->
		<link rel=\"stylesheet\" href=\"assets/css/main.css\" />
		<!--[if lte IE 9]><link rel=\"stylesheet\" href=\"assets/css/ie9.css\" /><![endif]-->
		<!--[if lte IE 8]><link rel=\"stylesheet\" href=\"assets/css/ie8.css\" /><![endif]-->
			<title>LE Login</title>
		</head>
		<body>";
		if($access ne "Y"){
			print"
				<div style=\"width:auto; height: auto; text-align: center; margin:auto;\">
					<h1>Login</h1>
					<form action=\"login.cgi\" method=\"post\">
						<table style=\"width:auto; margin:auto;\">
							<tr>
								<td><h3>Id</h3></td>
								<td><input type=\"text\" name=\"id\"></td>
							</tr>
							<tr>
								<td><h3>Password</h3></td>
								<td><input type=\"password\" name=\"pw\"></td>
							</tr>
						</table><br>
						
						<input type=\"submit\" value=\"Login\">
						<a href=\"register.htm\"><input type=\"button\" value=\"Register\"></a>
						<h2>$result</h2>
					</form>	
				</div>";
		}
		else{
			
			print"Connecting.......... <meta http-equiv=\"refresh\" content=\"0;url=index.cgi\"> "
		}
		print"
			
			<script src=\"assets/js/jquery.min.js\"></script>
			<script src=\"assets/js/skel.min.js\"></script>
			<script src=\"assets/js/util.js\"></script>
			<!--[if lte IE 8]><script src=\"assets/js/ie/respond.min.js\"></script><![endif]-->
			<script src=\"assets/js/main.js\"></script>
			
		<body>
		</html>";
