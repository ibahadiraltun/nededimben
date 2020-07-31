# #nededimben
Projemizin amacı ...

## Modeller
1 ve 5 milyon Türkçe sosyal medya iletisi kullanılarak oluşturduğumuz RoBERT a modellerimiz:
```
https://huggingface.co/YSKartal/berturk-social-5m
https://huggingface.co/ibahadiraltun/berturk-social
```

5 milyon ileti ile eğitilen modeli 3 task için ayrı ayrı fine tune ederek oluşturduğumuz modeller `/models/fine/` klasörü içerisinde:
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

# Web Kurulum
Web kurulumuna başlamadan önce bilgisayarınızda `npm` ve `node` yüklemesinin yapılmış olması gerekmektedir. Eğer daha önceden yapmadıysanız [buradaki](https://www.npmjs.com/get-npm) adımları takip ederek indirebilirsiniz.
Öncelikle bu `git clone https://github.com/ibahadiraltun/teknofest.git` diyerek bu kodu indirin ve uygulamamızın bulunduğu dizine `cd web-app` ile gidin.
Sonrasında ise: 
`1. pip install requirements.txt` - gerekli python paketlerini indirir.
`2. npm install` - server için gerekli olan node modüllerini indirir.
`3. cd client && npm install` - client için gerekli olan vue modüllerini indirir.

Uygulamanın çalışması için gerekli olan tüm paketleri indirdik ve localhost'umuzda artık kullanabiliriz. `web-app/` dizininde olduğunuzdan emin olun ve aşağıdaki komutları çalıştırın:
`1. npm run dev` - server tarafını localhost:8081 de çalıştırır.
`2. cd client && npm run serve` client tarafını localhost:8080 de çalıştırır.


