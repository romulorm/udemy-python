"""
Esta é uma descrição simples sobre o módulo modulo1.

Esta é uma descrição completa sobre o módulo. Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard
dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen
book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially
unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more
 recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.

It is a long established fact that a reader will be distracted by the readable content of a page when looking at its
layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using
 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page
 editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites
 still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose
 (injected humour and the like).

"""
from typing import Union


def soma(num1, num2) -> Union[int, float]:
    """
    Função que soma dois números.
    :param num1: Primeiro número.
    :type num1: int ou float.
    :param num2: Segundo número.
    :type num2: int ou float.
    :return: retorna um int ou float com a soma dos números.
    """
    return num1 + num2
