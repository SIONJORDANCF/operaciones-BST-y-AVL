class NodoAVL:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
        self.altura = 1

class ArbolAVL:
    def __init__(self):
        self.raiz = None

    def _obtener_altura(self, nodo):
        return nodo.altura if nodo else 0

    def _obtener_balance(self, nodo):
        if not nodo:
            return 0
        return self._obtener_altura(nodo.izquierda) - self._obtener_altura(nodo.derecha)

    def _rotacion_derecha(self, y):
        x = y.izquierda
        T2 = x.derecha
        x.derecha = y
        y.izquierda = T2
        y.altura = 1 + max(self._obtener_altura(y.izquierda), self._obtener_altura(y.derecha))
        x.altura = 1 + max(self._obtener_altura(x.izquierda), self._obtener_altura(x.derecha))
        return x

    def _rotacion_izquierda(self, x):
        y = x.derecha
        T2 = y.izquierda
        y.izquierda = x
        x.derecha = T2
        x.altura = 1 + max(self._obtener_altura(x.izquierda), self._obtener_altura(x.derecha))
        y.altura = 1 + max(self._obtener_altura(y.izquierda), self._obtener_altura(y.derecha))
        return y

    def insertar(self, valor):
        def _insertar(nodo, valor):
            if not nodo:
                return NodoAVL(valor)
            elif valor < nodo.valor:
                nodo.izquierda = _insertar(nodo.izquierda, valor)
            else:
                nodo.derecha = _insertar(nodo.derecha, valor)

            nodo.altura = 1 + max(self._obtener_altura(nodo.izquierda), self._obtener_altura(nodo.derecha))
            balance = self._obtener_balance(nodo)

            # Casos de rotación
            if balance > 1 and valor < nodo.izquierda.valor:  # Izquierda Izquierda
                return self._rotacion_derecha(nodo)
            if balance < -1 and valor > nodo.derecha.valor:  # Derecha Derecha
                return self._rotacion_izquierda(nodo)
            if balance > 1 and valor > nodo.izquierda.valor:  # Izquierda Derecha
                nodo.izquierda = self._rotacion_izquierda(nodo.izquierda)
                return self._rotacion_derecha(nodo)
            if balance < -1 and valor < nodo.derecha.valor:  # Derecha Izquierda
                nodo.derecha = self._rotacion_derecha(nodo.derecha)
                return self._rotacion_izquierda(nodo)

            return nodo

        self.raiz = _insertar(self.raiz, valor)

    def recorrido_inorden(self):
        resultado = []
        def _inorden(nodo):
            if nodo:
                _inorden(nodo.izquierda)
                resultado.append(nodo.valor)
                _inorden(nodo.derecha)
        _inorden(self.raiz)
        return resultado