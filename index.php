<?php

$sessionId = $_POST["sessionId"];
$serviceCode = $_POST["serviceCode"];
$phoneNumber = $_POST["phoneNumber"];
$text = $_POST["text"];

if ($text == "") {
    $response = "CON What do you want to do? \n";
    $response .= "1. Water usage \n";
    $response .= "2. Throtle water usage \n";
    $response .= "3. "

}
else if ($text == "1") {
    $response = "END The water usage is var_from_db\n";
}
else if ($text == "2") {
    $response = "Throtle water usage feature coming soon\n";
}

header('Content-type; text/plain');
echo $response;

?>