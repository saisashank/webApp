<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" type="text/css" href="style.css" />
<link href="template1/tabcontent.css" rel="stylesheet" type="text/css" />

<script src="tabcontent.js" type="text/javascript"></script>
 
<script type="text/javascript">
<!-->
var image1=new Image()
image1.src="1.jpg"
var image2=new Image()
image2.src="Red Wine.jpg"
var image3=new Image()
image3.src="cheers.jpg"
//-->
</script>
<style type="text/css">
	.gradienttable{
		width:100%; 
		border-collapse:collapse; 
	}
	.gradienttable td{ 
		padding:7px; border:#4e95f4 1px solid;
	}
	/* provide some minimal visual accomodation for IE8 and below */
	.gradienttable tr{
		background: #b8d1f3;
	}
	/*  Define the background color for all the ODD background rows  */
	.gradienttable tr:nth-child(odd){ 
		background: #b8d1f3;
	}
	/*  Define the background color for all the EVEN background rows  */
	.gradienttable tr:nth-child(even){
		background: #dae5f4;
	}
</style>


</head>
<body>
<div id="maincontainer"> <!--/container-->

<div id="header-cont"> <!--header-cont-->

<div id="header"> <!--header-->
 <img class="logo" src="l.png" alt="Club Logo" height="104" width="107">
<img class="logo1" src="s.png" alt="Club Logo1" height="64" width="160">
<div id="slideshow">
<img src="1.jpg" name="slide" width="679" height="200">
<script type="text/javascript">
<!--
var step=1
function slideit(){
document.images.slide.src=eval("image"+step+".src")
if(step<3)
step++
else
step=1
setTimeout("slideit()",2500)
}
slideit()
//-->
</script>
</div>  
</div> <!--/header-->


</div> <!--/header-cont-->


