<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>Search a wine</title>


<style type="text/css">
	.gradienttable{
		width:80%; 
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

.wine{
position:relative;
right:40px;

}
.text{
position:relative;
left:80px;
top:15px;
}
.prev{
position:relative;
left:40px;


}
.select{
position:relative;
left:40px;


}

.cost{
position:relative;
left:40px;


}

.search{
position:relative;
top:60px;
right:90px;

}

.tip{
position:relative;
top:160px;


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
<label class="head"><center>Wine Search</center></label>
</div>
<center>
<div id="main">
<form name="search" method="post" >
<br><br>



<table cellspacing="20" cellpadding="20">

<tr class="spaceUnder"><td>Wine Price:</td>
						<td><input type="text" name="wineprice" size="5"/>
						</td></tr> 
						
<tr class="spaceUnder"><td>Wine Year:</td>
							<td><select name="wineyear">
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
							<option value='2000'>2000</option>
							<option value='2000'>2001</option>
							<option value='2000'>2002</option>
							<option value='2000'>2003</option>
							<option value='2000'>2004</option>
							<option value='2000'>2005</option>
							<option value='2000'>2006</option>
							<option value='2000'>2007</option>
							<option value='2000'>2008</option>
							<option value='2000'>2009</option>
							<option value='2000'>2010</option>
							<option value='2000'>2011</option>
							<option value='2000'>2012</option>

							</select></td></tr>
						<tr class="spaceUnder"><td></td><td><input type="submit" class="search" name="submit" value="submit" /></td></tr>	
							


</table>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


</form>

<?php
			
$dbhostname = 'localhost';
 
$dbusername = 's_sravi';
 
$dbpassword = 'TDJXeVfB';

$db="s_sravi";
 
 mysql_connect($dbhostname, $dbusername, $dbpassword) or die("Sorry, can't connect to the mysql.");

 mysql_select_db($db) or die("Sorry, can't select the database.");

            

            if(isset($_POST['submit']))
            {
            $wine_price =$_POST['wineprice'];
			$wine_year =$_POST['wineyear'];
?>
<br><br><br><br><br>          
<center>
<center><label>Query Results</label></center>
            <table class="gradienttable">
            <tr>
            <th><p>WINE ID</p></th><th><p>WINE NAME</p></th><th><p>WINE TYPE</p></th><th><p>YEAR</p></th><th><p>WINERY ID</p></th><th><p>DESCRIPTION</p></th><th><th><p>PRICE</p></th><th>
            </tr>
<?php
           
 $query = "SELECT w.wine_id,w.wine_name,w.wine_type,w.year,w.winery_id,w.description,i.price
			from wine as w join items as i on i.wine_id = w.wine_id
			where i.price < $wine_price and w.year= $wine_year ";
							/*if (isset($region) && $region != "All")
							{
							 $query .= " AND region_name = \"{$region}\""; 
							 
							}
							   if (isset($wine_type) && $wine_ype != "All")
							   {
								$query .= " AND wine_type = \"{$wine_type}\""; 
															   }
						 if (isset($cost))
							 $query .= " AND cost >= \"{$cost}\"";
						  $query .= " ORDER BY wine_id";*/

$queries=mysql_query($query);

            while($result = mysql_fetch_array( $queries ))
            {
				?>       
           <tr>
           
           <td><?php echo $result['wine_id']; ?></td>
           <td><?php echo $result['wine_name'];?> </td>
           <td><?php echo $result['wine_type'];?> </td> 
           <td><?php echo $result['year'];?> </td>
           <td><?php echo $result['winery_id'];?> </td>
           <td><?php echo $result['description'];?> </td>
		   <td><?php echo $result['price'];?> </td>
		   </td>

            </tr>
<?php
            }
			
			$anymatches = mysql_num_rows($queries);
            if ($anymatches == 0)
            {
            echo "Not found<br><br>";
            }
			
			}
?>					  
</table>
</center>
</div>
<center>
</body>
</html>