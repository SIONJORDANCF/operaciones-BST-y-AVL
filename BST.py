class NodoBST:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBST:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        def _insertar(nodo, valor):
            if nodo is None:
                return NodoBST(valor)
            elif valor < nodo.valor:
                nodo.izquierda = _insertar(nodo.izquierda, valor)
            else:
                nodo.derecha = _insertar(nodo.derecha, valor)
            return nodo
        self.raiz = _insertar(self.raiz, valor)

    def buscar(self, valor):
        def _buscar(nodo, valor):
            if nodo is None or nodo.valor == valor:
                return nodo
            if valor < nodo.valor:
                return _buscar(nodo.izquierda, valor)
            else:
                return _buscar(nodo.derecha, valor)
        return _buscar(self.raiz, valor)

    def recorrido_inorden(self):
        resultado = []
        def _inorden(nodo):
            if nodo:
                _inorden(nodo.izquierda)
                resultado.append(nodo.valor)
                _inorden(nodo.derecha)
        _inorden(self.raiz)
        return resultado

    def eliminar(self, valor):
        def _minimo_nodo(nodo):
            while nodo.izquierda:
                nodo = nodo.izquierda
            return nodo

        def _eliminar(nodo, valor):
            if not nodo:
                return nodo
            if valor < nodo.valor:
                nodo.izquierda = _eliminar(nodo.izquierda, valor)
            elif valor > nodo.valor:
                nodo.derecha = _eliminar(nodo.derecha, valor)
            else:
                if nodo.izquierda is None:
                    return nodo.derecha
                elif nodo.derecha is None:
                    return nodo.izquierda
                temp = _minimo_nodo(nodo.derecha)
                nodo.valor = temp.valor
                nodo.derecha = _eliminar(nodo.derecha, temp.valor)
            return nodo

        self.raiz = _eliminar(self.raiz, valor)