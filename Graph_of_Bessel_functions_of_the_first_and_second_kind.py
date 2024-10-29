import numpy as np
import matplotlib.pyplot as plt
from scipy.special import jn, yn, jv

# Valores de x

x = np.linspace(0, 10, 400)

# Función de Bessel de primera especie de orden n

y0 = jn(0, x)
y1 = jn(1, x)
y2 = jn(2, x)
y3 = jn(3, x)
y4 = jn(4, x)

plt.plot(x, y0, label = 'J_{0}')
plt.plot(x, y1, label = 'J_{1}')
plt.plot(x, y2, label = 'J_{2}')
plt.plot(x, y3, label = 'J_{3}')
plt.plot(x, y4, label = 'J_{4}')

plt.xlabel('x')
plt.ylabel('J_{n}(x)')
plt.title('''Función de Bessel de primera especie de orden n, n = 0,1,2,3,4
          ''')
plt.xlim(-2, 10)
plt.ylim(-2, 2)
plt.legend(loc = 'upper right')
plt.show()

# Función de Bessel de primera especie de orden -n

y1 = jn(-1, x)
y2 = jn(-2, x)
y3 = jn(-3, x)
y4 = jn(-4, x)

plt.plot(x, y1, label = 'J_{-1}')
plt.plot(x, y2, label = 'J_{-2}')
plt.plot(x, y3, label = 'J_{-3}')
plt.plot(x, y4, label = 'J_{-4}')

plt.xlabel('x')
plt.ylabel('J_{-n}(x)')
plt.title('''Función de Bessel de primera especie de orden -n, n = 1,2,3,4
          ''')
plt.xlim(-2, 10)
plt.ylim(-2, 2)
plt.legend(loc = 'upper right')
plt.show()

# Función de Bessel de primera especie de orden n/2

y1 = jv(0.5, x)
y2 = jv(1.5, x)
y3 = jv(2.5, x)
y4 = jv(3.5, x)

plt.plot(x, y1, label = 'J_{1/2}')
plt.plot(x, y2, label = 'J_{3/2}')
plt.plot(x, y3, label = 'J_{5/2}')
plt.plot(x, y4, label = 'J_{7/2}')

plt.xlabel('x')
plt.ylabel('J_{n/2}(x)')
plt.title('''Función de Bessel de primera especie de orden n/2, n = 1,3,5,7
          ''')
plt.xlim(-2, 10)
plt.ylim(-2, 2)
plt.legend(loc = 'upper right')
plt.show()

# Función de Bessel de primera especie de orden -n/2

y1 = jv(-0.5, x)
y2 = jv(-1.5, x)
y3 = jv(-2.5, x)
y4 = jv(-3.5, x)

plt.plot(x, y1, label = 'J_{-1/2}')
plt.plot(x, y2, label = 'J_{-3/2}')
plt.plot(x, y3, label = 'J_{-5/2}')
plt.plot(x, y4, label = 'J_{-7/2}')

plt.xlabel('x')
plt.ylabel('J_{n/2}(x)')
plt.title('''Función de Bessel de primera especie de orden -n/2, n = 1,3,5,7
          ''')
plt.xlim(-2, 10)
plt.ylim(-2, 2)
plt.legend(loc = 'upper right')
plt.show()

# Función de Bessel de segunda especie de orden n

y0 = yn(0, x)
y1 = yn(1, x)
y2 = yn(2, x)
y3 = yn(3, x)
y4 = yn(4, x)

plt.plot(x, y0, label = 'Y_{0}')
plt.plot(x, y1, label = 'Y_{1}')
plt.plot(x, y2, label = 'Y_{2}')
plt.plot(x, y3, label = 'Y_{3}')
plt.plot(x, y4, label = 'Y_{4}')

plt.xlabel('x')
plt.ylabel('Y_{n}(x)')
plt.title('''Función de Bessel de segunda especie de orden n, n = 0,1,2,3,4
          ''')
plt.xlim(-2, 10)
plt.ylim(-2, 2)
plt.legend(loc = 'upper right')
plt.show()

# Función de Bessel de segunda especie de orden -n

y1 = yn(-1, x)
y2 = yn(-2, x)
y3 = yn(-3, x)
y4 = yn(-4, x)


plt.plot(x, y1, label = 'Y_{-1}')
plt.plot(x, y2, label = 'Y_{-2}')
plt.plot(x, y3, label = 'Y_{-3}')
plt.plot(x, y4, label = 'Y_{-4}')

plt.xlabel('x')
plt.ylabel('Y_{-n}(x)')
plt.title('''Función de Bessel de segunda especie de orden -n, n = 1,2,3,4
          ''')
plt.xlim(-2, 10)
plt.ylim(-2, 2)
plt.legend(loc = 'upper right')
plt.show()
