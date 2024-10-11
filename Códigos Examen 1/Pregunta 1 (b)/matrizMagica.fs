module matrizMagica
open System
// Método que verifica si una matriz cuadrada es mágica
let esMagico (matrix: int[,]) =
    let size = Array2D.length1 matrix  // Tamaño de la matriz 
    
    // Metodos que calculan la suma de los elementos por fila, columna y diagonal
    let sumaRow r = Array.sum [| for c in 0 .. size - 1 -> matrix.[r, c] |]
    let sumaCol c = Array.sum [| for r in 0 .. size - 1 -> matrix.[r, c] |]
    let sumaDiag1 = Array.sum [| for i in 0 .. size - 1 -> matrix.[i, i] |]
    let sumaDiag2 = Array.sum [| for i in 0 .. size - 1 -> matrix.[i, size - 1 - i] |]

    let targetSum = sumaRow 0  // Suma objetivo de la primera fila
    let rowSumas = [| for r in 0 .. size - 1 -> sumaRow r |]  // Suma de cada fila
    let colSumas = [| for c in 0 .. size - 1 -> sumaCol c |]  // Suma de cada columna

    // Se verifica si todas las sumas (filas, columnas, diagonales) son iguales a la suma objetivo
    Array.forall ((=) targetSum) (Array.append rowSumas (Array.append colSumas [| sumaDiag1; sumaDiag2 |]))

// Uso del método
printfn "Introduce el orden de la matriz: "
let n = Int32.Parse(Console.ReadLine())

// Se crea una matriz de nxn inicializada con ceros
let matriz = Array2D.zeroCreate<int> n n

// Se rellena la matriz con valores ingresados por el usuario
for i in 0 .. n - 1 do
    for j in 0 .. n - 1 do
        printf "Ingresa un numero para la posicion (%d, %d): " i j
        let numero = Int32.Parse(Console.ReadLine())
        matriz.[i, j] <- numero

// Se verifica si la matriz es mágica y se imprime el resultado
let m = esMagico matriz
printfn "La matriz es magica: %b" m
