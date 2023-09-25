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

        <title></title>
        
    </head>
<body>
    <div class="container mt-5">
        <div class="d-flex justify-content-center">

            <div class="card" style="width: 750px; inline-block; margin-right: 100px;">
                <form action="deliver.php" method="post" enctype='multipart/form-data'>
                    <div class="card-header"><h1>Upload an Image</h1></div>
                    <div class="card-body">
                
                        <div class="input-group mb-3">
                            <input type="file" class="form-control" id="imageUpload" name="image" accept="image/*">
                            <label class="input-group-text" for="imageUpload">Choose Image</label>
                        </div>

                        <div id="imageInfo"></div>

                        <div class="input-group mb-3">
                            <input type="text" class="form-control" id="message" name="message">
                            <label class="input-group-text" for="message">Message to Encode</label>
                        </div>

                    </div>
                    <div class="card-footer text-right"><input type="submit" name='encode' value='encode' class='btn btn-primary'></div>


                </form>
            </div>

        </div>
    </div>
    <script>
        document.getElementById('imageUpload').addEventListener('change', function () {
            const fileInput = this;
            const file = fileInput.files[0];

            if (file) {
                // Display file size
                const fileSize = file.size;
                const fileSizeMB = (fileSize / (1024 * 1024)).toFixed(2); // in MB

                // Display file type
                const fileType = file.type;

                // Create an image element to get image dimensions
                const imageElement = new Image();
                imageElement.src = URL.createObjectURL(file);

                imageElement.onload = function () {
                    // Display image resolution
                    const imageWidth = this.width;
                    const imageHeight = this.height;

                    // Display the information
                    const infoContainer = document.getElementById('imageInfo');
                    infoContainer.innerHTML = `
                        <p>File Size: ${fileSizeMB} MB</p>
                        <p>File Type: ${fileType}</p>
                        <p>Resolution: ${imageWidth} x ${imageHeight}</p>
                        <p>Max encoded characters: ${ (imageWidth * imageHeight) -5}</p>
                    `;
                };
            }
        });
    </script>

    </body>
</html>
