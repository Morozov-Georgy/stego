# stego
В программе crypt.py представлена реализация стеганографического метода LSB совместстно
с шифрованием одноразовым блокнотом. Программа принимает сообщение, получает его битовое 
представление и случайным образом (согласно сгенерированному ключу) выбирает пиксели на 
картинке и заменяет последний бит красного цвета на бит из сообщения. Таким образом 
помимо того, что сообщение гаранитрованно будет секретным, оно еще и будет защищено 
стеганографически. Для расшифровки требуется секретный ключ. В идеале сначала генерируется
общий ключ для общающихся, а уже затем на основе него происходит шифрование. В программе, для 
наглядности, ключ генерируется непосредственно перед шифрованием. И поэтому, для расшифровки
ключ все таки нужно как то передавать приемнику.

Программа decrypt.py получает на вход зашифрованную картинку и ключ. И расшифровывает
сообщение согласно данным.
