import objandfuncs as lib

lib.header()

produtos, _refs = lib.carregar_dados()

while True:
    ent = lib.ler()

    lib.limpar_buffer()

    if lib.nao_tem_problema(ent):
        
        ref, cor, tam = ent

        if lib.tem_essa_ref(ref,_refs):

            if lib.tem_essa_cor(produtos,_refs,ref,cor):
                print('adicionado mais um...')
                produtos[_refs[ref]].dat[produtos[_refs[ref]].lig[cor]][tam] += 1

            else:
                print('Criando cor...')
                produtos[_refs[ref]].lig.update({cor:len(produtos[_refs[ref]].dat)})
                a = lib.addcor(cor)
                a[tam] = 1
                produtos[_refs[ref]].dat.append(a)

        else:
            print('Criando referência e cor...')
            new = lib.produto(ref,[lib.addcor(cor)],{cor:0})
            new.dat[new.lig[cor]][tam] = 1
            
            _refs.update({ref:len(produtos)})
            produtos.append(new)

        lib.salvar(produtos)

    else:
        continue
