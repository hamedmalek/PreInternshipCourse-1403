Write-Host "Hello World!"

$name = "Aria"
Write-Host "Hello , $name ! "

$fruits = @("Apple" , "Banana" ,  "Cherry")
Write-Host "Fruits : $($fruits -join ', ')"

$age = 20

if($age -lt 18){
    Write-Host "You are 18"
} elseif ($age -lt 60){
    Write-Host " You are old"
} else{
    Write-Host "HI"
}

for($i = 1 ; $i -le 5 ; $i++){
    Write-Host "Count , $i"
}

$count = 0
while($count -le 5){
    Write-Host "count : $count"
    $count++
}



function Say-Hello{
    param($name)
    return "Hello , $name!"
}

$name2 = Say-Hello -name "Mamad"
Write-Host = "Hello , $name2"