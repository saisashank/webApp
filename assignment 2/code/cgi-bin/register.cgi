#!/usr/bin/perl -wT
use strict; 
use CGI;
use Fcntl qw(:flock);
require "/home/jiangbo/public_html/cgi-bin/ch09/validate_email_address_sub.lib";

# Clean up environment for taint mode before calling sendmail
BEGIN {
    $ENV{PATH} = "/bin:/usr/bin";
    delete @ENV{ qw( IFS CDPATH ENV BASH_ENV ) };
}

my $cgi = new CGI;
# Read in the data from HTML form
my $name = $cgi->param( "name" ); 
my $username = $cgi->param( "username" );
my $password = $cgi->param( "password" );  
my $email = $cgi->param( "email" );
my $repassword = $cgi->param( "repassword" );  
my $BirthMonth = $cgi->param( "BirthMonth" );
my $BirthDay = $cgi->param( "BirthDay" );  
my $BirthYear = $cgi->param( "BirthYear" );  
my $radio = $cgi->param( "radio" );
my $Address = $cgi->param( "Address" );  
my $phone = $cgi->param( "phone" );
my $activity = $cgi->param( "activity" );   
my $userexists = "no";	
my $salt = "21";
my $message = "Hi $name
  
Thank you for Joining our Club!!!!

Following are your Registration Details

User Name:$username
Password: $password  ";
open(PASSWDDATA, "<passwd.txt") or die "Can not open passwd.txt";

#Read in the data from the passwd.txt file
break: while(<PASSWDDATA>)
{
	my $line = $_;
	my @namepass = split(' ',$line);
	if($namepass[0] eq $username)
	{
	  $userexists = "yes";
	  last break;
	}
		  
}
close(PASSWDDATA);

if($userexists eq "yes")
{
	print $cgi->header( "text/html" ); 
	print $cgi->start_html( "" ),
	$cgi->h2(" Username already Exists. Cannot confirm membership. Please go back and try again."),
	$cgi->end_html; 
}
else
{
	if($password eq $repassword)
	{
		my $enpass = crypt($password,$salt);
		open(PASSWDDATA, ">>passwd.txt") or die "Can not open passwd.txt";

		#Read in the data from the passwd.txt file
		 print PASSWDDATA $username," ",$enpass;
		 print PASSWDDATA "\n";
		close(PASSWDDATA); 
		
unless ( $email ) {
    print $cgi->header( "text/html" ),
          $cgi->start_html( "Invalid Email Address" ),
          $cgi->h1( "Invalid Email Address" ),
          $cgi->p( "The email address you entered is invalid. " .
                 "Please use your browserÕs Back button to " .
                 "return to the form and try again." );
          $cgi->end_html;
    exit;
}

send_feedback( $email, $message );
send_receipt( $email );



sub send_feedback {
    my( $email, $message ) = @_;
    
    open MAIL, "| /usr/lib/sendmail -t -i"
        or die "Could not open sendmail: $!";
    
    print MAIL <<END_OF_MESSAGE;
#To: jiangbo\@bradley.edu
To: $email
Reply-To: $email
Subject: Web Site Feedback

Feedback from a user:

$message
END_OF_MESSAGE
    close MAIL or die "Error closing sendmail: $!";
}

sub send_receipt {
    my $email       = shift;
    #my $from_email  = shift || $ENV{SERVER_ADMIN};
    my $from_email  = shift || "manager\@www.bradley.edu";
    my $from_name   = shift || "The Manager";
 
    open MAIL, "| /usr/lib/sendmail -t -F '$from_name' -f '$from_email'"
        or die "Could not open sendmail: $!";
    print MAIL <<END_OF_MESSAGE;
To: $email
Subject: Your feedback

Your message has been sent and someone should be responding to you 
shortly. Thanks for taking the time to provide us with your feedback!
END_OF_MESSAGE
    close MAIL or die "Error closing sendmail: $!";
}




 
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
<li><a href="news.html">News</a></li>
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

<p class="title" style="padding:2px;background-color:green; width:935px;">&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Registration Details</p>

<p class="contact">
<br><br><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Name: $name <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;User Name: $username <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Password: $password <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Email: $email <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Date of Birth: $BirthMonth - $BirthDay - $BirthYear <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Gender: $radio <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Address: $Address <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Phone: $phone <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Activity: $activity <br>
</p>
</div> <!--/home-->

</div> <!--/maincontainer-->

</body>
</html>
END_OF_PAGE
 
		}
		else
		{
			print $cgi->header( "text/html" ); 
			print $cgi->start_html( "" ),
			$cgi->h2(" Password missmatch. Cannot confirm membership. Please go back and try again."),
			$cgi->end_html; 
	}  
}
