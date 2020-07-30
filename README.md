# teknofest


# Modeller
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

Fine etmek için kullandığımız referans veri kaynakları:
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
