<?php

if (isset($_POST['encode'])) {
    $message = $_POST['message'];
    $uploadDir = 'uploaded_images/'; // Directory to save the uploaded image

    // Check if the directory exists; if not, create it
    if (!file_exists($uploadDir)) {
        mkdir($uploadDir, 0777, true);
    }

    $fileName = str_replace(" ","",$_FILES['image']['name']);
    echo "Modified Image Name (removed whitespace): ".$fileName."<br>";
    $fileExtension = pathinfo($fileName, PATHINFO_EXTENSION); // Get the file extension

    $uploadFile = $uploadDir . $fileName;

    if (move_uploaded_file($_FILES['image']['tmp_name'], $uploadFile)) {
        // Image uploaded successfully
        $date = date_create();
        $output_file_name = date_timestamp_get($date);
        $output_file_name = $output_file_name . '.' . $fileExtension;
        
        // Sanitize user input (message) and escape it for shell execution
        $sanitizedMessage = escapeshellarg($message);

        // Define the full path to the Python executable
        $pythonExecutable = 'C:\OtherPrograms\py3_11_2\python.exe';
        // $file_location = realpath("uploaded_images/{$fileName}");
        $file_location = "uploaded_images/{$fileName}";

        // Construct the shell command
        $command = "$pythonExecutable steganography.py e $file_location --output_file_name $output_file_name --msg $sanitizedMessage 2>&1";
        
        "<br>";
        // Execute the shell command and capture the output
        // $output = shell_exec($command);
        system($command, $output);

        // Output the result
        // echo "$output";
    } else {
        echo "<h1>Error..!</h1>";
    }
}
elseif(isset($_POST['decode'])) {
    $uploadDir = 'uploaded_images/'; // Directory to save the uploaded image

    // Check if the directory exists; if not, create it
    if (!file_exists($uploadDir)) {
        mkdir($uploadDir, 0777, true);
    }

    $fileName = str_replace(" ","",$_FILES['image']['name']);
    echo "Modified Image Name (removed whitespace): ".$fileName."<br>";
    $fileExtension = pathinfo($fileName, PATHINFO_EXTENSION); // Get the file extension

    $uploadFile = $uploadDir . $fileName;

    if (move_uploaded_file($_FILES['image']['tmp_name'], $uploadFile)) {
        // Image uploaded successfully
        $date = date_create();
        $output_file_name = date_timestamp_get($date);
        $output_file_name = $output_file_name . '.' . $fileExtension;

        // Define the full path to the Python executable
        $pythonExecutable = 'C:\OtherPrograms\py3_11_2\python.exe';
        // $file_location = realpath("uploaded_images/{$fileName}");
        $file_location = "uploaded_images/{$fileName}";

        // Construct the shell command
        $command = "$pythonExecutable steganography.py d $file_location 2>&1";
        
        "<br>";
        // Execute the shell command and capture the output
        // $output = shell_exec($command);
        system($command, $output);

        // Output the result
        // echo "$output";
    } else {
        echo "<h1>Error..!</h1>";
    }
}
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

        <title></title>

    </head>
<body>

    <div class="container h-100">
    <div class="row h-100 justify-content-center align-items-center">
        <?php 
            if(isset($_POST['encode'])){
                ?>
                    <div class="col-md-6">
                        <img class="text-center" src="encoded_images\<?php echo $output_file_name; ?>" alt="Encoded Image" style='width: 800px;'>
                        <a href="encoded_images\<?php echo $output_file_name; ?>">Click here to download the Encoded Image.</a>
                    </div>
                <?php
            }
            elseif(isset($_POST['decode'])){
                ?>
                    <div class="col-md-6">
                        <br>
                        <br>
                        <br>
                        <!-- <p>Encoded Message: <?php echo $output; ?></p> -->
                    </div>
                <?php
            }
        ?>
    </div>
    </div>

</body>
</html>
