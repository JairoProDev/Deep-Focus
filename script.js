// Crear escena, cámara y renderizador
var scene = new THREE.Scene();
var camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
var renderer = new THREE.WebGLRenderer();

renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

// Crear geometría y material para la página
var geometry = new THREE.PlaneGeometry(1, 1);
var material = new THREE.MeshBasicMaterial({color: 0xffff00, side: THREE.DoubleSide});
var page = new THREE.Mesh(geometry, material);

// Añadir página a la escena
scene.add(page);

// Posicionar la cámara
camera.position.z = 5;

// Función de animación
function animate() {
    requestAnimationFrame(animate);
    renderer.render(scene, camera);
}
animate();

// Animación de volteo de página con GSAP
gsap.to(page.rotation, {y: Math.PI, duration: 1});