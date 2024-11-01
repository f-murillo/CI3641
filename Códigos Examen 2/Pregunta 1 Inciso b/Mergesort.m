% Metodo "principal"
function Mergesort()
    array = [34, 7.2, 23, 32, 5, 62, 32.3, 45, 0];
    disp('Arreglo original:');
    disp(array);
    sortedArray = merge_sort(array);
    disp('Arreglo ordenado:');
    disp(sortedArray);
end

% Método que aplica Mergesort sobre un arreglo
function sortedArray = merge_sort(array)
    % Caso base: si la longitud del array es 1, ya está ordenado
    if numel(array) <= 1
        sortedArray = array;
        return;
    end

    % Dividir el arreglo en dos mitades
    mid = floor(numel(array) / 2);
    left = array(1:mid);
    right = array(mid+1:end);

    % Ordenar recursivamente cada mitad
    sortedLeft = merge_sort(left);
    sortedRight = merge_sort(right);

    % Combinar las dos mitades ordenadas
    sortedArray = merge(sortedLeft, sortedRight);
end

% Método que combina los dos subarreglos ordenados en un solo arreglo
% ordenado
function result = merge(left, right)
    % Inicializar arreglo final
    result = zeros(1, numel(left) + numel(right));
    i = 1;  % Índice para left
    j = 1;  % Índice para right
    k = 1;  % Índice para result

    % Fusionar las dos mitades ordenadas
    while i <= numel(left) && j <= numel(right)
        % Si el elemento de left es menor al elemento de right
        if left(i) <= right(j)
            result(k) = left(i); % Agregar el elemento de left
            i = i + 1;
        % En caso contrario
        else
            result(k) = right(j); % Agregar elemento de right
            j = j + 1;
        end
        k = k + 1; 
    end

    % Agregar los elementos restantes de left, si los hay
    while i <= numel(left)
        result(k) = left(i);
        i = i + 1;
        k = k + 1;
    end

    % Agregar los elementos restantes de right, si los hay
    while j <= numel(right)
        result(k) = right(j);
        j = j + 1;
        k = k + 1;
    end
end
