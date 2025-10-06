# Refactor de Datos (Java)

Desde `java/data_refactor`:
```powershell
mkdir out
javac -d out (Get-ChildItem -Recurse -Filter *.java | Select-Object -ExpandProperty FullName)
java -cp out Main
```
