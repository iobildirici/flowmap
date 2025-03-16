# flowmap
Flowmap eklentisi, farklı düğüm noktaları arasındaki etkileşimleri gösteren akış verilerini (örneğin göçler, uçuş verileri, ticaret verileri) göstermek için kullanılır.

Farklı düğüm noktaları arasındaki akış çizgilerini oluşturmada kullanılmaktadır. Eklentide kullanılacak dosyalar QGIS'de halihazırda açık bulunan katmanlar arasından seçilmelidir. Bu dosyalardan düğüm noktaları dosyası, nokta geometrisine sahip olmalı ve içerisinde akış verileri ile eşleştirmeyi sağlayacak anahtar alan bulundurmalıdır. Akış verilerini içerisinde bulunduran dosya ise herhangi bir geometriye sahip olmamalı ve .xls, .xlsx, .csv vb. formatlarda olmalıdır. Akış verilerinin bulunduğu katman seçildikten sonra akışın yönünü belirten ve düğüm noktaları dosyasındaki anahtar alan ile eşleştirilecek iki sütun seçilmelidir. Bu iki sütun ve düğüm noktaları katmanından gelen anahtar alanın veri türleri aynı olmak zorundadır. Eklentinin çalıştırılması sonucu ise akış verilerini gösteren çizgilerin olduğu bir çizgi katmanı ve düğüm noktalarına giren-çıkan çizgi sayısını içerisinde bulunduran bir nokta katmanı oluşturulur. Oluşturulan çizgi katmanı düğüm noktaları arasındaki akışları gösterir. Nokta katmanı ise kullanıcıya Yoğunluk, Orantılı İşaret Haritası vb. başka haritalar yapma imkânı sunar.

Eklenti Caner Güzeler'in Prof.Dr. İbrahim Öztuğ BİLDİRİCİ yönetiminde tamamlanan yüksek lisans tezi kapsamında geliştirilmiştir. 

Eklentiyi yüklemek için flow_map.zip dosyasını indirin. QGIS eklentiler penceresinde "install from zip" seçin.
