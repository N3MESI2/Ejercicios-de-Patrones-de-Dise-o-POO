# Ejercicios Prácticos – Paradigmas y Lenguajes de Programación II

## 🧩 Estructura
Cada ejercicio contiene implementaciones en **Python** y **Java**, con patrones de diseño aplicados.

ejercicio1/ → Sistema de notificaciones extensible (Observer, Strategy, Factory)
ejercicio2/ → Refactor de acceso a datos (Repository, Unit of Work)
ejercicio3/ → Pasarelas de pago (Adapter, Factory, Circuit Breaker)


## 🚀 Cómo ejecutar

### Python
```bash
cd ejercicio1/python
python -m notifications.demo
```

### Java

```bash
cd ejercicio1/java
mkdir out -Force | Out-Null
javac -d out (Get-ChildItem -Recurse -Filter *.java | Select-Object -ExpandProperty FullName)
java -cp out Main

```
