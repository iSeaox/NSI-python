<?php 
	define('HOST', 'localhost');
	define('USER', 'bestrace_handler');
	define('PASSWORD', '7g8Krc7SpSA7');
	define('DATABASE', 'bestrace');

  try {
		$db = new PDO('mysql:host='.HOST.';dbname='.DATABASE.";charset=utf8", USER, PASSWORD);
  } catch (Exception $e) {
		die("Erreur :".$e->getMessage());
  }

	if(isset($_POST['score']) and isset($_POST['name'])) {
		$prepared_insert = $db->prepare("INSERT INTO results (score, name, date_time) VALUES (?, ?, NOW())");
		$prepared_insert->execute([$_POST['score'], $_POST['name']]);
		exit();
	}

  $select = $db->query("SELECT * FROM results ORDER BY score DESC");
?>

<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>BestRace-Result</title>
		<link rel="icon" type="image/png" href="/ressources/server-icon.png" />
	</head>
	<body>
		<ul>
			<?php 
				while($data = $select->fetch()) {
					echo "<li>".$data['score']." fait le ".^$data['date_time']."</li>";
				}
			?>
		</ul>
	</body>
</html>
