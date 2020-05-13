#! /usr/bin/perl -w

use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);

my $cookie_data =cookie('Le_cookie') || 'No Cookie Set';
my @data_cookie=split(/\+/, $cookie_data);
my $result="";
my $key=param('key');

if($key eq "Caltural"){
	$write_title="교양강의인 경우 강의 명을 입력해주세요";
}
else{
	$write_title="title";
}
 
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
	print"<!doctype html>
<!--
	Editorial by HTML5 UP
	html5up.net | 
	Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
-->
<html><head>
		<title>Write-$key</title>
		<meta charset=\"utf-8\">
		<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, user-scalable=no\">
		<!--[if lte IE 8]><script src=\"assets/js/ie/html5shiv.js\"></script><![endif]-->
		<link rel=\"stylesheet\" href=\"assets/css/main.css\">
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
									<a href=\"index.cgi\" class=\"logo\"><strong>강의평가</strong></a>
									
								</header>

							<!-- Banner -->
								<section id=\"banner\">
												    <form action=\"upload.cgi\" method=\"post\" style=\"width:100%;\">
												    <div style=\"margin-bottom:1%;\">
												    	<input type=\"text\" name=\"title\" placeholder=\"$write_title\" required>
												    </div>
												    <div style=\"width:33%; margin-bottom:1%; display:inline-block;\">
												    <input type=\"text\" name=\"professor\" placeholder=\"Professor\" required>
												    </div>
												    <div style=\"width:33%; margin-bottom:1%; display:inline-block;\"> 
												    <select name=\"grading\" id=\"demo-category\" required>
															<option disabled=\"disabled\">- Grading -</option>
															<option value=\"A\">A</option>
															<option value=\"B\">B</option>
															<option value=\"C\">C</option>
															<option value=\"D\">D</option>
															<option value=\"F\">F</option>
														</select>
														</div>
														<div style=\"width:33%; margin-bottom:1%; display:inline-block;\"> 
														    <select name=\"date\" required>
															<option disabled=\"disabled\">- 수강시기 -</option>
															<option value=\"2011\">2011년</option>
													        <option value=\"2012\">2012년</option>
													        <option value=\"2013\">2013년</option>
															<option value=\"2014\">2014년</option>
															<option value=\"2015\">2015년</option>
															<option value=\"2016\">2016년</option>
															<option value=\"2017\">2017년</option>
														</select>
														</div>
														<textarea name=\"text\" rows=\"20\" placeholder=\"Type in\" required></textarea>
														<input type=\"submit\" value=\"Submit\">
														<input type=\"hidden\" value=\"$key\" name=\"key\">
    
													    </form></section>

							<!-- Section -->
								
						<footer id=\"footer\">
									<p class=\"copyright\"> Untitled. All rights reserved. Demo Images: <a href=\"https://unsplash.com\">Unsplash</a>. Design: <a href=\"https://html5up.net\">HTML5 UP</a>.</p>
						</footer>
						</div>
					</div>

				<!-- Sidebar -->
					<div id=\"sidebar\">
						<div class=\"inner\">
    <a href=\"#sidebar\" class=\"toggle\">Toggle</a>

							<!-- Search -->
								<section id=\"search\" class=\"alt\">
									<form method=\"post\" action=\"search.cgi\">
										<input type=\"text\" name=\"query\" id=\"query\" placeholder=\"Search\">
									</form>
								</section>

							<!-- Menu -->
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
