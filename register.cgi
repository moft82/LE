#! /usr/bin/perl -w

use utf8;
use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);
use Digest::SHA qw(sha256_hex);

my $inputId=param('id');
my $inputPw=param('pw');
my $inputPwCheck=param('pwcheck');
my $inputEmail=param('email');
my @data=();
my $line="";
my $file="data/user.out";
my $access="Y";
my $result="There is already same ";
my $Pw=sha256_hex("$inputPw");


open(IN,"$file") || die "can't open";
while($line=<IN>){
	@data=split(/\+/,$line);
	if($data[0] eq $inputId){
		$access="N";
		$result.="Id";
		last;
	}
	elsif($data[2] eq $inputEmail){
		$access="N";
		$result.="Email";
		last;
	}
	elsif($inputPw ne $inputPwCheck){
		$access="N";
		$result="Check the password and Confirm  password is same.";
	}
	elsif(length($inputPw)<8){
		$access="N";
		$result="Password must be longer than 8 letter";
	}
}
close(IN);
if($inputPw=~m/\+/){
	$access="N";
	$result="Sorry, you can't use \'\+\' in password.";
}

if($access eq "Y"){
	open(OUT,">>$file") ||  "can't write";
	my ($sec, $min, $hour, $mday, $mon, $year, $wday, $yday, $isdst) = localtime;
	my $now = sprintf("%04d-%02d-%02d %02d:%02d:%02d", $year + 1900, $mon + 1, $mday, $hour, $min, $sec);
	print OUT "$inputId+$Pw+$inputEmail+$now\n";
	close(OUT);
	$result="Register Successful.";
}
##############################################################
##########               HTML CODE             ###############
##############################################################

print "Content-type:text/html\r\n\r\n";
print"<!DOCTYPE HTML>
		<html>
		<head>
		<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, user-scalable=no\" />
		<!--[if lte IE 8]><script src=\"assets/js/ie/html5shiv.js\"></script><![endif]-->
		<link rel=\"stylesheet\" href=\"assets/css/main.css\" />
		<!--[if lte IE 9]><link rel=\"stylesheet\" href=\"assets/css/ie9.css\" /><![endif]-->
		<!--[if lte IE 8]><link rel=\"stylesheet\" href=\"assets/css/ie8.css\" /><![endif]-->
			<title>LE Register</title>
		</head>
		<body>";
##############################################################
##########               PERL CODE             ###############
##############################################################
		if($access eq "N"){
			print"
					<div style=\"width:100%; height: auto; text-align: center;\">
						<h1>Register</h1>
						<form action=\"register.cgi\" method=\"post\" >
							<table style=\"display: inline-block; margin:auto\">
								<tr>
									<td><h3>Id</h3></td>
									<td><input type=\"text\" name=\"id\"></td>
								</tr>
								<tr>
									<td><h3>Password</h3></td>
									<td><input type=\"password\" name=\"pw\"></td>
								</tr>
								<tr>
									<td><h3>Confirm Password</h3></td>
									<td><input type=\"password\" name=\"pwcheck\"></td>
								</tr>
								<tr>
									<td><h3>E-mail</h3></td>
									<td><input type=\"text\" name=\"email\"></td>
								</tr>
							</table><br>
							<input type=\"submit\" value=\"Register\">
							<a href=\"login.htm\"><input type=\"button\" value=\"Back\"></a>
						</form>	
					</div>"
		}
print"<div style=\"width:100%; text-align:center;\">$result<br>
<a href=\"login.cgi\"><input type=\"button\" value=\"Back\"></a></div>
			<script src=\"assets/js/jquery.min.js\"></script>
			<script src=\"assets/js/skel.min.js\"></script>
			<script src=\"assets/js/util.js\"></script>
			<!--[if lte IE 8]><script src=\"assets/js/ie/respond.min.js\"></script><![endif]-->
			<script src=\"assets/js/main.js\"></script>
		<body>
		</html>";
