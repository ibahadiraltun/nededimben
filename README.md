# #nededimben
Herkesin bize ait bilgileri bilmesini istemeyiz. Ancak sosyal medyayı kullanırken farkında olmadan kendimize ait birçok kişisel bilgiyi de paylaşmaktayız. Doğal dil işleme alanındaki gelişmeler ile kişilerin paylaştıkları mesajlardan da siyasi görüş, psikolojik durum, konum, meslek gibi kişisel bilgilerine dair başarılı tahminler  yapabilen modeller geliştirilmektedir. Sosyal medya platformlarının uzun ve karmaşık kişisel veri kullanımı sözleşmeleri insanların kendilerine dair ne tür bilgilerin çıkarılabildiklerini anlamalarına yardımcı olmamaktadır.

Her internet kullanıcısının kendisine dair ne tür bilgilerin çıkarılabildiğini bilme hakkı olduğuna inanıyoruz.  
**Çünkü bilgi güçlü bir silahtır**

## Proje Süreci
Doğal dil işleme üzerine yapılan araştırmalar sonucu birçok model ile Türkçe üzerine dil analizi yapmak mümkündür. Özellikle Google tarafından geliştirilen BERT metodu kullanarak eğitilen modeller ile duygu analizi, konum, meslek vb. alanlarda güzel sonuçlar elde edebilmekteyiz.

Ancak bunları yaparken kullandığımız hazır-önceden eğitilimiş- modeller Türkçe harici bir dil üzerinden eğitilmiş olduğundan sonuç Türkçe dilinin yapısal özelliklerinden uzak olmaktadır. Bundan dolayı ise Türkçe veri kullanarak eğitilen [BERTurk](https://github.com/stefan-it/turkish-bert) modeli sunulmuştur.

BERTurk; çoğunlukla Wikipedia verisi kullanarak eğitildiğinden dili çok düzgün ve kurallıdır. **Ancak sosyal medya paylaşımlarının dili genel olarak dilbilgisi bakımından hatalı ve devriktir.**

Bu duruma çözüm/alternatif olarak kendi eğittiğimiz BERTurk-Social modelini Türkçe Doğal Dil İşleme topluluğuna sunmaktayız.

## Paylaşılan Modeller
Paylaştığımız modeller Türkçe sosyal medya verisi kullanarak oluşturduğumuz 56 milyonluk veri iletisinin 5 milyonluk kısmından eğitilmiştir. Ayrıca BERT metodu yerine onun gibi ancak bazı istisnalar yaparak daha hızlı çalışan RoBERTa metodunu kullandık. 
1 ve 5 milyon Türkçe sosyal medya iletisi kullanılarak oluşturduğumuz RoBERTa modellerimiz:
```
https://huggingface.co/YSKartal/berturk-social-5m
https://huggingface.co/ibahadiraltun/berturk-social
```

5 milyon ileti ile eğitilen modeli 3 task için ayrı ayrı fine tune ederek oluşturduğumuz modeller `/models/fine-tune/` klasörü içerisinde:
```
ft5m_sa: duygu analizi
ft5m_off: saldırganlık analizi
ft5m_cw: teyide muhtaçlık analizi
```

Fine tune etmek için kullandığımız referans veri kaynakları:
```
ft5m_sa: https://github.com/sercankulcu/twitterdata
ft5m_off: https://coltekin.github.io/offensive-turkish/
ft5m_cw: Kendimiz oluşturduk
```

Fine tune işlemini nasıl yaptığımız örneği(saldırganlık tespiti analizi için örnek verilmiştir o yüzden ilgili veri dosyasının 'off_tr.tsv' adıyla notebookun çalıştığı yüklenmesi gerekmektedir):
```
https://colab.research.google.com/drive/1l7vZNJ6ZlX_A_6c3Lpkprg9G_AbJIIAI?usp=sharing
```

## Fine Tune Modeller Kullanımı

Colab notebook üzerinden doğrudan kullanım örneği:
```
https://colab.research.google.com/drive/17eyvr29TaFlJMNTcX6A_uZHySSFFDY1y?usp=sharing
```

## Web Uygulaması
Eğittiğimiz modellerin nasıl kullanılabileceğine dair örnek bir web arayüzü geliştirdik. Uygulamamızın çalışma prensibi aşağıdaki gibidir:
![Alt text](https://i.ibb.co/BZKqyxx/app-structure.png)  
Uygulamamız frontend tarafında vue.js ile çalışıp sizden mesaj veya tweet linki girmenizi beklemektedir. Girilen mesajlar sonrasında sunucu tarafında değerlendirilecektir. Bu esnada bize daha çok esneklik kazandırması açısından python ile oluşturduğumuz Predictor yapısı aslında arka tarafta tüm modelleri yükleyip Server tarafından iletilen isteklere gerekli yanıtları döndürmektedir. Bunu direk Server içerisinde halledebilirdik ancak bu sayede gerekirse python üzerinden yeni birçok eklenti geliştirebiliriz.  
Uygulamayı indirip kullanmak için lütfen Web Kurulum bölümüne geçiniz.  

## Web Kurulum
Web kurulumuna başlamadan önce bilgisayarınızda `npm` ve `node` yüklemesinin yapılmış olması gerekmektedir. Eğer daha önceden yapmadıysanız [buradaki](https://www.npmjs.com/get-npm) adımları takip ederek indirebilirsiniz.  
Öncelikle bu `git clone https://github.com/ibahadiraltun/nededimben.git` diyerek bu kodu indirin ve uygulamamızın bulunduğu dizine `cd web-app` ile gidin.
Sonrasında ise:  
1. `pip install -r requirements.txt` - gerekli python paketlerini indirir.  
2. `npm install` - server için gerekli olan node modüllerini indirir.  
3. `cd client && npm install` - client için gerekli olan vue modüllerini indirir.  

Uygulamanın çalışması için gerekli olan tüm paketleri indirdik ve localhost'umuzda artık kullanabiliriz. `web-app/` dizininde olduğunuzdan emin olun ve aşağıdaki komutları çalıştırın:  
1. `npm run dev` - server tarafını localhost:8081 de çalıştırır.
2. yeni bir komut sekmesinde `cd client && npm run serve` client tarafını localhost:8080 de çalıştırır.

Harika! Artık localhost:8080/ üzerinden uygulamayı kullanabilirsiniz.

## Referans
[Turkish-Bert](https://github.com/stefan-it/turkish-bert)  
[Huggingface](https://huggingface.co/blog/)  
[Off-Data](https://coltekin.github.io/offensive-turkish)  
[Sent-Analysis](https://github.com/sercankulcu/twitterdata)  


[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


