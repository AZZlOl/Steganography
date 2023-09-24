<?php

// $op = shell_exec("C:\OtherPrograms\py3_11_2\python.exe script.py");
// echo $op;
?>

<!doctype html>
<html data-bs-theme="dark" lang='en-US'>
    <head>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <!-- Bootstrap CSS -->
        <!-- BS5 and JS Includes -->
        <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.min.js" integrity="sha384-fbbOQedDUMZZ5KreZpsbe1LCZPVmfTnH7ois6mU1QK+m14rQ1l2bGBq41eYeM/fS" crossorigin="anonymous"></script>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-geWF76RCwLtnZ8qwWowPQNguL3RmwHVBC9FhGdlKrxdiJJigb/j/68SIy3Te4Bkz" crossorigin="anonymous"></script>
        

        <style>
            .container {
                display: flex;
                justify-content: center;
            }
        </style>

        <title></title>
    </head>
<body>
    <div class="container mt-5">
        <div class="card" style="max-width: 260px; inline-block; margin-right: 100px;">
            <div class="card-header"><h1>Encode</h1></div>
            <div class="card-body"><img src="images/encode.png" alt="Encode Image" style='border-radius: 10px;'></div>
            <div class="card-footer text-right"><button class='btn btn-primary' onclick="window.location.href='encode.php'">Encode</button></div>
        </div>
        <div class="card" style="max-width: 260px; inline-block;">
            <div class="card-header"><h1>Decode</h1></div>
            <div class="card-body"><img src="images/decode.png" alt="Decode Image" style='border-radius: 10px;'></div>
            <div class="card-footer text-right"><button class='btn btn-primary' onclick="window.location.href='decode.php'">Decode</button></div>
        </div>
    </div>
</body>
</html>
