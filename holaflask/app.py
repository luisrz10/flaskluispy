
from flask import Flask, request, render_template
from flask_cors import CORS
app=Flask(__name__)
CORS(app)

@app.route("/")
def hola():
    return "<h1>¡Hola flask!</h1> <hr>"


## Haga un programa que calcule el promedio de notas sabiendo que tienen un valor de 30%,
## 30% y 40% respectivamente.
@app.route("/notas")
@app.route("/notas/<float:nota1>/<float:nota2>/<float:nota3>")
def notas(nota1=0,nota2=0,nota3=0):
    resultado=(nota1*30)/100+(nota2*30)/100+(nota3*40)/100
    return f"<h1>El resultado es: {resultado}</h1> <hr>"

## 2.) Un programa que al capturar la edad de una persona diga si es:
##  Menor de edad (Menor a 18 años)
##  Adulto (Mayor o igual a 18 años y menor a 60 años)
##  Adulto mayor (Mayor o igual a 60 años)
@app.route("/edades")
@app.route("/edades/<int:edad>")
def edades(edad=0):
    if edad<18:
        R="menor de edad"
    elif(edad<60):
        R="Adulto"
    else:
        R="Adulto mayor"    
    return f"<h1> La persona es: {R}</h1> <hr>"


## Realizar un algoritmo con funciones que en la primera opción cargue e imprima vectores,
## en la segunda opción cargue e imprima matrices
import numpy as np
@app.route("/arreglos")
@app.route("/arreglos/<int:valores>/<int:columnas>")
@app.route("/arreglos/<int:valores>/<int:columnas>/<int:filas>")
def arreglos(valores=0,columnas=0,filas=0):
    if filas==0:
        arreglo=np.random.randint(valores, size=columnas)
    else:
        arreglo=np.random.randint(valores, size=(filas,columnas))
    
    return f"<h1> El arreglo aleatorio es: {arreglo}</h1> <hr>"

# Programa 1: Ecuación
@app.route("/ecuacion")
@app.route("/ecuacion/<int:x>/<int:z>")
def ecuacion(x=0,z=0):
    resultado = (x*z+z+x)
    return f"El resultado de la ecuación Y = X * Z + Z + X es: {resultado}"

@app.route('/tabla/<int:numero>')
def tabla_multiplicar(numero):
    tabla = [(i, numero * i) for i in range(1, 11)]
    resultado_html = ''.join(f'<tr><td>{(numero)}</td><td>{factor}</td><td>{resultado}</td></tr>' for factor, resultado in tabla)
    return f'''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Tabla de Multiplicar</title>
        </head>
        <body>
            <h1>Tabla de Multiplicar del {numero}</h1>
            <table border="1">
                <tr>
                    <th>Factor</th>
                    <th>X=</th>
                    <th>Resultado</th>
                    
                </tr>
                {resultado_html}
            </table>
        </body>
        </html>
    '''



# Programa para calcular áreas de círculo, cuadrado y triángulo
@app.route('/areas/<float:radio_circulo>/<float:lado_cuadrado>/<float:base_triangulo>/<float:altura_triangulo>')
def areas(radio_circulo, lado_cuadrado, base_triangulo, altura_triangulo):
    area_circulo = calcular_area_circulo(radio_circulo)
    area_cuadrado = calcular_area_cuadrado(lado_cuadrado)
    area_triangulo = calcular_area_triangulo(base_triangulo, altura_triangulo)

    return f'''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Áreas</title>
        </head>
        <body>
            <h1>Áreas Calculadas</h1>
            <p><tr><td> Área del círculo: {area_circulo}</td></tr></p>
            <p>Área del cuadrado: {area_cuadrado}</p>
            <p>Área del triángulo: {area_triangulo}</p>
        </body>
        </html>
    '''

def calcular_area_circulo(radio):
    return 3.14159 * radio**2  # Fórmula del área del círculo

def calcular_area_cuadrado(lado):
    return lado**2  # Fórmula del área del cuadrado

def calcular_area_triangulo(base, altura):
    return (base * altura) / 2  # Fórmula del área del triángulo

if __name__ == '__main__':
    app.run(debug=True)
