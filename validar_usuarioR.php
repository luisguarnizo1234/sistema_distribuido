<?php
include 'conexion.php';
$usuario=$_POST['usuarioR'];
$contrasena=$_POST['contrasenaR'];


//$usuario="Cangreburger";
//$contrasena="bochafood";

$sentencia=$conexion->prepare("SELECT * FROM userres WHERE usuario=? AND contrasena=?");
$sentencia->bind_param('ss',$usuario,$contrasena);
$sentencia->execute();

$resultado = $sentencia->get_result();
if ($fila = $resultado->fetch_assoc()) {
         echo json_encode($fila,JSON_UNESCAPED_UNICODE);     
}
$sentencia->close();
$conexion->close();
?>