# Notificaciones (Java)

Compilar y ejecutar (desde `java/notifications`):
```powershell
mkdir out
javac -d out (Get-ChildItem -Recurse -Filter *.java | Select-Object -ExpandProperty FullName)
java -cp out Main
```
