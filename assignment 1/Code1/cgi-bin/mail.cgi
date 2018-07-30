#!/usr/bin/perl -wT

use strict;
use CGI;
require "/home/jiangbo/public_html/cgi-bin/ch09/validate_email_address_sub.lib";

# Clean up environment for taint mode before calling sendmail
BEGIN {
    $ENV{PATH} = "/bin:/usr/bin";
    delete @ENV{ qw( IFS CDPATH ENV BASH_ENV ) };
}

my $q       = new CGI;
my $email   = &validate_email_address( $q->param( "email" ) );
my $message = "Hi";

unless ( $email ) {
    print $q->header( "text/html" ),
          $q->start_html( "Invalid Email Address" ),
          $q->h1( "Invalid Email Address" ),
          $q->p( "The email address you entered is invalid. " .
                 "Please use your browserÕs Back button to " .
                 "return to the form and try again." );
          $q->end_html;
    exit;
}

send_feedback( $email, $message );
send_receipt( $email );

print $q->redirect( "http://cs99.bradley.edu/~jiangbo/perl/feedback/thanks.html" );

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