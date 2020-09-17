#...initialize looping variable, assume 'yes' as the first answer
$continueYN = 1;
 
while ($continueYN eq 1)
{
   #...get temperature input from the user
   print "\nEnter next temperature in degrees Farenheight (F): ";
 
   $degreeF = <STDIN>;
   chomp($degreeF);
 
   #...convert temperature from F to Celsius
   $degreeC = ($degreeF - 32) * 5 / 9;

   if ($degreeF =~ /\D/)
   {
	   print "\n[!] That is not a valid temperature.\n";
   }
   else
   {
	   print "\nTemperature in degrees C is: ".$degreeC."\n";
 	#...check for temperature below freezing..
	#...print "Temperature in degrees F is: ".$degreeF."\n";

  	 if ($degreeC < 0)
  	 {
     		 print "Pack long underwear!\n";
  	 }
 
   	#...check for it being a hot day...
  	 if ($degreeF > 100)
  	 {
     	 print "Remember to hydrate!\n";
  	 }
   }

   print "\nInput another? ";
 
   $continueYN = <STDIN>;
   chomp($continueYN);

   if($continueYN eq "y")
   {
	   $continueYN = 1;
	} else {
		$continueYN = 0;
	}
}
