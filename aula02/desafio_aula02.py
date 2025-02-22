
def media(lista):
    return sum(lista) / len(lista)


def regressao_linear(x, y):
   
    x_media = media(x)
    y_media = media(y)

  
    somatorio_num = 0
    somatorio_den = 0
    for i in range(len(x)):
        somatorio_num += (x[i] - x_media) * (y[i] - y_media)
        somatorio_den += (x[i] - x_media) ** 2
    
    
    beta_1 = somatorio_num / somatorio_den
    beta_0 = y_media - beta_1 * x_media

    return beta_0, beta_1


x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]


beta_0, beta_1 = regressao_linear(x, y)


print(f"A equação da reta de regressão é: y = {beta_0:.2f} + {beta_1:.2f}x")
