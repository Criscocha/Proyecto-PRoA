var modal = document.getElementById("myModal");
var modalImg = document.getElementById("imgAmpliada");
var captionText = document.getElementById("caption");

// Seleccionar todas las imágenes con la clase "myImg"
var imgs = document.querySelectorAll(".myImg");

// Agregar un evento de clic a cada imagen
imgs.forEach(function(img) {
    img.onclick = function() {
        modal.style.display = "block";
        modalImg.src = this.src;
        captionText.innerHTML = this.alt;
    }
});

// Cerrar el modal al hacer clic en la "X"
var span = document.getElementsByClassName("close")[0];
span.onclick = function() { 
    modal.style.display = "none";
}

// Cerrar el modal al hacer clic fuera de la imagen ampliada
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