<div id="home"> <!--home-->
<center>
   
   <div style="width: 900px; margin: 0 auto; padding: 120px 0 40px;">
        <ul class="tabs" data-persist="true">
            <li><a href="#view1">Select</a></li>
            <li><a href="#view2">Insert</a></li>
            <li><a href="#view3">Update</a></li>
            <li><a href="#view4">Delete</a></li>
        </ul>
        <div class="tabcontents">
            <div id="view1">
			
	               <form name="select" method="post" action="wineselect.php">
						<table cellspacing="20" cellpadding="20">
		 				<tr class="spaceUnder"><td>Wine Type  :</td>
							<td><select name="wineType">
							<option value="All">All</option>
							<option value="2">Sparkling</option>
							<option value="3">Fortified</option>
							<option value="4">Sweet</option>
							<option value="5">White</option>
							<option value="6">Red</option>
							</select></td></tr>
						<tr class="spaceUnder"><td>Region  : </td>
							<td><select name="regionName">
							<option value="All">All</option>
							<option value="Barossa Valley">Barossa Valley</option>
							<option value="Coonawarra">Coonawarra</option>
							<option value="Goulburn Valley">Goulburn Valley</option>
							<option value="Lower Hunter Valley">Lower Hunter Valley</option>
							<option value="Margaret River">Margaret River</option>
							<option value="Riverland">Riverland</option>
							<option value="Rutherglen">Rutherglen</option>
							<option value="Swan Valley">Swan Valley</option>
							<option value="Upper Hunter Valley">Upper Hunter Valley</option>
							</select></td></tr>
						 <tr class="spaceUnder"><td>Price Range  :</td>
							<td><input type="text" name="price1" size="5"/>
						<strong>-</strong>		
						<input type="text" name="price2" size="5"/>
						</td></tr> 
						<tr class="spaceUnder"><td>Year  :</td>
						
						<td><select name="year">
							<option value="All">All</option>
							<option value='1970'>1970</option>
							<option value='1971'>1971</option>
							<option value='1972'>1972</option>
							<option value='1973'>1973</option>
							<option value='1974'>1974</option>
							<option value='1975'>1975</option>
							<option value='1976'>1976</option>
							<option value='1977'>1977</option>
							<option value='1978'>1978</option>
							<option value='1979'>1979</option>
							<option value='1980'>1980</option>
							<option value='1981'>1981</option>
							<option value='1982'>1982</option>
							<option value='1983'>1983</option>
							<option value='1984'>1984</option>
							<option value='1985'>1985</option>
							<option value='1986'>1986</option>
							<option value='1987'>1987</option>
							<option value='1988'>1988</option>
							<option value='1989'>1989</option>
							<option value='1990'>1990</option>
							<option value='1991'>1991</option>
							<option value='1992'>1992</option>
							<option value='1993'>1993</option>
							<option value='1994'>1994</option>
							<option value='1995'>1995</option>
							<option value='1996'>1996</option>
							<option value='1997'>1997</option>
							<option value='1998'>1998</option>
							<option value='1999'>1999</option>

							</select></td></tr>
	 	 				<tr class="spaceUnder"><td></td><td><input type="submit" value="Show wines"></td></tr>
						</table>
						 
			  </form> 
            </div>
            <div id="view2">
               <form method="post" action="wineinsert.php">
					<table> 
					<tr class="spaceUnder"><td>Wine Id  :</td><td><input type="text" name="wine_id" size="25"/></td></tr>
						<tr class="spaceUnder"><td>Wine Name :</td><td><input type="text" name="wine_name" size="25"/></td></tr>
						<tr class="spaceUnder"><td>Wine Type:</td><td><select name="wine_type">
						<option value="All">All</option>
							<option value="2">Sparkling</option>
							<option value="3">Fortified</option>
							<option value="4">Sweet</option>
							<option value="5">White</option>
							<option value="6">Red</option>
						</select></td>
						</tr>
						

						<tr class="spaceUnder"><td>Year :</td>
						<td><input type="text" name="year"size="25"/></td>
						</tr>
						<tr  class="spaceUnder"><td>Price :</td><td><input type="text" name="price" size="25"></td></tr>
						<tr  class="spaceUnder"><td>On hand count : </td><td><input type="text" name="on_hand"size="25"/></td></tr>
						<tr  class="spaceUnder"><td>Winery Id : </td><td><input type="text" name="winery_id"size="25"/></td></tr>
						<tr  class="spaceUnder"><td>Winery Name :</td><td><input type="text" name="winery_name" size="25"/></td></tr>
						<tr  class="spaceUnder"><td>Region Id :</td><td><select name="region_id"><option value="7">Barossa Valley</option><option value="4">Coonawarra</option>
									<option value="2">Goulburn Valley</option><option value="6">Lower Hunter Valley</option><option value="9">Margaret River</option>
									<option value="8">Riverland</option><option value="3">Rutherglen</option><option value="10">Swan Valley</option>
									<option value="5">Upper Hunter Valley</option></select></td></tr>

						<tr class="spaceUnder"><td></td><td><input id="Submit" type="submit" value="Insert Records" /></td></tr>
						</table>
						 
			  </form>
            
            </div>
            <div id="view3">
               <form method="post" action="wineupdate.php">
					<table>
						<tr class="spaceUnder"><td>Wine ID : <td><input type="text" name="wine_id" size=25></tr>
						<tr class="spaceUnder"><td>Winery ID :<td><input type="text" name="winery_id" size=25></tr>
						<tr class="spaceUnder"><td>Wine Name : <td><input type="text" name="wine_name" size=25></tr>
    					<tr class="spaceUnder"><td>Winery name :<td><input type="text" name="winery_name" size=25></tr>
						<tr class="spaceUnder"><td>Wine Price :<td><input type="text" name="price" size=25></tr>
						<tr class="spaceUnder"><td></td><td><br><input type="submit" value="Update Records"></td>
					</table>
						 
				</form>
            </div>
			<div id="view4">
                
				<form method="post" action="winedelete.php">
					<table>
					<tr class="spaceUnder">
  						<td>Wine ID:
  						<td><input type="text" name="wine_id" size=25>
					</tr>
					<tr class="spaceUnder">
 						<td>Winery ID:
  						<td><input type="text" name="winery_id" size=25>
					</tr>
					<tr><td></td><td><br><input type="submit" value="Delete Records"></td>

<?php    
						require 'db.inc';
								
						 try
					 {
					   
					  if (!($connection = @ mysql_connect($dbhost, $dbuser, $dbpass)))
					  throw new Exception('Could not connect to database:'.mysql_error());
					 }
					 catch(Exception $e)
					 {
						 echo 'Caught Exception: ',  $e->getMessage(), "\n";
					 }
					if (!mysql_select_db($select_db, $connection))
					die('cant use' . databaseName.':'.mysql_error());
					

					 $wine_id = $_POST['wine_id'];
					 $winery_id = $_POST['winery_id'];


						$query = "DELETE from wine Where wine_id= {$wine_id} ";
						$query1= "DELETE from winery Where winery_id= {$winery_id} ";
						$query2 = "DELETE from inventory Where wine_id= {$wine_id} ";
					   $rs1=mysql_query($query,$connection);
					   $rs2=mysql_query($query1,$connection);   	  
					   $rs2=mysql_query($query2,$connection);   	  
					   
						  if (!(@ mysql_query ($query, $connection)))   showerror();
							mysql_close($connection);
							{
								print "<br><br><p>Successfully deleted Wine with ID - $wine_id</p>";
							}
							
							function showerror()   {
						die("Error " . mysql_errno() . " : " . mysql_error());   }

								 ?>
					</table>











				</form>
   				
            </div>
      </div>
        <p>&nbsp;</p>
        <p>&nbsp;</p>
        <p>&nbsp;</p>
     </div>

</center>



</div> <!--/home-->

</div> <!--/maincontainer-->

</body>
</html>