'''
Este programa muestra como utilizar los operadores lógicos. And or y not. Se utilizan tablas de verdad para
saber como construir expresiones con ellos.
'''
numero1 = 20
numero2 = 24
numero3 = 26


resultado = ((numero1>numero2) or (numero1<numero3)) and ((numero1==numero3) or (numero1>=numero2))
                                # falso or verdadero y falso o falso
                                        # verdadero  y falso
                                                  # falso

print(resultado)