# ROS1'den ROS2'ye Geçiş Rehberi

Bu rehber, ROS1 (Noetic) kullanan mobil robot sisteminizi ROS2 (Humble)'a geçirmenize yardımcı olmak için hazırlandı. Rehberimiz, LIDAR ve derinlik kamerası bulunan **LIMCOBOT** isimli mobil robot üzerinde yoğunlaşmaktadır ve Python ile C++ dillerini temel alır. Ayrıca, robotun simülasyonu **Gazebo** ortamında gerçekleştirilerek gerçek donanım öncesi testler yapılacaktır.

## 📌 Hedef Kitle
Bu rehber, **ROS1 konusunda orta seviye bilgiye sahip** kullanıcılar için hazırlanmıştır ve pratik, örnek tabanlı bir geçiş süreci sunar.

## 📦 İçerik Başlıkları

- 🔁 ROS1 ve ROS2 arasındaki temel farklar (Noetic → Humble)
- 🛠️ `colcon` kullanarak ROS2 paket yapısı ve workspace oluşturma
- 🚀 `.launch` (XML) → Python tabanlı launch dosyası dönüşümü
- ⚙️ Parametre yönetimi ve dinamik yapılandırma
- 🔄 TF ve TF2 dönüşümleri
- 📡 Navigasyon, haritalama ve MoveIt geçişi
- 🧪 ROS1 ve ROS2 versiyonları ile örnek kodlar
- 🧭 **Gazebo simülasyonu**: ROS1 vs ROS2 ile simülasyon yapısı
- 🔗 `ros1_bridge` ile hibrit ortam geçişi

## 🧰 Gereksinimler

- Ubuntu 22.04 (Jammy)
- ROS1 Noetic (karşılaştırma için)
- ROS2 Humble
- VSCode (önerilen)
- colcon, rosdep, vcs vb. araçlar
- Gazebo (Classic ve Ignition/GZ destekli)

## 📁 Dizin Yapısı

- `docs/`: Teknik dokümantasyon ve geçiş adımları
- `examples/`: ROS1 ve ROS2 versiyonlarını gösteren örnek kodlar
- `images/`: Diyagramlar ve ekran görüntüleri

## 🚀 Başlarken

1. Bu repoyu klonlayın.
2. `docs/` klasöründeki adımları takip edin.
3. Örneklerle kendi kod geçişinizi test edin.

## 🤝 Katkı Sağlama

Topluluk katkılarını memnuniyetle karşılıyoruz! Forklayın, geliştirmelerle veya düzeltmelerle pull request gönderin.

---

ROS sisteminizi modernleştirmeye birlikte başlayalım 🧠🤖

--- 

# ROS1 (Noetic) ile ROS2 (Humble) Arasındaki Temel Farklar

Bu bölümde, ROS1 ve ROS2 arasındaki temel mimari farkları, yeni özellikleri ve neden ROS2'ye geçiş yapılması gerektiğini detaylı bir şekilde inceleyeceğiz.

---

## 1. Giriş: Neden ROS2?

ROS1, uzun yıllar boyunca robotik alanında standart bir platform haline gelmiştir. Ancak zamanla aşağıdaki eksiklikleri nedeniyle daha sürdürülebilir, güvenli ve modüler bir altyapıya ihtiyaç duyulmuştur:

- **Gerçek zamanlılık desteği eksikliği**
- **Güvenlik önlemlerinin olmaması**
- **Çok robotlu sistemlerde sınırlı performans**
- **Dağıtık sistemlerde esneklik eksikliği**

ROS2, bu eksiklikleri gidermek için sıfırdan tasarlanmıştır. Özellikle **DDS (Data Distribution Service)** altyapısı sayesinde daha esnek, güvenli ve özelleştirilebilir bir iletişim yapısı sunar.

---

## 2. İletişim Altyapısı

| Özellik        | ROS1                         | ROS2 (Humble)                     |
|----------------|------------------------------|-----------------------------------|
| Protokol       | TCPROS / UDPROS              | DDS tabanlı (FastDDS, CycloneDDS vb.) |
| QoS Desteği    | Yok                           | Var (reliability, durability, history vs.) |
| Multicast      | Yok                           | Var                               |
| Güvenlik       | Harici çözümler gerekir       | SROS2 ile entegre                 |
| Discovery      | Manuel veya topic bazlı       | Otomatik discovery                |

---

## 3. Workspace ve Paket Yapısı

ROS2’de workspace yapısı modernleştirilmiştir. `colcon` aracı, bağımsız paketlerin paralel derlenmesini ve yönetimini sağlar.

### ROS1 (catkin)
```bash
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws
catkin_make

### ROS2 (colcon)
bash
Copy
Edit
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws
colcon build
