#! /usr/bin/perl -w

use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);
use Digest::SHA qw(sha256_hex);

my $cookie_data =cookie('Le_cookie') || 'No Cookie Set';
my @data_cookie=split(/\+/, $cookie_data);
my $result="";
my $key=param('key');

$dir="data/lecture/$key";
opendir(IND,$dir) || die "cant' opendir $dir";
@files=readdir(IND);
closedir IND;
#print "@files\n";

if($data_cookie[0] eq "Y"){
	$result="success"
}
else{
	$result="fail";
}

open(IN, "ko_list.txt");
while($line=<IN>){
	chomp $line;
	push @data, $line;
}
close(IN);

##############################################################
##########               HTML CODE             ###############
##############################################################
print header(-charset=>'utf8');
if($result eq "success"){
	print"<!DOCTYPE HTML>
<!--
	Editorial by HTML5 UP
	html5up.net | @ajlkn
	Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
-->

<html>
	<head>
		<title>$key</title>
		<meta charset=\"utf-8\" />
		<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, user-scalable=no\" />
		<!--[if lte IE 8]><script src=\"assets/js/ie/html5shiv.js\"></script><![endif]-->
		<link rel=\"stylesheet\" href=\"assets/css/main.css\" />
		<!--[if lte IE 9]><link rel=\"stylesheet\" href=\"assets/css/ie9.css\" /><![endif]-->
		<!--[if lte IE 8]><link rel=\"stylesheet\" href=\"assets/css/ie8.css\" /><![endif]-->
	</head>
	<body>

		<!-- Wrapper -->
			<div id=\"wrapper\">

				<!-- Main -->
					<div id=\"main\">
						<div class=\"inner\">

							<!-- Header -->
								<header id=\"header\">
									<a href=\"index.cgi\" class=\"logo\"><strong>Lecture Evaluation</strong></a>
									
								</header>

							<!-- Banner -->
								<section id=\"banner\">
									<div class=\"content\">
										<header>
											<h2>$key</h2>
										</header>
										<table>
											<tbody><tr>
												<th style=\"width:60%;\">Title</th>
												<th>Rate</th>
												<th>Writer</th>
												<th>Date</th>
											</tr>";
											foreach $f(@files){
												next if($f eq "." || $f eq"..");
												open(IN,"data/lecture/$key/$f");
												$lecture=<IN>;
												$title=<IN>;
												$professor=<IN>;
												$grade=<IN>;
												$rate=<IN>;
												$writer=<IN>;
												@text=<IN>;
												
												print"<tr>
												<td><a href=\"showData.cgi?key=$key&file=$f\">$title</td>
												<td>$rate</td>";
												if($data_cookie[1] eq "admin"){
													$file="data/user.out";
													open(IN,"$file");
													while($line=<IN>){
														@user_data=split(/\+/, $line);
														if($writer eq sha256_hex("$user_data[0]")){
															print "<td>$user_data</td>";
															last;
														}
														
													}
												}
												else{
													print "<td>anonymous</td>";
												} 
												for($i=0;$i<13;$i+=1){
													chop $f;
												}
												print"<td>$f</td>
												</tr>";
											}
										print "</tbody></table>
										<a href=\"write.cgi?key=$key\"><input type=\"button\" value=\"write\" class=\"special\" /></a>
								</section>

							<!-- Section -->
								
						<footer id=\"footer\">
									<p class=\"copyright\">&copy; Untitled. All rights reserved. Demo Images: <a href=\"https://unsplash.com\">Unsplash</a>. Design: <a href=\"https://html5up.net\">HTML5 UP</a>.</p>
								</footer>
						</div>
					</div>

				<!-- Sidebar -->
					<div id=\"sidebar\">
						<div class=\"inner\">

							<!-- Search -->
								<section id=\"search\" class=\"alt\">
									<form method=\"post\" action=\"search.cgi\">
										<input type=\"text\" name=\"query\" id=\"query\" placeholder=\"Search\" />
									</form>
								</section>

							<!-- Menu -->
								<nav id=\"menu\">
									<header class=\"major\">
										<h2>Menu</h2>
									</header>
									<ul>
										<li><a href=\"index.cgi\">@data[7]</a></li>
										<li><a href=\"list.cgi?key=feed\">Feedback</a></li>
										<li><a href=\"list.cgi?key=Introduction to Library and Information Science\">@data[8]</a></li>
										<li>
											<span class=\"opener\">@data[9]</span>
											<ul>
												<li><a href=\"list.cgi?key=History of Printing and Libraries\">@data[10]</a></li>											
												<li><a href=\"list.cgi?key=Classifying and Subject Heading of Information Materials\">@data[11]</a></li>												
												<li><a href=\"list.cgi?key=Management of Knowledge Information Centers\">@data[12]</a></li>												
												<li><a href=\"list.cgi?key=Information Systems\">@data[13]</a></li>												
												<li><a href=\"list.cgi?key=Information Technology and Human\">@data[14]</a></li>												
												<li><a href=\"list.cgi?key=Archives and Human\">@data[15]</a></li>												
											</ul>
										</li>
										<li>
											<span class=\"opener\">@data[16]</span>
											<ul>
												<li><a href=\"list.cgi?key=Cataloging of Information Materials\">@data[17]</a></li>
												<li><a href=\"list.cgi?key=Public Library Management\">@data[18]</a></li>
												<li><a href=\"list.cgi?key=Digital Libraries\">@data[19]</a></li>
												<li><a href=\"list.cgi?key=Understanding Korean Old Books\">@data[20]</a></li>
												<li><a href=\"list.cgi?key=Search Engine\">@data[21]</a></li>
												<li><a href=\"list.cgi?key=Collection Management\">@data[22]</a></li>
											</ul>
										</li>
										<li>
											<span class=\"opener\">@data[23]</span>
											<ul>
												<li><a href=\"list.cgi?key=Database Design\">@data[24]</a></li>
												<li><a href=\"list.cgi?key=Records Archiving\">@data[25]</a></li>
												<li><a href=\"list.cgi?key=School Media Center Management\">@data[26]</a></li>
												<li><a href=\"list.cgi?key=Traditional Archives Construction\">@data[27]</a></li>
												<li><a href=\"list.cgi?key=Organization of Information Materials\">@data[28]</a></li>
												<li><a href=\"list.cgi?key=Introduction to Information Services\">@data[29]</a></li>
												<li><a href=\"list.cgi?key=Database Practice\">@data[30]</a></li>
												<li><a href=\"list.cgi?key=User Interface\">@data[31]</a></li>
											</ul>
										</li>
										<li>
											<span class=\"opener\">@data[32]</span>
											<ul>
												<li><a href=\"list.cgi?key=Knowledge Information Retrieval\">@data[33]</a></li>
												<li><a href=\"list.cgi?key=Management of Serials\">@data[34]</a></li>
												<li><a href=\"list.cgi?key=Reading Guidance\">@data[35]</a></li>
												<li><a href=\"list.cgi?key=Knowledge Information Retrieval\">@data[36]</a></li>
												<li><a href=\"list.cgi?key=Theory of Information Users\">@data[37]</a></li>
												<li><a href=\"list.cgi?key=Information Sources by Subject\">@data[38]</a></li>
												<li><a href=\"list.cgi?key=Systems of Archival Management\">@data[39]</a></li>
											</ul>
										</li>
										<li>
											<span class=\"opener\">@data[40]</span>
											<ul>
												<li><a href=\"list.cgi?key=Library and Information Center Practice\">@data[41]</a></li>
												<li><a href=\"list.cgi?key=Management of Nonbook Materials\">@data[42]</a></li>
												<li><a href=\"list.cgi?key=Information Ethics in the Digital Age\">@data[43]</a></li>
											</ul>
										</li>
										<li>
											<span class=\"opener\">@data[44]</span>
											<ul>
												<li><a href=\"list.cgi?key=Traditional Archives and Cultural Contents\">@data[45]</a></li>
												<li><a href=\"list.cgi?key=Introduction to Web Programming\">@data[46]</a></li>
												<li><a href=\"list.cgi?key=Online Information Searching\">@data[47]</a></li>
											</ul>
										</li>
										<li>
											<span class=\"opener\">@data[48]</span>
											<ul>
												<li><a href=\"list.cgi?key=Discrete Mathematics\">@data[49]</a></li>
												<li><a href=\"list.cgi?key=Data Structure\">@data[50]</a></li>
												<li><a href=\"list.cgi?key=Elementary Programming\">@data[51]</a></li>
												<li><a href=\"list.cgi?key=Java Programming\">@data[52]</a></li>
												<li><a href=\"list.cgi?key=Software Design\">@data[53]</a></li>
												<li><a href=\"list.cgi?key=Operating Systems\">@data[54]</a></li>
												<li><a href=\"list.cgi?key=Artificial Intelligence\">@data[55]</a></li>
												<li><a href=\"list.cgi?key=Mobile App Programming 1\">@data[56]</a></li>
												<li><a href=\"list.cgi?key=Introduction to Computer Science and Engineering\">@data[57]</a></li>
												<li><a href=\"list.cgi?key=Advanced Web Programming\">@data[58]</a></li>
											</ul>
										</li>
										<li><a href=\"list.cgi?key=Caltural\">@data[59]</a></li>
									</ul>
								</nav>

							<!-- Section -->
								

							<!-- Section -->


						

						</div>
					</div>

			</div>

		<!-- Scripts -->
			<script src=\"assets/js/jquery.min.js\"></script>
			<script src=\"assets/js/skel.min.js\"></script>
			<script src=\"assets/js/util.js\"></script>
			<!--[if lte IE 8]><script src=\"assets/js/ie/respond.min.js\"></script><![endif]-->
			<script src=\"assets/js/main.js\"></script>

	</body>
</html>";
}
else{
	print"<meta http-equiv=\"refresh\" content=\"0;url=login.cgi\"> "
}
