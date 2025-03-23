<?php
for ($i = 1; $i <= 100; $i++) {
    $out = "";
    $a = false;
    if ($i % 3 == 0) {
        $out .= "Fizz";
        $a = true;
    }
    if ($i % 5 == 0) {
        $out .= "Buzz";
        $a = true;
    }
    if ($a) {
        $out .= "!";
    } else {
        $out = $i;
    }
    $out .= "\n";
    echo $out;
}
?>