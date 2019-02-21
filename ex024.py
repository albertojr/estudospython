nome = input('Digite o nome de uma cidade: ').strip().upper()#removo os espaço e deixo tudo maisculo
print('Se o retorno for true, tem a palavra SANTO.\nCaso for False, não tem a palavra')
print('\n\nRetorno:{}'.format(nome[:5] == 'SANTO'))#leio as 5 primeiras letras
