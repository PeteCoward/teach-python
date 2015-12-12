## TASK4 - find the shift with the lowest difference rating
from .task2 import get_byte_frequencies
from .task3 import get_difference_rating
from lesson2.task5 import get_all_shifts

encrypted = "6b9542968a8b9542968a87429487838e428e8b8887612c6b9542968a8b95428c979596428883909683959b612c658397898a96428b904283428e839086958e8b86874e2c709142879585839287428894918f429487838e8b969b502c2c71928790429b91979442879b87954e2c6e91918d42979242969142968a8742958d8b879542839086429587874e2c6b498f428c979596428342929191944284919b4e426b429087878642909142959b8f9283968a9b4e2c64878583979587426b498f428783959b4285918f874e428783959b4289914e2c6e8b96968e87428a8b898a4e428e8b96968e87428e91994e2c63909b99839b42968a8742998b908642848e9199954286918795904996429487838e8e9b428f8396968794429691428f874e429691428f87502c2c6f838f834e428c979596428d8b8e8e87864283428f83904e2c729796428342899790428389838b909596428a8b95428a8783864e2c72978e8e8786428f9b4296948b898987944e42909199428a8749954286878386502c6f838f834e428e8b8887428a8386428c9795964284878997904e2c64979642909199426b49988742899190874283908642968a94919990428b9642838e8e428399839b502c2c6f838f834e4291918a4e2c668b86904996428f878390429691428f838d87429b91974285949b4e2c6b88426b498f42909196428483858d428389838b9042968a8b9542968b8f874296918f91949491994e2c658394949b4291904e42858394949b429190428395428b88429091968a8b9089429487838e8e9b428f839696879495502c2c769191428e8396874e428f9b42968b8f87428a83954285918f874e2c7587909642958a8b988794954286919990428f9b4295928b90874e2c6491869b49954283858a8b908942838e8e42968a8742968b8f87502c69919186849b874e42879887949b8491869b4e426b499887428991964296914289914e2c6991969683428e87839887429b919742838e8e4284878a8b908642839086428883858742968a8742969497968a502c2c6f838f834e4291918a424a83909b99839b42968a8742998b908642848e9199954b4e2c6b42869190499642998390908342868b874e2c6b4295918f87968b8f879542998b958a426b49864290879887944284878790428491949042839642838e8e502c2c6b429587874283428e8b96968e8742958b8e8a9197879696914291884283428f83904e2c75858394838f9197858a874e4275858394838f9197858a874e42998b8e8e429b919742869142968a87426883908683908991612c768a979086879484918e9642839086428e8b898a96908b90894e2c7887949b4e429887949b4288948b898a9687908b9089428f87502c4a69838e8b8e87914b4269838e8b8e8791502c4a69838e8b8e87914b4269838e8b8e87914e2c69838e8b8e879142688b898394912c6f8389908b888b8591502c2c6b498f428c979596428342929191944284919b4e4290918491869b428e91988795428f87502c6a874995428c979596428342929191944284919b428894918f428342929191944288838f8b8e9b4e2c7592839487428a8b8f428a8b95428e8b8887428894918f42968a8b95428f919095969491958b969b502c2c6783959b4285918f874e428783959b4289914e42998b8e8e429b9197428e8796428f87428991612c648b958f8b8e8e838a434270914e42998742998b8e8e42909196428e8796429b919742899150424a6e8796428a8b8f428991434b2c648b958f8b8e8e838a4342798742998b8e8e42909196428e8796429b919742899150424a6e8796428a8b8f428991434b2c648b958f8b8e8e838a4342798742998b8e8e42909196428e8796429b919742899150424a6e8796428f87428991434b2c798b8e8e42909196428e8796429b919742899150424a6e8796428f87428991434b2c70879887944e429087988794428e8796429b91974289912c7087988794428e8796428f874289914e42918a502c70914e4290914e4290914e4290914e4290914e4290914e429091502c718a4e428f838f83428f8b834e428f838f83428f8b83424a6f838f83428f8b834e428e8796428f87428991504b2c6487878e9c87849784428a83954283428687988b8e429297964283958b86874288916487878e9c87849784428a83954283428687988b8e429297964283958b86874288916487878e9c87849784429596919087428f87428390864295928b96428b90428f9b42879b87612c7591429b919742968a8b908d429b919742858390428e919887428f8742839086428e87839887428f8742969142868b87612c718a4e428483849b4e42858390499642869142968a8b95429691428f874e428483849b4e2c6c97959642899196968342898796429197964e428c9795964289919696834289879642948b898a96429197969683428a879487502c2c4a718a4e429b87838a4e42918a429b87838a4b2c2c7091968a8b9089429487838e8e9b428f8396968794954e2c63909b91908742858390429587874e2c7091968a8b9089429487838e8e9b428f8396968794954e2c7091968a8b9089429487838e8e9b428f839696879495429691428f87502c2c63909b99839b42968a8742998b908642848e91999550"


def find_best_decrypt():
    hex_bytes = bytearray.fromhex(encrypted)

    all_shifts = get_all_shifts(hex_bytes)

    lowest_rating = 999999999999
    for shift in all_shifts:
        frequencies = get_byte_frequencies(shift)
        rating = get_difference_rating(frequencies)
        if rating < lowest_rating:
            lowest_rating = rating
            best_shift = shift

    return best_shift