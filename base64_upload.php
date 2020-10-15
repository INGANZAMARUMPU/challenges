<?php 
if(isset($_POST)){
  $nom_fichier = $_POST["nom_fichier"];
  $fichier64 = $_POST["fichier"];
	try{
		$decoded_fichier = base64_decode(explode(',', $fichier64)[1]);
		$fichier = "./uploads/$nom_fichier";

		$image = fopen($fichier, "wb");
		fwrite($image, $decoded_fichier);
		fclose($image);
		echo "image reçu avec succes";
		echo "<img src='$fichier'/>";
	} catch(Exception $e){
    echo $e->getMessage();
  }
}
?>

<!DOCTYPE html>
<html>
<body>
  <!-- <form action="base64_upload.php" method="post" enctype="multipart/form-data"> -->
  <form action="#" method="post" enctype="multipart/form-data">
    Select image to upload:
    <input type="file" name="fileToUpload" id="fileToUpload">
    <input type="submit" value="Upload Image" name="submit">
  </form>
  <script>
  	var form = document.getElementsByTagName("form")[0];
  	form.addEventListener("submit", function(event) {
  		event.preventDefault();
  		var dom_file = document.getElementById("fileToUpload");
  		if (dom_file.files.length>0){
    		var file = dom_file.files[0];
    		var name = file.name;
        var reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onload = function () {
          postToUrl(name, reader.result);
        };
        reader.onerror = function (error) {
          console.log('Error: ', error);
        };
      }
  	}, true);
    function postToUrl(name, base64) {
      var form = document.createElement("form");
      form.setAttribute("method", "post");
      form.setAttribute("action", "");
      form.setAttribute("enctype", "multipart/form-data");

      var nom_fichier = document.createElement("input");
      nom_fichier.setAttribute("type", "hidden");
      nom_fichier.setAttribute("name", "nom_fichier");
      nom_fichier.setAttribute("value", name);
      form.appendChild(nom_fichier);

      var fichier64 = document.createElement("input");
      fichier64.setAttribute("type", "hidden");
      fichier64.setAttribute("name", "fichier");
      fichier64.setAttribute("value", base64);

      form.appendChild(fichier64);
      document.body.appendChild(form);
      form.submit();
  }
  </script>
</body>
</html>
