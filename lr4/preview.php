<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Резюме</title>
<script src="jquery-2.1.3.min.js"></script>
<link href="style2.css" rel="stylesheet" type="text/css">
</head>

<body>
<pre id = "content">
<?php
$content = file('mes.txt');
foreach ($content as $string) {
    echo $string;
}
?>
</pre>
<input type="button" onclick="downloadInnerHtml('resume.doc', 'content');" value = "Зберегти в Word">
<script type="text/javascript" src="script/language.js" ></script>
</body>
</html>
