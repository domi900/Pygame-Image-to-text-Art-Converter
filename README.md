<h1>Imagem em caracteres com Pygame</h1>
    <p>Este projeto é um exemplo de como criar uma imagem em caracteres usando o Pygame. O programa lê uma imagem, converte para escala de cinza, redimensiona 
        e converte em uma matriz de caracteres para ser exibida na tela.</p>
        <h2>Requisitos</h2>
        <ul><li>Python 3.x</li>
            <li>Pygame</li>
            <li>NumPy</li>
            <li>PIL (Python Imaging Library)</li>
        </ul><h2>Como usar</h2>
        <ol><li>Clone este repositório ou faça o download do arquivo .zip</li>
            <li>Instale as bibliotecas necessárias usando o pip:</li>
            pip install pygame numpy Pillow
            <li>Execute o programa main.py:</li></ol>
            <h2>Funcionamento</h2>
<p>O programa começa lendo uma imagem usando a biblioteca PIL e convertendo-a para escala de cinza. Em seguida, a imagem é redimensionada para 
    um tamanho menor (80x80 pixels, neste caso). A matriz de brilho resultante é convertida em uma matriz de caracteres usando a função <code>matrix_to_chars</code>, que mapeia 
    cada valor de brilho para um caractere apropriado.</p>
    <p>A matriz de caracteres é exibida na tela do Pygame usando a função <code>blit</code>, que desenha cada caractere na posição correta. 
        A fonte a ser usada é definida na inicialização do Pygame.</p>
        <h2>Funções</h2>
        <h3><code>matrix_to_chars(matrix, chars)</code></h3>
        <p>Esta função mapeia uma matriz de valores de brilho (0-255) para uma matriz de caracteres. A matriz de caracteres é construída usando
             uma lista de caracteres passada como argumento. Cada caractere é atribuído a um intervalo de brilho de tamanho igual, de modo que os 
             caracteres com menor brilho são atribuídos aos intervalos mais baixos e os caracteres com maior brilho aos intervalos mais altos.</p>
             <p>Parâmetros:</p><ul>
                <li><code>matrix</code> (array NumPy): a matriz de valores de brilho a ser mapeada.</li>
                <li><code>chars</code> (list): a lista de caracteres a ser usada para mapear os valores de brilho.</li></ul>
                <p>Retorna:</p><ul><li><code>char_matrix</code> (list): a matriz de caracteres resultante.</li></ul>
                <h2>Créditos</h2>
