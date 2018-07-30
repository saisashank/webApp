#!/usr/bin/perl -wT
use strict; 
use CGI; 
use Fcntl qw(:flock);

my $cgi = new CGI;
# Read in the data from HTML form
my $username = $cgi->param( "username" );
my $password = $cgi->param( "password" ); 
#my $username = "cs531";
#my $password = "web"; 
my $login = "fail";
		
my $salt = "21";
my $enpass = crypt($password,$salt);
open(PASSWDDATA, "<passwd.txt") or die "Can not open passwd.txt";

#Read in the data from the passwd.txt file
break: while(<PASSWDDATA>)
{
	my $line = $_;
	my @namepass = split(' ',$line);
	if($namepass[0] eq $username && $namepass[1] eq $enpass)
	{
	  $login = "success";
	  last break;
	}
		  
}
close(PASSWDDATA);
#displayOtherHTMLPage($cgi);

if($login eq "success")
{		
	displayOtherHTMLPage($cgi);
}
else
{
	print $cgi->header( "text/html" );
	print("<meta http-equiv='refresh' content='2;url=http://cs99.bradley.edu/~sravi/Code1/login.html' />");
	print $cgi->start_html( "Welcome to XXX's Club" ),
	$cgi->h2(" Sorry! Login Failed, Automatically you will be redirected to login page"),
	$cgi->end_html;
}


# creates the Other page
sub displayOtherHTMLPage {
	use CGI qw(:standard);
	print "Content-type: text/html\n\n";
print <<END_OF_PAGE;
<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" type="text/css" href="login.css" />


<script type="text/javascript">
<!-->
var image1=new Image()
image1.src="1.jpg"
var image2=new Image()
image2.src="2.jpg"
var image3=new Image()
image3.src="3.jpg"
//-->
</script>
</head>
<body>
<div id="header-cont"> <!--header-cont-->
<div id="header"> <!--header-->
 <img class="logo" src="logo.png" alt="Club Logo" height="104" width="107">
<img class="logo1" src="logo1.png" alt="Club Logo1" height="104" width="120">
<img class="logo2" src="logo2.jpg" alt="Club Logo2" height="150" width="657">
</div> <!--/header-->

<div class="horizontal">
<ul>
<li><a href="index.html">Home</a></li>
<li><a href="#">News</a></li>
<li><a href="records.html">RECORDS</a></li>
<li><a href="login.html">Login</a></li>
<li><a href="register.html">Register</a></li>
<li><a href="rgi.html">STADIUM</a></li>
<li><a href="Selectors.html">SELECTORS</a></li>
<li><a href="about.html">About</a></li>
<li><a href="contact.html">Contact</a></li>
</ul>
</div>

</div> <!--/header-cont-->
<div id="maincontainer"> <!--/container-->

<div id="home"> <!--home-->
<br><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Welcome to the Club $username<br><br><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Upload Your Profile Pic
<FORM ACTION="/~sravi/cgi-bin/upload.cgi" METHOD="POST" ENCTYPE="multipart/form-data">
 <P>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Please choose a file to upload: 
<INPUT TYPE="FILE" NAME="file" SIZE="20" MAXLENGTH="20">

<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Please enter the name of this file: 
<INPUT TYPE="TEXT" NAME="filename" SIZE="20" MAXLENGTH="20"></p>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<INPUT TYPE="submit"></P>
</FORM>

</div> <!--/home-->

</div> <!--/maincontainer-->

</body>
</html>
END_OF_PAGE
	    
}






