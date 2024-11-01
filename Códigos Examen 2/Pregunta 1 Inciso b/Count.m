% Método "principal"
function Count()
    n = input('Ingresa un número: ');
    if n <= 0 || mod(n,1) ~= 0
       disp('n tiene que ser un entero positivo'); 
       return;
    end
    disp(['El count de ', num2str(n), ' es: ', num2str(c(n))]);
end

% Método que calcula f(n) como se define en el enunciado de la pregunta
function x = f(n)
    if mod(n,2) == 0
        x = n/2;
    else
        x = 3*n + 1;
    end
end

% Método que cuenta el número de aplicaciones de f sobre n hasta que el
% resultado sea 1
function a = c(n)
    a = 0;
    while n ~= 1
        n = f(n);
        a = a + 1;
    end
end
