import random

greetings = ["""안녕하세요 : 'an-nyeong-ha-se-yo'
안녕 : 'ahn-nyeong' (Korean)""",
"Aloha, “peace” : (Hawaiian)",
"sälem, Сәлем (casual), sälemetsiz be (formal), assalamu aleikum [When greeted first, the response should follow: wa aleikum ssselam] : (Kazakhstan)",
"שלום : shalom  (Hebrew)",
"אַ גוטן טאָג : a gutn tog, sholem-aleykhem, aleykhem-sholem (Yiddish)",
"Bonjour, salut, allô (phone), coucou (informal), Ça va? (French)",
"Dia dhuit : 'God be with you' (Gaelic)",
"haló (Scottish Gaelic)",
"Helô, haia, shwmae, sut mae, diolch (Welsh)",
"hola (Catalan)",
"Ciao, buon giorno, pronto (phone), salve (Italian)",
"Goede dag  (Dutch)",
"olá, oi, bom dia (Portuguese)",
"God dag  (Swedish)",
"Bună ziua (Romanian)",
"Guten tag, tag, hallo, alles klar, Moin: (Northern), (German)",

"བཀྲ་ཤིས་བདེ་ལེགས : 'tashi delek' “blessings and good luck” (Tibetan)",
"你好 : 'nǐ hǎo' : “you well”  (Mandarin)",
"नमस्ते : 'namaste'; “bow to you”  (Hindi)",
"""こんにちは : 'konnichiwa'
(tel) もしもし : 'moshi moshi'
"お会いできて光栄です : 'O-ai dekite kouei desu'
いかがお過ごしでした : 'Ikaga o-sugoshi deshita ka' (formal)
(日本語 : Japan)""",
"မင်္ဂလာပါ။ : 'mingalaba' “It is a blessing”  (Burmese)",
"สวัสดี : 'sàwàtdee'; from Sanskrit “swasti:” “good,” “auspicious”  (Thai)",

"здравствуйте : 'zdrastvuytye' zdorovo, привет 'privet' hey/hi, Алло allo, (Russian)",
"'zdravei' : single, Здравейте (formal, group) : 'zdraveĭte' (Bulgarian)",
"Tere or Tervist : versatile greeting “terve” (Estonian)",
"halló 'hal-law;' hæ 'haic;' góðan dag 'gothan dahg;' Komdu sæll 'come happy;' informal : (f) Sæl 'Sigh-l.' (m) Sæll 'Sight-l.'  (Icelandic)",

"السلام عليكم : 'al salaam aliykhum'  مرحبا : 'mar haba' ((العربية) Arabic)",
"سلام : cалам, salam əleyküm : 'sa-laam-mu-alaikum'  (Azerbaijan)",
"Ассаламу Iалайкум or Салам : 'assalamu aliykhum' or salam (Chechen)",

"Kia ora : “Be healthy” (Maori)",
"Talofa (Samoan)",
"ສະບາຍດີ : 'sabǎai děe' “you well” (Laos)",
"Bula : “Life” or “Alive” 	(Fijian)",

"Hujambo or jambo, Habri gani 'what is the news?'' (Swahili)",
"Aaniin : “what” or “how”  (Ojibwe)",
"hallo : (Afrikaans)",

"Lumela : for “believe” or “agree”	(Sesotho)",
"გამარჯობა : 'gah-mahr-joh-bah' მიესალმები : 'miesalmebi' “Victory” (Georgian)",
"Sawubona : “We see you”  (Zulu)",
"Mogethin : “Say a word”  (Yapese)",
"Ahoj, dobrý deň (Slovakia, Czech)",
"Zdravo, živjo 'ZHEE-vyoh' (Slovenian)",

"ጤና ይስጥል : Teanastëllën, 'teen-as-tell-an' (Amharic: Ethiopia, Egypt, Eritria, Israel)",
"barev dzez : 'bah-REV DZEZ' (Armenian)",
"kaixo : 'kai-show,' morning: egun on, night: gau on (Basque)",
"servus, seavus : '-vOOS;' grüß Gott (formal) : 'gruess got' (Bavarian, Austrian)",
"biтаю : 'vee-tie-you' (Belarusian)",
"নমস্কার : 'Nomoshkaar /Namaskāra' (Bengali)",
"wai, oi, oye : (बर’/बड़ Bodo: Bodoland, Assam, NE India, Nepal, Bengal)",
"dobar dan : 'DOH-bahr dahn' zdravo : 'ZDRAH-voh' (Bosnian)",

"demat (Breton)",
"Здраво : 'zdravo,' ćao : 'chow' (Serbian)",

"ជំរាបសួរ, chum reap suor, sous-dey (informal) : (Cambodian Khmer)",
"moni moni onse 'mooni-mooni-on-se' (general), moni mayi (f), moni bambo (m) : (Chichewa : Malawi; S SE E Africa)",

"你好 'néih hóu' (Cantonese)",
"bonghjornu 'bwohn JOHR-noh' (Corsican)",
"bok 'bohk,' dobar dan (Croatian)",
"hallo, goedendag, hoi (Dutch)",
"kuzu-zangpo la 'koo-zoo-zang-poh-la' (Dzongkha, Kingdom of Bhutan)",
"سلام  Salām, درود بر تو  Dorood bar to, درود بر شما  Dorood bar shoma, 'Dravat' - health (Farsi, Avestan)",
"bula, 'mbula' (Fijian)",
"hyvää päivää (HUU-vaa PAI-vaah) – good day : hei (hay) — informal hey : terve (TEHR-ve) — informal hello : moi (Moy) — informal hey : (Finnish)",
"goeie 'GOO-ee' : (Frisian)",
"xαίρε 'chai-ray' hi, yassas 'YAH sahss' γεια σας (formal) “health to you,” yassou 'YAH soo' γεια σου (informal) : (Greek)",
"namaskaar, namaste 'nah-mah-steh' : kem cho 'kem-choh' (Gujarat)",
"alo, bonjou 'BOH-joo' (formal), sak pase 'sak-pase' (informal) '"'what''s up'"' : (Kreyòl ayisyen, Haitian Creole)",
"sannu 'san-NU' (Hausa: W Chadic, West and Central Africa; Nigeria, Niger, Benin, Burkina Faso, Cameroon, C.A.R., Chad, Congo, Eritrea, Germany, Ghana, Sudan, Togo)"
"shalom, ma korae (informal greeting) (Hebrew)",
"nyob zoo (Hmong)",
"ha'u, 'hah-uh' : waynuma (Hopi, Uto-Aztec, AZ)",
"jó napot (yoe naupote), szervusz (SEHR-voos), szia (SEE-ah) : (Hungarian)",
"halo, hai (Indonsian Bahasa)",
"ᐊᐃᓐᖓᐃ : '"'Ainngai'"' (Inuktitut Eskimo-Aleut)",
"ನಮಸ್ಕಾರ : '"'Namaskār'"'   dhanyavāda ಧನ್ಯವಾದ (Kannada : Dravidian, Karnataka, SW India; Maharashtra, Andhra Pradesh, Tamil Nadu, Telangana, Kerala)",
"silav (slaw), as-salaamu’ alaykum (Kurdish)",
"salamatsyzby 'sah-lam-aht-seez-bee' - formal, salam 'sah-lam' - casual (Kyrgyz: Kipchak; China, Tajikstan)",
"ສະບາຍດີ 'sa-baai-di' (Lao)",
"Salve 'sal-way,' Salvete 'sal-way-tay' (assembly) : (Latin)",
"sveiks 'SVEH-eeks' (f to m), sveiki 'SVYEH-kah' (m to f) : (Latviešu Valoda: Latvian)",
"hallau, hoi, daag (Limburgish, Netherlands, Belgium)",
"mbote (mboh-teh) : (Lingala, DRC)"
"sveiki 'SVEH-kii' (to m), sveika 'SVYEH-kah' (to f), laba diena 'good day' (Lithuanian)",
"moïen 'MOY-en' (Luxembourg)",
"ki kati 'chi kati' (informal), oli otya to one person, muli mutya to a group (Luganda: Kampala, Bantu)",
"Tālofa (Tuvalu)",
"Talofa (Samoan)",
"Здраво 'zdravo', Добар ден 'dobar den' (Macedonian)",
"salama manao ahoana : (Malagasy: Madagascar)",
"hello, hai, selamat tengahari (good afternoon), selamat pagi 'suh-lah-mat puh-guee' (good morning) : (Malay: Bahasa Melayu: Malaysia, Brunei, +)",
"halēā, namaskkaram 'nah-mah-skahr-ahm' (ംമലയാള Malayalam)",
"bongu, 'Ħelow' : (Maltese)",
"namaskār (नमस्कार Marathi)",
"yokwe (YAW-kweh) (Marshallese: Ebon, Micronesia, Marshall Islands)",
"sain baina uu 'sain bai-na oo' (formal) sain uu 'say-noo' (casual) : (Mongolian)",
"नमस्ते '"'namaste'"' : Nepali (नेपाली)",
"cia, cha (Neopolitan)",
"dumela (doo-MAY-lah) one person, dumelang (doo-MAY-lang) >one person, khotso (coat-so) casual (Northern Sotho)",
"hei, Hallo, god dag, halla (Norwegian: Norsk)",
"ନମସ୍କାର Namaskār (Odia: Odisha, India)",
"akkam: Oromo (Cushitic; Ethiopia, Kenya, Somalia, Egypt)",
"salam, khe chare (Pashto: E. Iran, Afghanistan; Pakistan, Iran)",
"""dzień dobry (jeyn dob-ry) — good morning
cześć (cheshch) — informal hello
siema — used only by young people to say hi
hej — casual hey
(Polish: polski)""",
"'sata sri akaal' ਸਤ ਸ੍ਰੀ ਅਕਾਲ (formal, Sikh) : 'as-alam-walaykum' (formal, Muslim) : (Punjabi)",
"bună (informal), salut (formal) : (Romanian)",
"dumela 'doo-meh-lah' (single), dumelang 'doo-meh-lang' (>one) Sesotho (Sotho, Southern Bantu: Lesotho, S. Africa, Zimbabwe)",
"noŋ hɔ 侬好 (Sino-Tibetan Wu Chinese, City of Shanghai)",
"mhoro (Shona, Bantu, Zimbabwe)",
"āyubōvan - formal hello; halō - casual (Sinhala, Sri Lanka)",
"¡Hola! (O-laa), buenos dias, buenas tardes, buenas noches (Spanish)",
"Halo, sampurasun (formal) : (Sundanese, western Java Indonesia, Malayo-Polynesia)",
"grüss gott (Swabian, SW Germany)",
"sawubona (Swati, Bantu, Nguni, S. Africa)",
"hej, hallå (Swedish)",
"hoi (informal), grüezi (singular formal) grüezi mitenand (plural formal) (Swiss German)",
"kumusta 'how are you, hello' helów (informal) Tagalog",
"Ia ora na (ee-ah oh-rah-na) : (Tahitian)",
"lí-hó (lee-hoh) : (Taiwanese Hokkien)",
"cалом (sah-lohm), ассалом (a-sah-lohm) - casual hellos, ассалому алейкум (asah-lomu ah-lay-koom): (Tajik)",
"வணக்கம் Vanakkam (Tamil)",
"azul (peace) : (Tarifit)"
"isänmesez sawmısız (formal), sälam (informal) : Tatar (татарча)",
" నమస్కారం : Namaskāram (Telugu: Andhra, Pradesh, Telangana)",
"sawasdee krap สวัสดี ครับ/ค่ะ (as m), sawasdee ka สวัสดี ครับ/ค่ะ (as f) (Thai ภาษาไทย)"
"tashi delek (Lhasa dialect), cho demo (Amdo dialect) : (Tibetan, Tibet Autonomous Region)"
"osiyo (Cherokee, Tsalagi, Iroquois)",
"minjhani (to adults), kunjhani (to friends, children) (Tsonga: Bantu: S. Africa; Mozambique, Eswatini)",
"dumela (Tswana: Bantu: Botswana, S. Africa; Namibia, Zimbabwe)",
"Turkish : merhaba, selam",
"Assalomu alaykum, salom : (Uzbekistan)",
"Dobriy den, vitayu (formal), pryvit (informal) : (Ukrainian)",
"assalam u Alaikum السلام علیکم meaning '"'peace be on you'"' (anytime) : (Urdu, Pakistan)",
"xin chào, chào bạn — casual (Vietnamese)",
"womenjeka 'molo' (Xhosa: Nguni Bantu, S. Africa)",
"bawo ni (Yoruba: Nigeria, Benin; Sierra Leone, Liberia, W. Africa)",
"sawubona (Zulu: Bantu, Nguni, S. Africa Zululand, Natal; Botswana, Lesotho, Malawi, Mozambique, Eswatini)",
"NuqneH 'nook-neck' (Klingon)",
"bello (Minionese)",
"kaltxì 'kal-T-ì' (informal), oel ngati kameie 'o-el nga-ti kamei-e' (formal) (Na’vi)",
"saluton (Esperanto)",
"British Sign Language (BSL): 'Dominant hand wave, from inside to out with the palm facing towards recipient. As the hand moves bring it into a thumbs up gesture (hello) Sweep hands in front of chest, thumbs facing upwards, give two thumbs up: (how are you)",
"ASL (American Sign Language): 'Squeeze the fingers in your right hand together, touch the fingertips to the forehead, palm facing outward, and move your hand away from your forehead in a saluting motion (hello);' 'Point the center fingers towards the self, hands in front of chest, bring it out, to say (what's up)'"]

random_greetings = random.choice(greetings)

print(f"\n\nGreetings! {random_greetings}\n")

# + Thank You in all Languages
#There are 2,300 languages in Asia
#References:
#https://www.araioflight.com/hello-in-different-languages-world/
#https://www.araioflight.com/thank-you-in-different-languages-world/
#https://www.fluentin3months.com/international-greetings/
#https://www.youtube.com/watch?v=PoP9gVJLEqM
#https://www.british-sign.co.uk/bsl-greetings-signs-british-sign-language/
#Other sources+
#emoji output by connecting to website
#created by faxpillow
