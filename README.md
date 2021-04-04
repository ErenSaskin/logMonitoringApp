# Log monitoring app
#
##### FastAPI, PostgreSql, Kafka, Grafana
#
- Python FastAPI ile 4 farklı endpoint bulunur.
- İsteklere random 1000/3000 ms arası cevap döner ve log yazar. ({methodType, ms, timestamp})
- Kafka Producer log dosyasından satır satır okur ve log topice gönderir.
- Kafka Consumer log topicden verileri okur veritabanına ekler.
- Grafana postgreSql veritabanına eklenen logları anlık olarak monitör eder.

## Docker
**Proje dizinine gidin** ve aşağıdaki komutu **Docker** ile çalıştırın. Docker uygulamayı ve bağımlılıklarını yükleyecektir. 
```sh
docker-compose up -d
```

Yükleme tamamlanınca aşağıdaki adresi tarayıcıda çalıştırın. Swagger arayüzü ile istek gönderebilirsiniz. bkz:   [FastAPI](https://fastapi.tiangolo.com/#interactive-api-docs) 

```sh
http://localhost:8000/docs
```
#
# Dashboard
1 - Aşağıdaki adrese giderek grafanaya erişin ve giriş yapın. 
**user**: admin 
**pasword**: admin
```sh
http://localhost:3000
```
2 - Aşağıdaki bağlantıya giderep postgreSql veritabanını Grafanaya gösterin.
```sh
http://localhost:3000/datasources/new
```
- **Database**: root
- **user**: root
- **password**: 1234
- **TLS/SSL Mode**: Disable
- Buradaki *localhost:5432* yerine docker **bridge gateway** eklemeniz gerekebilir. Bunun için aşağıdaki komutu çalıştırın ve *config>gateway* adresini HOST alanına ekleyin. Örn:-> *gateway-adresi:5432*
```sh
docker inspect bridge
```
3 - Son olarak aşağıdaki bağlantıya gidip proje dizinindeki **dashboard.json** dosyasını yükeyip az önce tanıttığınız veritabanını seçip yükleyin.
```sh
http://localhost:3000/dashboard/import
```
***Dashboard > Manage > new Dashboard*** a giderek gönderdiğiniz istekleri grafik üzerinde görebilirsiniz.

#
#
#

anahtar kodu:
```sh
gAAAAABgUPdH2eoetAHkRfa1HJZJLhoxZWi6WDc0luvMF-Z-KZNbIQc1mZO6LGvyEAt3D8j3N2NRSc95PMxD7LCOoJ9D462jaxScGH-VejZ3cEZ8owwKAtaYFVUYD9hYQFMdY2Z4t4XYmrhDUTjE3E-G0ztcPb5j_1-3z6BNGG_0F6UMxsFTRHgnYlMNH9K4EdL9Uphlj_Iz
```