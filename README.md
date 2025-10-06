# Ejercicios de Patrones de Diseño – POO
Implementaciones prácticas en Python y Java de los principales patrones de diseño vistos en Paradigmas y Lenguajes de Programación II.

---

## Estructura del proyecto
```
Ejercicios-de-Patrones-de-Dise-o-POO/
├── ejercicio1/ → Sistema de notificaciones extensible
│   ├── python/ → Observer + Strategy + Factory
│   └── java/
├── ejercicio2/ → Refactor de acceso a datos legacy
│   ├── python/ → Repository + Unit of Work + DI
│   └── java/
├── ejercicio3/ → Integración de múltiples pasarelas de pago
│   ├── python/ → Adapter + Factory + Circuit Breaker
│   └── java/
└── README.md
```

---

## Patrones aplicados

| Ejercicio | Descripción | Patrones Clave |
|------------|-------------|----------------|
| 1 | Sistema de notificaciones extensible (Email, SMS, Push) | Observer, Strategy, Factory |
| 2 | Refactor de capa de datos con separación de responsabilidades | Repository, Unit of Work, Dependency Injection |
| 3 | Integración con múltiples pasarelas de pago (Stripe, MercadoPago, Banco local) | Adapter, Factory, Circuit Breaker |

---

## Ejecución en local (Windows / Linux / VS Code)

### Python
```bash
cd ejercicio1/python
python -m notifications.demo

cd ../../ejercicio2/python
python -m data_refactor.demo

cd ../../ejercicio3/python
python -m payments.demo
```

### Java
```bash
cd ejercicio1/java
mkdir out -p
javac -d out $(find src -name "*.java")
java -cp out Main
```
(Repetir para cada módulo ejercicio2/java y ejercicio3/java)

---

## Ejecución en Google Colab

Colab no trae Java instalado por defecto, pero puede agregarse fácilmente.  
A continuación, los pasos para ejecutar Python y Java dentro de una notebook de Colab.

---

### 1. Ejecutar las versiones Python
Colab ya incluye Python 3, así que solo hay que clonar el repositorio y ejecutar los módulos:

```bash
# Clonar el repositorio
!git clone https://github.com/N3MESI2/Ejercicios-de-Patrones-de-Dise-o-POO.git
%cd Ejercicios-de-Patrones-de-Dise-o-POO
```

Luego se puede correr, por ejemplo:

```bash
# Ejercicio 1 - Notificaciones
%cd ejercicio1/python
!python -m notifications.demo

# Ejercicio 2 - Refactor de datos
%cd ../../ejercicio2/python
!python -m data_refactor.demo

# Ejercicio 3 - Pasarelas de pago
%cd ../../ejercicio3/python
!python -m payments.demo
```

---

### 2. Instalar y ejecutar las versiones Java en Colab
```bash
# Instalar Java (OpenJDK 17)
!sudo apt-get update -y
!sudo apt-get install -y openjdk-17-jdk
!java -version
!javac -version
```

Luego, por cada ejercicio:

```bash
# Clonar el repositorio si no se hizo antes
!git clone https://github.com/N3MESI2/Ejercicios-de-Patrones-de-Dise-o-POO.git
%cd Ejercicios-de-Patrones-de-Dise-o-POO/ejercicio1/java

# Crear carpeta de salida y compilar
!mkdir -p out
!find src -name "*.java" | xargs javac -d out

# Ejecutar el programa principal
!java -cp out Main
```

(Repetir el mismo bloque cambiando la ruta a ejercicio2/java y ejercicio3/java para los otros dos ejercicios.)

---

### Notas
- Python no necesita configuración adicional en Colab.  
- Java solo debe instalarse una vez por notebook.  
- Si Colab pide permisos para “apt-get”, simplemente aceptarlos.  
- Todos los ejemplos imprimen en consola simulaciones; no hacen llamadas reales a APIs.

---

## Créditos
Autor: Tomás Mieres  
Materia: Paradigmas y Lenguajes de Programación II – Universidad de la Cuenca del Plata

---

## Licencia
Uso educativo – libre para estudio y mejora.

---

## Resumen rápido de ejecución en Colab

| Tipo | Comando |
|------|----------|
| Instalar Java | `!sudo apt-get install -y openjdk-17-jdk` |
| Clonar repo | `!git clone https://github.com/N3MESI2/Ejercicios-de-Patrones-de-Dise-o-POO.git` |
| Python demo | `%cd ejercicio1/python; !python -m notifications.demo` |
| Java demo | `%cd ejercicio1/java; !find src -name "*.java" | xargs javac -d out; !java -cp out Main` |
