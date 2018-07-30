#!/usr/bin/perl -wT
use strict; 
use CGI;
use Fcntl qw(:flock);

my $cgi = new CGI;
# Read in the data from HTML form
my $userid = $cgi->param( "UserId" ); 
my $dateofbirth = $cgi->param( "DateofBirth" );
my $age = $cgi->param( "age" );



my $userexists = "no";	

 if($age < 21)
{
		use CGI qw(:standard);
	print "Content-type: text/html\n\n";
print <<END_OF_PAGE;
<!DOCTYPE html>
<html>
<head>
<style type="text/css">
	
body{
margin:0px;
background-color:silver;
}

#main{
position:absolute;
background-color:silver;

width:100%;
height:100%
}

#header{
background-color:orange;
width:100%;
margin:0px;
height:70px;

}

#crypt{

position:relative;
top:50px;

}
.head{
position:relative;
top:20px;
font-size:20px;
}

</style>
</head>
<body>
<div id="header">
<label class="head"><center>Registration</center></label>
</div>
<div id="main">
<center>
<div id="crypt">
Your date of birth is:$dateofbirth <br>
Your userid is:$userid <br>
"You cannot drink alcohol"
</div>
</center>
</div>
</body>
</html>
END_OF_PAGE
}

if($age >= 21)
{
		use CGI qw(:standard);
	print "Content-type: text/html\n\n";
print <<END_OF_PAGE;
<!DOCTYPE html>
<html>
<head>
<style type="text/css">
	
body{
margin:0px;
background-color:silver;
}

#main{
position:absolute;
background-color:silver;

width:100%;
height:100%
}

#header{
background-color:orange;
width:100%;
margin:0px;
height:70px;

}

#crypt{

position:relative;
top:50px;

}

.head{
position:relative;
top:20px;
font-size:20px;
}
</style>
</head>
<body>
<div id="header">
<label class="head"><center>Registration</center></label>
</div>
<div id="main">
<center>
<div id="crypt">
Your date of birth is:$dateofbirth <br>
Your userid is:$userid <br>
"You can drink alcohol"
</div>
</center>
</div>
</body>
</html>
END_OF_PAGE
}
