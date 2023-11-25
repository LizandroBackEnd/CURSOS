<?php  
 
require "database.php"; 
 
$error = null;

  if($_SERVER["REQUEST_METHOD"] == "POST"){  
    if(empty($_POST["name"]) || empty($_POST["phone_number"])) { 
      $error = "Please fill all the fields.";
    } else if (strlen($_POST["phone_number"]) < 9 ) {  
      $error = "Phone number must be at least 9 characters.";
    } else { 
      $name = $_POST["name"];  
      $phoneNumber = $_POST["phone_number"];  
       
      $statement = $conn->prepare("INSERT INTO contacts (name, phone_number) VALUES (:name, :phone_number)");  
      $statement->bindParam(":name", $_POST["name"]); 
      $statement->bindParam(":phone_number", $_POST["phone_number"]);
      $statement->execute();
       
      header("Location: index.php");
    }
       
  }
 ?>
  
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">   
    <!-- Boostrap -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootswatch/5.3.2/darkly/bootstrap.min.css" integrity="sha512-JjQ+gz9+fc47OLooLs9SDfSSVrHu7ypfFM7Bd+r4dCePQnD/veA7P590ovnFPzldWsPwYRpOK1FnePimGNpdrA==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    <script defer src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>
    <!-- Static content -->
    <link rel="stylesheet" href="./static/css/index.css"> 
    <title>Contacts App</title>
</head>
<body> 
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container-fluid">
          <a class="navbar-brand font-weight-bold" href="#">
            <img class="mr-2" src="./static/img/logo.png" />
            ContactsApp
          </a>
          <button
            class="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarNav"
            aria-controls="navbarNav"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
              <li class="nav-item">
                <a class="nav-link" href="index.php">Home</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="add.php">Add Contact</a>
              </li>
            </ul>
          </div>
        </div>
      </nav>
    
      <main> 
        <div class="container pt-5">
          <div class="row justify-content-center">
            <div class="col-md-8">
              <div class="card">
                <div class="card-header">Add New Contact</div>
                <div class="card-body"> 
                  <?php if ($error): ?>  
                    <p class="text-danger"> 
                      <?= $error ?>
                    <?php endif  ?>
                  <form method="POST" action="add.php">
                    <div class="mb-3 row">
                      <label for="name" class="col-md-4 col-form-label text-md-end">Name</label>
        
                      <div class="col-md-6">
                        <input id="name" type="text" class="form-control" name="name"  autocomplete="name" autofocus>
                      </div>
                    </div>
        
                    <div class="mb-3 row">
                      <label for="phone_number" class="col-md-4 col-form-label text-md-end">Phone Number</label>
        
                      <div class="col-md-6">
                        <input id="phone_number" type="tel" class="form-control" name="phone_number"  autocomplete="phone_number" autofocus>
                      </div>
                    </div>
        
                    <div class="mb-3 row">
                      <div class="col-md-6 offset-md-4">
                        <button type="submit" class="btn btn-primary">Submit</button>
                      </div>
                    </div>
                  </form>
                </div>
              </div>
            </div>
          </div>
        </div>
      </main>
</body>
</html>
