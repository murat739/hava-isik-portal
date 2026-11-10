# -- coding: utf-8 --
"""
Modül Adı: Hava, Işık ve Hikmet Portalı (Tam Metin, Çok Dilli & Gelişmiş Güvenlikli Master Sürüm)
"""

import streamlit as st
import pandas as pd

# ==========================================
# 1. SAYFA YAPILANDIRMASI
# ==========================================
st.set_page_config(
    page_title="Hava, Işık ve Hikmet Portalı / Air, Light & Wisdom Portal",
    page_icon="☀️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Kapsamlı Metin Seçimi, Sağ Tık, Kopyalama ve Kısayol Engelleme (CSS & JS)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Amiri:ital,wght@0,400;0,700;1,400&family=Inter:wght@300;400;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    /* Sayfadaki tüm metinlerin seçilmesini, kopyalanmasını ve sürüklenmesini tamamen engelle */
    * {
        -webkit-user-select: none !important;
        -moz-user-select: none !important;
        -ms-user-select: none !important;
        user-select: none !important;
        -webkit-touch-callout: none !important;
    }
    
    /* Form input ve textarea alanlarında veri girişine izin ver */
    input, textarea {
        -webkit-user-select: text !important;
        -moz-user-select: text !important;
        -ms-user-select: text !important;
        user-select: text !important;
    }
    
    .main-header {
        background: linear-gradient(135deg, #0284C7 0%, #0369A1 100%);
        padding: 35px;
        border-radius: 14px;
        color: white;
        text-align: center;
        box-shadow: 0 10px 25px rgba(2, 132, 199, 0.25);
        margin-bottom: 25px;
    }
    .main-header h1 {
        font-size: 2.2rem;
        font-weight: 800;
        margin-bottom: 8px;
    }
    .main-header p {
        font-size: 1.15rem;
        opacity: 0.95;
    }
    
    .arabic-text {
        font-family: 'Amiri', serif;
        font-size: 1.8rem;
        direction: rtl;
        text-align: right;
        color: #0F172A;
        line-height: 2.2;
        background-color: #F8FAFC;
        padding: 15px;
        border-radius: 8px;
        border-right: 5px solid #0284C7;
        margin-bottom: 10px;
    }
    
    .card-box {
        background-color: #FFFFFF;
        padding: 22px;
        border-radius: 12px;
        border-left: 5px solid #0284C7;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    
    .quote-box {
        background-color: #F0FDF4;
        border-left: 5px solid #16A34A;
        padding: 16px;
        border-radius: 6px;
        font-style: italic;
        color: #1E293B;
        font-size: 1.05rem;
        margin-top: 10px;
        margin-bottom: 12px;
        line-height: 1.6;
    }
    
    .science-box {
        background-color: #EFF6FF;
        border-left: 5px solid #2563EB;
        padding: 16px;
        border-radius: 6px;
        color: #1E3A8A;
        font-size: 1.05rem;
        margin-top: 10px;
        margin-bottom: 12px;
        line-height: 1.6;
    }
    
    .source-badge {
        display: inline-block;
        background-color: #F1F5F9;
        color: #334155;
        border: 1px solid #CBD5E1;
        padding: 4px 12px;
        border-radius: 20px;
        font-weight: 600;
        font-size: 0.85rem;
        margin-top: 8px;
    }
    
    .legal-box {
        background-color: #FEF2F2;
        border-left: 5px solid #DC2626;
        padding: 20px;
        border-radius: 8px;
        color: #7F1D1D;
        font-size: 0.9rem;
        line-height: 1.6;
        margin-top: 30px;
        margin-bottom: 20px;
        border-top: 1px solid #FEE2E2;
        border-right: 1px solid #FEE2E2;
        border-bottom: 1px solid #FEE2E2;
    }
</style>

<!-- Sağ Tıklama, Metin Seçme, Kopyalama ve Geliştirici Araçları Kısayollarını Engelleyen JavaScript -->
<script>
    // Sağ tıklama menüsünü engelle
    document.addEventListener('contextmenu', event => event.preventDefault());
    
    // Klavye kısayollarını (Ctrl+C, Ctrl+X, Ctrl+U, Ctrl+S, Ctrl+A, Ctrl+P, F12 vb.) engelle
    document.addEventListener('keydown', function(event) {
        if (
            (event.ctrlKey && (event.key === 'c' || event.key === 'x' || event.key === 'u' || event.key === 's' || event.key === 'a' || event.key === 'p' || event.key === 'i' || event.key === 'j')) ||
            event.key === 'F12'
        ) {
            event.preventDefault();
            alert("Güvenlik Uyarısı: Bu uygulamadaki içeriklerin kopyalanması, çoğaltılması ve dışarıya aktarılması hukuken yasaktır!");
        }
    });

    // Metin seçimini (selection) programatik olarak sıfırla
    document.addEventListener('selectstart', function(e) {
        e.preventDefault();
    });
</script>
""", unsafe_allow_html=True)

# ==========================================
# 2. DİL YÖNETİMİ VE SÖZLÜK
# ==========================================
if 'lang' not in st.session_state:
    st.session_state.lang = 'TR'

translations = {
    'TR': {
        "sidebar_menu": "🌐 Gezinti Menüsü",
        "menu_select": "Menü Seçimi",
        "menu_items": [
            "📖 Ayet-i Kerîmeler (15+)",
            "📜 Hadis-i Şerifler (15+)",
            "💡 Bediüzzaman & Risale-i Nur (15+)",
            "🎓 İslam Alimlerinin Görüşleri (15+)",
            "🔬 Bilimsel Araştırmalar (15+)"
        ],
        "sleep_info": "💡 **Not:** Bu web uygulaması ücretsiz sunucularda barındırılmaktadır. Uzun süre işlem yapılmadığında uygulama uyku moduna geçebilir.\n\n💤 Eğer böyle bir ekranla karşılaşırsanız, ekranda beliren mavi renkli *'Yes, get this app back up!'* butonuna tıklayın.",
        "header_ayet": ("KUR'AN-I KERİM'DEN ÂYET-İ KERÎMELER", "Atmosfer, Rüzgar, Hava Olayları ve Nur Hakikatine Dair 15+ Âyet"),
        "header_hadis": ("MUTEBER HADİS-İ ŞERİFLER", "Rüzgar, Hava, Işık ve Tabiat Olayları Hakkında 15+ Hadis"),
        "header_risale": ("BEDİÜZZAMAN SAİD NURSÎ HAZRETLERİNİN GÖRÜŞLERİ", "Hava, Işık, Zerrat ve Kainat Hakikatine Dair 15+ Analiz"),
        "header_scholar": ("İSLAM ALİMLERİNİN GÖRÜŞLERİ", "Klasik Tefsir, Felsefe ve Tasavvuf Literatüründen 15+ Alıntı"),
        "header_science": ("BİLİMSEL VE FİZİKSEL ARAŞTIRMALAR", "Modern Fizik, Optik, Termodinamik ve Meteoroloji Alanından 15+ Akademik Veri"),
        "legal_title": "⚖️ Kapsamlı Fikri Mülkiyet, Telif Hakları ve Yasal Sorumluluk Reddi (Legal Notice & Disclaimer)",
        "legal_p1": "**1. Yalnızca Bilgi Paylaşımı ve Manevi Gelişim Amaçlıdır:** Bu yazılım ve içerisindeki tüm akademik, dini ve bilimsel derlemeler yalnızca bireysel bilgi paylaşımı ve manevi gelişim amaçlı sunulmaktadır.",
        "legal_p2": "**2. Ticari Yasağı:** Bu yazılımın ve içerisindeki hiçbir verinin, metnin veya tasarımın **ticari olarak kullanılması, satılması, pazarlanması, bir ürün veya hizmete dönüştürülmesi kesinlikle yasaktır.** Ticari menfaat elde etmek amacıyla kullanılamaz.",
        "legal_p3": "**3. Başka Amaçlar İçin Kullanılamaz:** Uygulama içerisinde sunulan içerikler, belirtilen bilgi paylaşımı ve manevi gelişim amacı dışında hiçbir farklı amaç, ideoloji, analiz veya mecrada kullanılamaz.",
        "legal_p4": "**4. Kopyalama ve Aktarım Yasağı:** Güvenlik tedbirleri gereğince yazılım içerisindeki hiçbir bilgi, veri, alıntı veya kod satırı kopyalanamaz, başka bir ortama aktarılamaz ve tersine mühendisliğe tabi tutulamaz.",
        "legal_p5": "**5. Yazılım Geliştiricinin Sorumsuzluğu:** Bu yazılım ve içerisindeki tüm içerikler 'olduğu gibi' (as-is) sunulmaktadır. Yazılım geliştiricisi; uygulamanın kullanımından, içeriklerin yorumlanmasından veya bu verilerin dayanak gösterilmesi neticesinde kullanıcıların ya da üçüncü şahısların uğrayabileceği doğrudan veya dolaylı hiçbir maddi, manevi, hukuki ve cezai zarardan **kesinlikle sorumlu tutulamaz.** Tüm hakları saklıdır."
    },
    'EN': {
        "sidebar_menu": "🌐 Navigation Menu",
        "menu_select": "Select Menu",
        "menu_items": [
            "📖 Verses of the Quran (15+)",
            "📜 Authentic Hadiths (15+)",
            "💡 Bediuzzaman & Risale-i Nur (15+)",
            "🎓 Views of Islamic Scholars (15+)",
            "🔬 Scientific Researches (15+)"
        ],
        "sleep_info": "💡 **Note:** This web app is hosted on free servers. It may go to sleep after inactivity.\n\n💤 If you encounter such a screen, click the blue *'Yes, get this app back up!'* button.",
        "header_ayet": ("VERSES FROM THE QURAN", "15+ Verses on Atmosphere, Wind, Weather Events and Truth of Light"),
        "header_hadis": ("AUTHENTIC HADITHS", "15+ Hadiths on Wind, Air, Light and Nature Events"),
        "header_risale": ("VIEWS OF BEDIUZZAMAN SAID NURSI", "15+ Analyses on Air, Light, Particles and Universe"),
        "header_scholar": ("VIEWS OF ISLAMIC SCHOLARS", "15+ Quotes from Classical Tafsir, Philosophy and Sufism"),
        "header_science": ("SCIENTIFIC AND PHYSICAL RESEARCHES", "15+ Academic Data from Modern Physics, Optics, Thermodynamics and Meteorology"),
        "legal_title": "⚖️ Comprehensive Intellectual Property, Copyrights and Legal Disclaimer",
        "legal_p1": "**1. Purpose Limitation (Information Sharing & Spiritual Development Only):** This software and all academic, religious, and scientific compilations herein are provided solely for individual information sharing and spiritual development purposes.",
        "legal_p2": "**2. Prohibition of Commercial Use:** It is strictly prohibited to use, sell, market, or transform this software or any data, text, or design within it into a commercial product or service. It cannot be used for commercial gain.",
        "legal_p3": "**3. Restriction on Other Uses:** The contents presented within the application cannot be used for any other purpose, ideology, analysis, or medium outside the specified information-sharing and spiritual development goals.",
        "legal_p4": "**4. Copying and Transfer Prohibition:** Due to security measures, no information, data, quote, or code line within the software can be copied, transferred to another medium, or subjected to reverse engineering.",
        "legal_p5": "**5. Non-Liability of the Software Developer:** This software and all contents are provided 'as-is'. The software developer shall not be held strictly liable for any direct or indirect material, moral, legal, or penal damages incurred by users or third parties arising from the use of the application, interpretation of contents, or reliance on these data. All rights reserved."
    }
}

t = translations[st.session_state.lang]

# ==========================================
# 3. TAM 15+15+15+15+15 VERİ SETLERİ (TR / EN)
# ==========================================

AYETLER_DATA = [
    {
        "title": {
            'TR': "1. Rüzgarın Rahmet Müjdecisi Olarak Gönderilmesi",
            'EN': "1. Sending Winds as Harbingers of Mercy"
        },
        "arabic": "وَهُوَ الَّذِي يُرْسِلُ الرِّيَاحَ بُشْراً بَيْنَ يَدَيْ رَحْمَتِهِ",
        "meal": {
            'TR': "Rahmetinin (yağmurun) önünde rüzgarları müjdeci olarak gönderen O'dur.",
            'EN': "And He is the One who sends the winds as good tidings before His mercy."
        },
        "source": "A'râf Suresi, 57"
    },
    {
        "title": {
            'TR': "2. Nur ve Işık Hakikati (Nur Ayeti)",
            'EN': "2. The Reality of Light (Verse of Light)"
        },
        "arabic": "اللَّهُ نُورُ السَّمَاوَاتِ وَالأَرْضِ مَثَلُ نُورِهِ كَمِشْكَاةٍ فِيهَا مِصْبَاحٍ",
        "meal": {
            'TR': "Allah, göklerin ve yerin nurudur. O'nun nurunun temsili, içinde lamba bulunan bir kandillik gibidir...",
            'EN': "Allah is the Light of the heavens and the earth. The example of His light is like a niche within which is a lamp..."
        },
        "source": "Nûr Suresi, 35"
    },
    {
        "title": {
            'TR': "3. Rüzgarların Aşılayıcı ve Sevk Edici Özelliği",
            'EN': "3. Pollinating and Directing Feature of Winds"
        },
        "arabic": "وَأَرْسَلْنَا الرِّيَاحَ لَوَاقِحَ فَأَنْزَلْنَا مِنَ السَّمَاءِ مَاءً فَأَسْقَيْنَاكُمُوهُ",
        "meal": {
            'TR': "Biz, rüzgarları aşılayıcı olarak gönderdik de gökten su indirip onu size içirdik.",
            'EN': "And We have sent the fertilizing winds and sent down water from the sky and given you drink from it."
        },
        "source": "Hicr Suresi, 22"
    },
    {
        "title": {
            'TR': "4. Gündüzün Işığı ve Gece Karanlığının Yaratılması",
            'EN': "4. Creation of Daylight and Night Darkness"
        },
        "arabic": "وَجَعَلَ الظَّLُمَاتِ وَالنُّورَ",
        "meal": {
            'TR': "Karanlıkları ve nûru (ışığı) yaratan O'dur.",
            'EN': "And [who] made the darkness and the light."
        },
        "source": "En'âm Suresi, 1"
    },
    {
        "title": {
            'TR': "5. Göğün Açılması ve Bulutların Sevk Edilmesi",
            'EN': "5. Directing Clouds to Dead Lands"
        },
        "arabic": "وَاللَّهُ الَّذِي أَرْسَلَ الرِّيَاحَ فَتُثِيرُ سَحَاباً فَسُقْنَاهُ إِلَى بَلَدٍ مَّيِّتٍ",
        "meal": {
            'TR': "Rüzgarları gönderip bulutu kıpırdatan Allah'tır. Derken onu ölü bir beldeye sevk ederiz.",
            'EN': "It is Allah who sends the winds, and they stir the clouds and Drive them to a dead land."
        },
        "source": "Fâtır Suresi, 9"
    },
    {
        "title": {
            'TR': "6. Işığın Karanlıkları Delip Geçmesi",
            'EN': "6. Praise to Creator of Heavens and Earth"
        },
        "arabic": "قُلِ الْحَمْدُ لِلَّهِ الَّذِي خَلَقَ السَّمَاوَاتِ وَالأَرْضَ وَجَعَلَ الظَّLُمَاتِ وَالنُّورَ",
        "meal": {
            'TR': "Gökleri ve yeri yaratan, karanlıkları ve nûru var eden Allah'a hamdolsun.",
            'EN': "[All] praise is due to Allah , who created the heavens and the earth and made the darkness and the light."
        },
        "source": "En'âm Suresi, 1"
    },
    {
        "title": {
            'TR': "7. Rüzgarların Delil Olması ve Akledenler İçin İbret",
            'EN': "7. Signs in Winds and Clouds for Those Who Use Reason"
        },
        "arabic": "وَتْصْرِيفِ الرِّيَاحِ وَالسَّحَابِ الْمُسَخَّرِ بَيْنَ السَّمَاءِ وَالأَرْضِ لآيَاتٍ لِّقَوْمٍ يَعْقِلُونَ",
        "meal": {
            'TR': "Rüzgarların çevrilmesinde, gök ile yer arasında emre amade bekleyen bulutlarda akleden bir toplum için deliller vardır.",
            'EN': "And [in] the alternation of the winds and the clouds controlled between the heaven and the earth are signs for a people who use reason."
        },
        "source": "Bakara Suresi, 164"
    },
    {
        "title": {
            'TR': "8. Sabah Aydınlığı (Fellak) ve Işığın Yayılması",
            'EN': "8. Seeking Refuge in Lord of Daybreak"
        },
        "arabic": "قُلْ أَعُوذُ بِرَبِّ الْفَلَقِ",
        "meal": {
            'TR': "De ki: Sabahın (karanlığı yarıp ışığı çıkaranın) Rabbine sığınırım.",
            'EN': "Say, 'I seek refuge in the Lord of daybreak.'"
        },
        "source": "Felak Suresi, 1"
    },
    {
        "title": {
            'TR': "9. Kasırga ve Şiddetli Rüzgarın Kudret Delili Olması",
            'EN': "9. Protection Against Violent Wind Storms"
        },
        "arabic": "أَوْ أَرْسَلْنَا عَلَيْكُمْ حَاصِباً ثُمَّ لاَ تَجِدُوا لَكُمْ وَكِيلاً",
        "meal": {
            'TR': "Yahut üzerinize şiddetli rüzgar (kasırga) göndermeyeceğimizden emin misiniz? Sonra kendinize bir koruyucu bulamazsınız.",
            'EN': "Or do you feel secure that He will not send against you a storm of stones? Then you would not find for yourselves an advocate."
        },
        "source": "İsrâ Suresi, 68"
    },
    {
        "title": {
            'TR': "10. Güneş'in Ziya (Işık) ve Ay'ın Nur Kılınması",
            'EN': "10. Sun as Radiant Lamp and Moon as Light"
        },
        "arabic": "هُوَ الَّذِي جَعَلَ الشَّمْسَ ضِيَاءً وَالْقَمَرَ نُوراً",
        "meal": {
            'TR': "Güneşi bir ziya (aydınlık kaynak), ay'ı da bir nur kılan O'dur.",
            'EN': "It is He who made the sun a shining light and the moon a derived light."
        },
        "source": "Yûnus Suresi, 5"
    },
    {
        "title": {
            'TR': "11. Rüzgarın Gemileri Denizde Yüzdürmesi",
            'EN': "11. Winds as Bearers of Good Tidings"
        },
        "arabic": "وَمِنْ آيَاتِهِ أَنْ يُرْسِلَ الرِّيَاحَ مُبَشِّرَاتٍ",
        "meal": {
            'TR': "Rüzgarları müjdeciler olarak göndermesi O'nun delillerindendir.",
            'EN': "And of His signs is that He sends the winds as bringers of good tidings."
        },
        "source": "Rûm Suresi, 46"
    },
    {
        "title": {
            'TR': "12. Göğün Karanlıklarının Yıldız ve Işıklarla Donatılması",
            'EN': "12. Stars for Guidance in Darkness"
        },
        "arabic": "وَهُوَ الَّذِي جَعَلَ لَكُمُ النُّجُومَ لِتَهْتَدُوا بِهَا فِي ظُلُمَاتِ الْبَرِّ وَالْبَحْرِ",
        "meal": {
            'TR': "Karanlıklarda yollarınızı bulmanız için size yıldızları var eden O'dur.",
            'EN': "And it is He who placed for you the stars that you may be guided by them through the darknesses of the land and sea."
        },
        "source": "En'âm Suresi, 97"
    },
    {
        "title": {
            'TR': "13. Rüzgarın Allah'ın Emriyle Boyun Eğdirilmesi",
            'EN': "13. Wind Subjected to Prophet Solomon"
        },
        "arabic": "وَلِسُلَيْمَانَ الرِّيحَ عَاصِفَةً تَجْرِي بِأَمْرِهِ",
        "meal": {
            'TR': "Süleyman'a da şiddetli esen rüzgarı boyun eğdirdik; onun emriyle akar",
            'EN': "And to Solomon [We subjected] the wind, blowing forcefully, proceeding by his command."
        },
        "source": "Enbiyâ Suresi, 81"
    },
    {
        "title": {
            'TR': "14. Kuşluk Vakti ve Işığın Tezahürü",
            'EN': "14. Morning Brightness and Night"
        },
        "arabic": "وَالضُّحَى وَاللَّيْلِ إِذَا سَجَى",
        "meal": {
            'TR': "Andolsun kuşluk vaktine ve sükuta erdiğinde geceye ki...",
            'EN': "By the morning brightness and by the night when it covers with darkness..."
        },
        "source": "Duhâ Suresi, 1-2"
    },
    {
        "title": {
            'TR': "15. Havanın Genişletilmesi ve Göğün Kubbe Yapılması",
            'EN': "15. Construction and Expansion of Heaven"
        },
        "arabic": "وَالسَّمَاءَ بَنَيْنَاهَا بِأَيْدٍ وَإِنَّا لَمُوسِعُونَ",
        "meal": {
            'TR': "Göğü kudretimizle biz kurduk ve şüphesiz bizim onu genişletmeye gücümüz yeter.",
            'EN': "And the heaven We constructed with strength, and indeed, We are [its] expander."
        },
        "source": "Zâriyât Suresi, 47"
    }
]

HADITHS_DATA = [
    {
        "text": {
            'TR': "Rüzgar Allah'ın rahmetindendir; rahmet getirir veya azap getirir. Onu gördüğünüzde sövmeyin, Allah'tan hayrını isteyin ve şerrinden sığının.",
            'EN': "The wind is from the mercy of Allah; it brings mercy or torment. When you see it, do not revile it, ask Allah for its good and seek refuge in Him from its evil."
        },
        "source": "Ebû Dâvûd, Edeb 111"
    },
    {
        "text": {
            'TR': "Allah Teâlâ nurdur (göklerin ve yerin nurunu idare edendir). O'nun perdesi nurdur.",
            'EN': "Allah Almighty is Light (governing the light of heavens and earth). His veil is light."
        },
        "source": "Sahih-i Müslim, İman 293"
    },
    {
        "text": {
            'TR': "Rüzgar esdiği zaman Resulullah (s.a.v.) şöyle dua ederdi: 'Allah'ım, benden bunun hayrını, içindeki hayrın hayırlısını ve gönderildiğin şeyin hayırlısını isterim...'",
            'EN': "When the wind blew, the Prophet (PBUH) would pray: 'O Allah, I ask You for its good, the good within it, and the good with which it was sent...'"
        },
        "source": "Tirmizi, Daavât 80"
    },
    {
        "text": {
            'TR': "Şiddetli rüzgar esip fırtına çıktığı vakit Peygamberimiz'in yüzünün rengi değişir, endişeyle içeri dışarı yürürdü.",
            'EN': "When a violent wind and storm broke out, the color of the Prophet's face would change, and he would walk back and forth in anxiety."
        },
        "source": "Buhârî, Tehid 23"
    },
    {
        "text": {
            'TR': "Sabah namazından sonra güneş doğuncaya kadar oturmak, bana İsmail evladından dört köle azat etmekten daha sevgilidir.",
            'EN': "Sitting after the morning prayer until sunrise is more beloved to me than freeing four slaves from the children of Ismail."
        },
        "source": "Ebû Dâvûd, Edeb 112"
    },
    {
        "text": {
            'TR': "Yeryüzünü aydınlatan güneş ve ay, Allah'ın ayetlerindendir; hiç kimsenin ölümünden veya doğumundan dolayı tutulmazlar.",
            'EN': "The sun and moon illuminating the earth are signs of Allah; they do not eclipse for the death or birth of anyone."
        },
        "source": "Buhârî, Küsûf 1"
    },
    {
        "text": {
            'TR': "Sübhanallahi ve bi-hamdike zikri, gök ile yer arasındaki boşluğu (havayı) sevapla doldurur.",
            'EN': "The remembrance of 'Subhanallahi wa bi-hamdike' fills the space (air) between heaven and earth with reward."
        },
        "source": "Müslim, Zikir 32"
    },
    {
        "text": {
            'TR': "Müminin nuru, kalbindeki iman kadardır. Karanlık gecede parlayan yıldızlar gibi ehl-i cennet birbirini görür.",
            'EN': "The light of a believer is according to faith in their heart. The people of Paradise will see each other like shining stars in a dark night."
        },
        "source": "Tirmizi, Cennet 15"
    },
    {
        "text": {
            'TR': "Yeryüzünde Allah'ın rahmet eserlerine (rüzgara, yağmura, ışığa ve bitkilere) bakın; ölümden sonra yeryüzünü nasıl dirilttiğini görün.",
            'EN': "Look at the traces of Allah's mercy on earth (wind, rain, light, plants); see how He revives the earth after its death."
        },
        "source": "İbn Kesir Külliyatı"
    },
    {
        "text": {
            'TR': "İlim taleb etmek her Müslümana farzdır. İlim nurdur, cehalet ise karanlıktır.",
            'EN': "Seeking knowledge is an obligation upon every Muslim. Knowledge is light, and ignorance is darkness."
        },
        "source": "İbn Mâce, Mukaddime 17"
    },
    {
        "text": {
            'TR': "Gece namazı kılın, çünkü gece ibadeti sizden önceki salihlerin adeti, Allah'a yakınlık vesilesi ve günahlara kefarettir.",
            'EN': "Perform night prayer, for it is the habit of righteous people before you, a means of proximity to Allah, and expiation for sins."
        },
        "source": "Tirmizi, Daavât 101"
    },
    {
        "text": {
            'TR': "Allah, geceleyin elini gündüz günah işleyenin tevbe etmesi için uzatır; gündüz elini gece günah işleyenin tevbesi için uzatır.",
            'EN': "Allah extends His hand at night so that the sinner of the day may repent, and extends His hand by day so that the sinner of the night may repent."
        },
        "source": "Müslim, Tevbe 31"
    },
    {
        "text": {
            'TR': "Güzel ahlak, suyun buzu eritmesi gibi günahları eritir; kötü ahlak ise sirkenin balı bozduğu gibi ameli bozar.",
            'EN': "Good character melts sins just as water melts ice; bad character spoils deeds just as vinegar spoils honey."
        },
        "source": "Taberani, Mu'cemu'l-Evsat"
    },
    {
        "text": {
            'TR': "İnsanın bedeninde üç yüz altmış eklem vardır; her gün bunların her biri için bir sadaka vermesi gerekir.",
            'EN': "There are three hundred and sixty joints in the human body; charity is required for each of them every day."
        },
        "source": "Müslim, Zekât 52"
    },
    {
        "text": {
            'TR': "Kıyamet gününde müminlerin önlerinde ve sağlarında nurları parlayacak, 'Bugün müjdeniz altından ırmaklar akan cennetlerdir' denilecek.",
            'EN': "On the Day of Judgment, the light of believers will shine before and to their right. It will be said, 'Your glad tidings today are gardens beneath which rivers flow.'"
        },
        "source": "Ahmed bin Hanbel, Müsned"
    }
]

RISALE_DATA = [
    {
        "title": {
            'TR': "1. Havanın Mucizevi Telefon ve Telgraf Vazifesi (Hüve Nüktesi)",
            'EN': "1. The Miraculous Telephone and Telegraph Duty of Air"
        },
        "text": {
            'TR': "Hava zerreleri şuursuz olduğu halde, milyarlarca farklı telefon sesini, radyo dalgasını ve kokuyu birbirine karıştırmadan aynı anda nakletmesi ilahi ilmin delilidir.",
            'EN': "Although air particles are unconscious, transmitting billions of different telephone sounds and radio waves simultaneously without mixing them is proof of divine knowledge."
        },
        "source": "30. Söz (Hüve Nüktesi)"
    },
    {
        "title": {
            'TR': "2. Işığın ve Nurun Kâinatı Donatması",
            'EN': "2. Light Adorning the Universe"
        },
        "text": {
            'TR': "Işık, Esma-i İlahiyyenin en parlak aynasıdır. Karanlıkları anında delip geçmesi, kâinatı bir anda şeffaf bir kitap haline getirmesidir.",
            'EN': "Light is the brightest mirror of Divine Names. Piercing the darkness instantly turns the universe into a transparent book."
        },
        "source": "33. Söz (Pencereler Risalesi)"
    },
    {
        "title": {
            'TR': "3. Nefes Alıp Vermede İlahi Rahimiyet",
            'EN': "3. Divine Mercy in Breathing"
        },
        "text": {
            'TR': "Havanın mahlukata tazyik edilmeden, musluk gibi en uzak ve dar yerlere kadar yetiştirilmesi Rahman'ın rahmetini gösterir.",
            'EN': "Delivering air to creatures like a tap into the most distant and narrow places without oppression shows the boundless mercy of the All-Merciful."
        },
        "source": "23. Söz"
    },
    {
        "title": {
            'TR': "4. Nurun Hakikati ve Zülal-i Hidayet",
            'EN': "4. The Reality of Light and Guidance"
        },
        "text": {
            'TR': "Nur, hem bir vücut vasıtası hem de mevcudatın mahiyetini gösteren bir keşif aletidir. Işık olmasa kâinat adem zindanında kalırdı.",
            'EN': "Light is both a medium of existence and a discovery tool showing the essence of beings. Without light, the universe would remain in the dungeon of non-existence."
        },
        "source": "1. Lem'a"
    },
    {
        "title": {
            'TR': "5. Rüzgarın Esmesindeki İlahi Tasarruf",
            'EN': "5. Divine Governance in Blowing Winds"
        },
        "text": {
            'TR': "Rüzgar ilahi kudretin kalemidir; seyyar bir mektup taşıyıcısı gibi bulutları sevk eder, nebatatın aşılanmasını sağlar.",
            'EN': "Wind is the pen of divine power; like a mobile letter carrier, it drives clouds and ensures pollination of plants."
        },
        "source": "22. Söz"
    },
    {
        "title": {
            'TR': "6. Zerratın Hareketlerinde İlim ve İrade",
            'EN': "6. Knowledge and Will in Particle Movements"
        },
        "text": {
            'TR': "Hava zerratının her birinin, her kelimeyi ve sesi tanıyıp nakletmesi ancak ezelî bir ilmin komutuyla mümkündür.",
            'EN': "The fact that each air particle recognizes and transmits every word and sound is only possible by the command of eternal knowledge."
        },
        "source": "20. Söz"
    },
    {
        "title": {
            'TR': "7. Göğün Yüzünün Temizlenmesi ve Hava Sirkülasyonu",
            'EN': "7. Cleaning of the Sky and Air Circulation"
        },
        "text": {
            'TR': "Milyonlarca mahlukun teneffüs ettiği havanın zehirlenmeyip daima tazelenmesi büyük bir mutfak ve temizlik hikmetini gösterir.",
            'EN': "The air breathed by millions not being poisoned and constantly refreshed shows great wisdom of cleanliness."
        },
        "source": "Asâ-yı Musa"
    },
    {
        "title": {
            'TR': "8. Güneş'in Bir Lamba Gibi Kullanılması",
            'EN': "8. The Sun Used as a Cosmic Lamp"
        },
        "text": {
            'TR': "Güneş, sema sarayında intizamla çalıştırılan muazzam bir lâmba ve sobodur; hem ışık hem hararet neşreder.",
            'EN': "The sun is a magnificent lamp and stove operated regularly in the heavenly palace; it radiates both light and heat."
        },
        "source": "32. Söz"
    },
    {
        "title": {
            'TR': "9. Seslerin Havada Kaybolmayıp Saklanması",
            'EN': "9. Preservation of Sounds in Air"
        },
        "text": {
            'TR': "Havada yayılan seslerin ve manzaraların levh-i mahfuz gibi muhafaza edilmesi hafıza-i kübranın varlığına delildir.",
            'EN': "The preservation of sounds and views spreading in the air like a preserved tablet is proof of the Supreme Memory."
        },
        "source": "İşaratü'l-İ'câz"
    },
    {
        "title": {
            'TR': "10. Renklerin Çeşitliliği ve Işığın Kırılması",
            'EN': "10. Diversity of Colors and Refraction of Light"
        },
        "text": {
            'TR': "Işığın prizmadan geçerek renk renge bürünmesi Sani-i Zülcelal'in mütenevvi nakışlarının bir tezahürüdür.",
            'EN': "Light turning into various colors through a prism is a manifestation of the diverse embroideries of the Maker."
        },
        "source": "29. Söz"
    },
    {
        "title": {
            'TR': "11. Atmosferin Basınç Kanunu ve İlahi Ölçü",
            'EN': "11. Atmospheric Pressure Law and Divine Measure"
        },
        "text": {
            'TR': "Havanın ağırlığı ve uyguladığı basınç, nebatatın ve insanların hayatını idame ettirecek kusursuz bir mizan üzerindedir.",
            'EN': "The weight and pressure of air are on a flawless balance to sustain the lives of plants and humans."
        },
        "source": "Mektubat"
    },
    {
        "title": {
            'TR': "12. Havanın Şeffaflığı ve İnsan Gözünün İmtihanı",
            'EN': "12. Transparency of Air and Human Test"
        },
        "text": {
            'TR': "Havanın görünmez ve şeffaf olması, arkasındaki muazzam mucizelerin tefekkür edilmesini sağlayan bir imtihan perdesidir.",
            'EN': "The invisibility and transparency of air serve as a test veil enabling contemplation of miracles behind it."
        },
        "source": "Mesnevî-i Nuriye"
    },
    {
        "title": {
            'TR': "13. Işığın Hızındaki İlahi İntizam",
            'EN': "13. Divine Order in the Speed of Light"
        },
        "text": {
            'TR': "Işığın saniyede 300 bin km hızla hareket etmesi, kâinatın zerratından seyyaratına kadar her yerin anında aydınlatılması hikmetinedir.",
            'EN': "Light traveling at 300,000 km per second serves the wisdom of instantly illuminating everywhere from particles to planets."
        },
        "source": "Şualar"
    },
    {
        "title": {
            'TR': "14. Rüzgarın Soğukluk ve Sıcaklık Dengesini Kurması",
            'EN': "14. Wind Balancing Temperature"
        },
        "text": {
            'TR': "Mevsimlerin değişmesi ve rüzgarların tasallutu ile yeryüzünün musluklarının açılıp kapanması ilahi bir tedbirdir.",
            'EN': "The changing of seasons and opening/closing of earthly taps through winds is a divine precaution."
        },
        "source": "Barla Lahikası"
    },
    {
        "title": {
            'TR': "15. Havada Oksijen ve Azotun Hassas Oranı",
            'EN': "15. Precise Ratio of Oxygen and Nitrogen in Air"
        },
        "text": {
            'TR': "%21 oksijen ve %78 azot dengesinin bir zerre bile şaşmaması, mutlak bir hakimiyetin ve adaletli bir tanzimin eseridir.",
            'EN': "The balance of 21% oxygen and 78% nitrogen not shifting even a particle is the work of absolute dominion and just arrangement."
        },
        "source": "Kastamonu Lahikası"
    }
]

SCHOLARS_DATA = [
    {
        "scholar": "İmam Gazâlî (r.a.)",
        "view": {
            'TR': "Işık (Nur), zihinsel ve fiziksel idrakin vasıtasıdır. Kalp gözü de ilahi nur ile hakikatleri idrak eder.",
            'EN': "Light is the medium of mental and physical perception. The eye of the heart perceives truths through divine light."
        }
    },
    {
        "scholar": "Fahreddin er-Râzî (r.a.)",
        "view": {
            'TR': "Rüzgarın esişindeki mükemmel intizam ve havanın canlılarca teneffüs edilmek üzere sunulması uluhiyetin en büyük delillerindendir.",
            'EN': "The perfect order in winds and air provided for breathing are among the greatest proofs of divinity."
        }
    },
    {
        "scholar": "İbn Rüşd",
        "view": {
            'TR': "Işığın cisimler üzerindeki etkisi ve havada yayılma karakteri, faal aklın kâinatı aydınlatma biçiminin fiziksel yansımasıdır.",
            'EN': "The effect of light on bodies and its spread in air are physical reflections of active intellect illuminating the universe."
        }
    },
    {
        "scholar": "İbn Sina",
        "view": {
            'TR': "Hava, ses dalgalarını ve ısıyı iletme kabiliyetiyle cismani âlemin en latif ve hayatî unsurlarından biridir.",
            'EN': "Air is one of the most subtle and vital elements of the corporeal world with its ability to conduct sound waves and heat."
        }
    },
    {
        "scholar": "Gazâlî (Mişkâtü'l-Envar)",
        "view": {
            'TR': "Hakiki nur, zâtı ile zahir olan ve her şeyi zahir kılan Cenab-ı Hak'tır. Güneş ve yıldızlar birer mecazi nur gölgesidir.",
            'EN': "The true light is Allah, who is manifest by His essence and makes everything manifest. Sun and stars are metaphorical shadows."
        }
    },
    {
        "scholar": "İbnü'l-Arabi",
        "view": {
            'TR': "Rüzgar (Rîh), esma-i ilahiyyenin celal ve cemal tecellilerini yeryüzüne taşıyan ilahi bir nefestir.",
            'EN': "The wind is a divine breath carrying the manifestations of divine names to the earth."
        }
    },
    {
        "scholar": "Celâleddîn-i Rûmî",
        "view": {
            'TR': "Hava aşıkların ruhuna benzer; gözle görülmez ama her an varlığıyla hayat verir.",
            'EN': "Air resembles the soul of lovers; it is invisible, but gives life with its presence every moment."
        }
    },
    {
        "scholar": "İmam Mâtürîdî",
        "view": {
            'TR': "Atmosferdeki gazların ve rüzgarların nizamı, tesadüfe asla ihtimal vermeyen hikmetli bir yaratılışın kanıtıdır.",
            'EN': "The order of gases and winds in the atmosphere is proof of a wise creation that leaves no room for coincidence."
        }
    },
    {
        "scholar": "Taftazânî",
        "view": {
            'TR': "Havanın esnekliği ve sıkıştırılabilir yapısı, insan hayatının konforu için özel olarak tasarlanmıştır.",
            'EN': "The flexibility and compressible structure of air are specially designed for human comfort."
        }
    },
    {
        "scholar": "İbn Kayyım el-Cevziyye",
        "view": {
            'TR': "Rüzgarlar bazen rahmet müjdecisi, bazen ilahi ikaz aracıdır; her esişinde hikmetler gizlidir.",
            'EN': "Winds are sometimes harbingers of mercy and sometimes divine warnings; wisdom is hidden in every blow."
        }
    },
    {
        "scholar": "Şah Veliyullah Dehlevî",
        "view": {
            'TR': "Kâinattaki nur ve karanlık mücadelesi, ruhani alemin maddî dünyadaki en açık tecellisidir.",
            'EN': "The struggle between light and darkness in the universe is the clearest manifestation of the spiritual realm."
        }
    },
    {
        "scholar": "Ali el-Kârî",
        "view": {
            'TR': "Rüzgara sövülmemesi emri, arkasındaki ilahi iradeye ve tasarrufa saygının gereğidir.",
            'EN': "The command not to revile the wind is a requirement of respect for the divine will behind it."
        }
    },
    {
        "scholar": "İmam Suyûtî",
        "view": {
            'TR': "Ayetlerde geçen rüzgar tasvirleri, insanlara sığınacak tek makamın Yaratıcı olduğunu hatırlatır.",
            'EN': "Wind descriptions in verses remind people that the only refuge is the Creator."
        }
    },
    {
        "scholar": "İbn Haldûn",
        "view": {
            'TR': "İklimlerin ve hava şartlarının oluşumunda rüzgarların rolü, medeniyetlerin coğrafi kaderini belirler.",
            'EN': "The role of winds in climate formation determines the geographical destiny of civilizations."
        }
    },
    {
        "scholar": "Beyzâvî",
        "view": {
            'TR': "Nur ayetindeki kandil ve lamba temsili, insan kalbindeki ilahi idrakin meşalesini simgeler.",
            'EN': "The lamp representation in the Verse of Light symbolizes the torch of divine perception in human heart."
        }
    }
]

SCIENCE_DATA = [
    {
        "title": {
            'TR': "1. Troposfer ve Atmosferik Basınç Gradyanı",
            'EN': "1. Troposphere and Atmospheric Pressure Gradient"
        },
        "desc": {
            'TR': "Atmosfer kütlesinin %75-80'ini barındıran troposfer tabakası, dikey sıcaklık düşüşü ve barometrik basınç dengesi sayesinde iklim döngülerini stabilize eder.",
            'EN': "The troposphere layer containing 75-80% of atmospheric mass stabilizes climate cycles through temperature lapse rate and barometric balance."
        }
    },
    {
        "title": {
            'TR': "2. Elektromanyetik Spektrum ve Maxwell Denklemleri",
            'EN': "2. Electromagnetic Spectrum and Maxwell Equations"
        },
        "desc": {
            'TR': "Işık, Maxwell denklemleriyle formüle edilen salınan elektrik ve manyetik alan vektörleri vasıtasıyla uzayda enerji ve bilgi transferi yapar.",
            'EN': "Light transfers energy and information across space via oscillating electric and magnetic field vectors formulated by Maxwell equations."
        }
    },
    {
        "title": {
            'TR': "3. Biyo-Jeokimyasal Gaz Dengesi ve Termodinamik",
            'EN': "3. Biogeochemical Gas Balance and Thermodynamics"
        },
        "desc": {
            'TR': "Atmosferdeki %21 Oksijen ve %78 Azot oranlarının fotosentez döngüleriyle sabit kalması termodinamiğin optimizasyonudur.",
            'EN': "The constancy of 21% Oxygen and 78% Nitrogen ratios via photosynthesis cycles is an optimization of open system thermodynamics."
        }
    },
    {
        "title": {
            'TR': "4. Akustik Dalga Yayılımı ve Boyuna Dalgalar",
            'EN': "4. Acoustic Wave Propagation and Longitudinal Waves"
        },
        "desc": {
            'TR': "Ses dalgaları, hava moleküllerinin elastik özellikleri aracılığıyla boyuna dalgalar halinde yaklaşık 343 m/s hızla yayılır.",
            'EN': "Sound waves propagate as longitudinal waves through air molecules' elastic properties at approximately 343 m/s."
        }
    },
    {
        "title": {
            'TR': "5. Kuantum Optiği ve Fotonik Dalga-Parçacık İkiliği",
            'EN': "5. Quantum Optics and Wave-Particle Duality"
        },
        "desc": {
            'TR': "Işığın hem dalga hem de kesikli enerji paketleri (fotonlar) karakteri göstermesi kuantum mekaniğinin temelidir.",
            'EN': "Light exhibiting both wave and discrete energy packets (photons) character is the foundation of quantum mechanics."
        }
    },
    {
        "title": {
            'TR': "6. Coriolis Kuvveti ve Küresel Dolaşım",
            'EN': "6. Coriolis Force and Global Circulation"
        },
        "desc": {
            'TR': "Dünya'nın dönme eylemsizliğinden kaynaklanan Coriolis etkisi, rüzgar akışlarını sapmaya uğratarak iklim kuşaklarını biçimlendirir.",
            'EN': "The Coriolis effect due to Earth's rotation deflects wind flows, shaping atmospheric pressure cells and climate zones."
        }
    },
    {
        "title": {
            'TR': "7. Stratosferik Ozon Absorpsiyon Spektrumu",
            'EN': "7. Stratospheric Ozone Absorption Spectrum"
        },
        "desc": {
            'TR': "Stratosferdeki ozon molekülleri, Güneş'ten gelen zararlı UV-B ve UV-C radyasyon fotonlarını emerek yeryüzünü korur.",
            'EN': "Ozone molecules in the stratosphere protect Earth by absorbing harmful UV-B and UV-C radiation photons from the Sun."
        }
    },
    {
        "title": {
            'TR': "8. Rayleigh Saçılması ve Optik Spektrum",
            'EN': "8. Rayleigh Scattering and Optical Spectrum"
        },
        "desc": {
            'TR': "Güneş ışığının gaz moleküllerinden dalga boylarına ters orantılı saçılması mavi rengin gökyüzünde yayılmasına neden olur.",
            'EN': "Sunlight scattering inversely proportional to wavelengths from gas molecules causes blue color to spread across the sky."
        }
    },
    {
        "title": {
            'TR': "9. Doğal Sera Etkisi ve Gezegensel Işıncıl Denge",
            'EN': "9. Natural Greenhouse Effect and Radiative Balance"
        },
        "desc": {
            'TR': "Atmosferdeki su buharı ve $CO_2$ gibi gazlar yeryüzünden yansıyan kızılötesi radyasyonu tutarak sıcaklığı 15°C'de tutar.",
            'EN': "Gases like water vapor and $CO_2$ trap infrared radiation reflected from Earth, keeping the average temperature at 15°C."
        }
    },
    {
        "title": {
            'TR': "10. Fotosentetik Kuantum Dönüşümü (Z-Şeması)",
            'EN': "10. Photosynthetic Quantum Conversion"
        },
        "desc": {
            'TR': "Bitkiler klorofil pigmentleriyle solar foton enerjisini soğurarak kimyasal enerjiye dönüştürür ve besin zincirini kurar.",
            'EN': "Plants convert solar photon energy into chemical energy via chlorophyll pigments, establishing the food chain."
        }
    },
    {
        "title": {
            'TR': "11. Üst Troposfer Jet Akıntıları",
            'EN': "11. Upper Troposphere Jet Streams"
        },
        "desc": {
            'TR': "Tropopoz seviyesinde saatte 400+ km hıza erişebilen yüksek hızlı rüzgar nehirleri küresel hava kütlelerini taşır.",
            'EN': "High-speed wind rivers reaching 400+ km/h at the tropopause level transport global air masses."
        }
    },
    {
        "title": {
            'TR': "12. Hidrolojik Döngü ve Gizli Isı",
            'EN': "12. Hydrological Cycle and Latent Heat"
        },
        "desc": {
            'TR': "Havanın nem taşıma kapasitesi ve suyun gizli ısı kapasitesi okyanuslar ile karalar arasında devasa enerji pompasıdır.",
            'EN': "Air's moisture capacity and water's latent heat capacity act as a massive thermal energy pump between oceans and land."
        }
    },
    {
        "title": {
            'TR': "13. Moleküler Termal İletkenlik ve Yalıtım",
            'EN': "13. Molecular Thermal Conductivity and Insulation"
        },
        "desc": {
            'TR': "Kuru havanın termal iletkenliğinin düşük olması yalıtım malzemelerinin yüksek ısı yalıtımı sağlamasına imkan tanır.",
            'EN': "The low thermal conductivity of dry air enables insulation materials to provide high thermal insulation performance."
        }
    },
    {
        "title": {
            'TR': "14. İyonosferik Plazma ve Radyo Propagasyonu",
            'EN': "14. Ionospheric Plasma and Radio Propagation"
        },
        "desc": {
            'TR': "Üst atmosferdeki iyonize tabakalar radyo dalgalarını yansıtarak kıtalararası elektromanyetik iletişimi mümkün kılar.",
            'EN': "Ionized layers in the upper atmosphere reflect radio waves, enabling global intercontinental electromagnetic communication."
        }
    },
    {
        "title": {
            'TR': "15. Aerodinamik Kaldırma ve Akışkanlar Mekaniği",
            'EN': "15. Aerodynamic Lift and Fluid Mechanics"
        },
        "desc": {
            'TR': "Bernoulli prensibi ve Navier-Stokes denklemleri çerçevesinde hava akışkanlığının yarattığı basınç farkı kaldırma kuvvetini doğurur.",
            'EN': "Pressure differences created by airflow under Bernoulli's principle and Navier-Stokes equations generate aerodynamic lift."
        }
    }
]

# ==========================================
# 4. KENAR ÇUBUĞU (DİL SEÇİMİ)
# ==========================================
st.sidebar.markdown("### 🌐 Dil Seçimi / Language")
col_l1, col_l2 = st.sidebar.columns(2)
with col_l1:
    if st.button("🇹🇷 Türkçe", use_container_width=True):
        st.session_state.lang = 'TR'
        st.rerun()
with col_l2:
    if st.button("🇬🇧 English", use_container_width=True):
        st.session_state.lang = 'EN'
        st.rerun()

st.sidebar.markdown("---")
st.sidebar.title(t["sidebar_menu"])

menu = st.sidebar.radio(
    t["menu_select"],
    t["menu_items"]
)

st.sidebar.markdown("---")
st.sidebar.info(t["sleep_info"])

lang_key = st.session_state.lang

# ==========================================
# 5. İÇERİK GÖSTERİMİ (DİNAMİK ÇEVİRİ İLE)
# ==========================================
if "Ayet" in menu or "Verses" in menu:
    title, desc = t["header_ayet"]
    st.markdown(f'<div class="main-header"><h1>{title}</h1><p>{desc}</p></div>', unsafe_allow_html=True)

    for item in AYETLER_DATA:
        st.markdown(f"""
        <div class="card-box">
            <h4>📌 {item['title'][lang_key]}</h4>
            <div class="arabic-text">{item['arabic']}</div>
            <p style="font-size:1.1rem; color:#1E293B;">"{item['meal'][lang_key]}"</p>
            <span class="source-badge">📖 {item['source']}</span>
        </div>
        """, unsafe_allow_html=True)

elif "Hadis" in menu or "Hadiths" in menu:
    title, desc = t["header_hadis"]
    st.markdown(f'<div class="main-header"><h1>{title}</h1><p>{desc}</p></div>', unsafe_allow_html=True)

    for item in HADITHS_DATA:
        st.markdown(f"""
        <div class="card-box">
            <div class="quote-box">"{item['text'][lang_key]}"</div>
            <span class="source-badge">📜 {item['source']}</span>
        </div>
        """, unsafe_allow_html=True)

elif "Bediüzzaman" in menu or "Bediuzzaman" in menu:
    title, desc = t["header_risale"]
    st.markdown(f'<div class="main-header"><h1>{title}</h1><p>{desc}</p></div>', unsafe_allow_html=True)

    for item in RISALE_DATA:
        st.markdown(f"""
        <div class="card-box">
            <h3>{item['title'][lang_key]}</h3>
            <div class="quote-box">"{item['text'][lang_key]}"</div>
            <span class="source-badge">📖 {item['source']}</span>
        </div>
        """, unsafe_allow_html=True)

elif "Alim" in menu or "Scholars" in menu:
    title, desc = t["header_scholar"]
    st.markdown(f'<div class="main-header"><h1>{title}</h1><p>{desc}</p></div>', unsafe_allow_html=True)

    for sch in SCHOLARS_DATA:
        st.markdown(f"""
        <div class="card-box">
            <h3>👤 {sch['scholar']}</h3>
            <div class="quote-box">"{sch['view'][lang_key]}"</div>
            <span class="source-badge">📚 İslami İlimler Külliyatı / Islamic Sciences</span>
        </div>
        """, unsafe_allow_html=True)

elif "Bilimsel" in menu or "Scientific" in menu:
    title, desc = t["header_science"]
    st.markdown(f'<div class="main-header"><h1>{title}</h1><p>{desc}</p></div>', unsafe_allow_html=True)

    for sci in SCIENCE_DATA:
        st.markdown(f"""
        <div class="card-box">
            <h3>🔬 {sci['title'][lang_key]}</h3>
            <div class="science-box">{sci['desc'][lang_key]}</div>
            <span class="source-badge">🧪 Modern Fizik ve Meteoroloji / Modern Physics & Meteorology</span>
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# 6. KAPSAMLI YASAL UYARI VE TELİF BÖLÜMÜ
# ==========================================
st.markdown(f"""
<div class="legal-box">
    <h3>{t["legal_title"]}</h3>
    <p>{t["legal_p1"]}</p>
    <p>{t["legal_p2"]}</p>
    <p>{t["legal_p3"]}</p>
    <p>{t["legal_p4"]}</p>
    <p>{t["legal_p5"]}</p>
</div>
""", unsafe_allow_html=True)

st.markdown("<p style='text-align: center; color: #64748B; font-weight:600;'>Hazırlayan: Geliştirici | Hava, Işık ve Hikmet Portalı</p>", unsafe_allow_html=True)