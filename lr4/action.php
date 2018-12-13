<!doctype html>
<html>
<head>
<meta charset="utf-8">
<?php 
if ($_POST['resume']); 
$file=fopen('mes.txt','a+');


fputs($file,$_POST['fullname']."\r\n"); 

fputs($file,$_POST['adress']."\r\n");
 
fputs($file,$_POST['E-mail']."\r\n");

fputs($file,$_POST['telephone']."\r\n"); 

fputs($file,$_POST['objective']."\r\n"); 

fputs($file,$_POST['posada']."\r\n"); 

fputs($file,$_POST['company']."\r\n"); 

fputs($file,$_POST['city']."\r\n"); 

fputs($file,$_POST['month1']); 

fwrite($file, ' ');

fputs($file,$_POST['year1']); 
fwrite($file, 'р.'."\r\n");

fputs($file,$_POST['month2']); 

fwrite($file, ' ');

fputs($file,$_POST['year2']); 
fwrite($file, 'р.'."\r\n");

fputs($file,$_POST['dosjagnenja']."\r\n"); 

fputs($file,$_POST['school']."\r\n"); 

fputs($file,$_POST['cityshool']."\r\n"); 

fputs($file,$_POST['month3']); 

fwrite($file, ' ');

fputs($file,$_POST['year3']); 
fwrite($file, 'р.'."\r\n");

fputs($file,$_POST['wchene']."\r\n"); 

fputs($file,$_POST['honnors']."\r\n"); 

fputs($file,$_POST['scils']."\r\n"); 

fputs($file,$_POST['languages']."\r\n");
 
fputs($file,$_POST['interests']."\r\n"); 

fputs($file,$_POST['organisation']."\r\n"); 

fputs($file,$_POST['Ref']."\r\n"); 

fclose($file); 
echo 'Ок'; 
?>
</body>
</html>