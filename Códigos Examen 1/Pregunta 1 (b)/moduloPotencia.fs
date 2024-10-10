open System 
// Método recursivo para calcular la fórmula del módulo aplicado a potencias
// Observacion: en F# se debe especificar si un método es o no recursivo
let rec modPot (a: int) (b: int) (c: int) : int =
    // Si c es menor a 2, imprime el mensaje de error y retorna -1
    if c < 2 then
        printfn "Error: El valor de c debe ser mayor o igual a 2"
        -1 
    else
        match b with
        | 0 -> 1 // Si b es 0
        | _ -> (a % c) * (modPot a (b - 1) c) % c // En otro caso

// Uso del método
printfn "Ingresa el valor de a: "
let a = Int32.Parse(Console.ReadLine())
printfn "Ingresa el valor de b: "
let b = Int32.Parse(Console.ReadLine())
printfn "Ingresa el valor de c: "
let c = Int32.Parse(Console.ReadLine())
let result = modPot a b c
// Si result no es -1, imprime el resultado
if result <> -1 then
    printfn "El resultado de (%d^%d) mod %d es: %d" a b c result