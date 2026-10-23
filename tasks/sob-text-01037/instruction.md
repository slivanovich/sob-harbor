{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nTopal Recep Pasha: Topal Recep Pasha (\"Recep Pasha \"Lame\"; died 18 May 1632) was an Ottoman statesman from the Sanjak of Bosnia, as well as Damat (\"bridegroom\") to the House of Osman.  He served as the Grand Vizier of the Ottoman Empire from 10 February 1632 to 18 May 1632.  He was instrumental in lynching the former grand vizier, Hafız Ahmet Pasha.  When his brother-in-law Sultan Murad IV realized this, he had Recep Pasha executed on 18 May 1632.\n\nKara Ahmed Pasha Mosque: The Kara Ahmed Pasha Mosque or Gazi Ahmed Pasha Mosque (Turkish: \"Kara Ahmet Paşa Camii\" ) is an Ottoman mosque near the city walls in Istanbul, Turkey.\n\nGazi Mehmet Pasha's Mosque: Gazi Mehmet Pasha's Mosque is one of the oldest monuments of Islamic art in Prizren.  The inscription above the entrance states it was built in 1561.  This mosque has a square base and numerous windows, while the main veneration niche (mihrab) and the pulpit (mimber) are made of marble.  A hexagonal mausoleum (madrasa) has been built in the courtyard of the mosque which Mehmet Pasha earmarked as his grave.  Building complex that mosque settles in, includes a high school (madrasa), a primary school (maktab), a library and a mausoleum for the founder, a bath of Gazi Mehmet Pasha, which is about 150m away from the mosque.  This Mosque, nowadays known as Bajrakli Mosque is behind Albanian League Museum.  Together with Albanian League Complex, Bath of Gazi Mehmet Pasha, and old urban houses, Mehmet Pasha Mosque gives you the sense of Ottoman architecture.\n\nAl-Adiliyah Mosque: Al-Adiliyah Mosque (Arabic: جامع العادلية‎ ‎ , Turkish: \"Adliye Camii\" ) or Dukaginzâde Mehmed Pasha mosque is a mosque complex in Aleppo, located to the southwest of the Citadel, in \"Al-Jalloum\" district of the ancient city, few meters away from Al-Saffahiyah mosque.  The mosque was endowed by the Dukakinzade Mehmed Pasha in 1556.  Dukakinzade was the Ottoman governor-general of Aleppo from 1551 until 1553 when he was appointed as governor-general of Egypt.  He died in 1557 and the mosque was not completed until 1565-66 (AH 973).  It is considered to be one of the oldest mosques of the Ottoman period in Aleppo after the Khusruwiyah Mosque.\n\nMurad Pasha Mosque: The Murad Pasha Mosque (Arabic: جامع مراد باشا‎ ‎ , transliteration: \"Jami Murad Pasha\") is an early Ottoman-era mosque and mausoleum in Damascus, Syria, located in the Suwayqa sector of the Al-Midan quarter.  The mosque was erected and named after Murad Pasha, who served as the Ottoman governor (\"\"wali\"\") of Damascus between 1568-1569.  The mosque was built in 1568.  The mosque is also known as the Naqshbandi Mosque (Arabic: جامع النقشبندي‎ ‎ ) after the \"Naqshbandi\" sufi order which it served as a center for.\n\nHirami Ahmet Pasha Mosque: Hirami Ahmet Pasha Mosque (Turkish: \"Hırami Ahmet Paşa Mescidi\" ) is a former Eastern Orthodox church converted into a mosque by the Ottomans.  The small church, one among the 36 dedicated to Saint John the Baptist in Constantinople, was part of a monastery bearing the same name.  Its full name was Saint John the Forerunner by-the-Dome (Greek: , \"Hagios Ioannis ho Prodromos en tō Trullō\").  It is the smallest Byzantine church of Constantinople still extant and has never been studied.\n\nÇarşamba, Fatih: Çarşamba is a small part of Balat quarter of Istanbul, Turkey.  It is in Fatih, the capital district which hosts the provincial authorities, inside the walls of the ancient Byzantine city of Constantinople.  It is one of the most conservative areas of the city, and also a quite peaceful environment.  It is rich with Byzantine monuments, like the mosques of Fethiye and Hirami Ahmet Pasha.  According to 17th-century Ottoman traveler Evliya Çelebi, its name comes from the town of Çarşamba in the Black Sea Region since, after the Fall of Constantinople, this part of Istanbul was repopulated with people coming from that city.  In Turkish Çarşamba means \"Wednesday\" and a famous street market is organized every week on this day, the \"Çarşamba Pazarı\" (\"Çarşamba Market\", but also \"Wednesday Market\").\n\nHassan Pasha Mosque: The Hassan Pasha Mosque (Arabic: مسجد حسن الباشا‎ ‎ , \"Masjid Hassan el-Basha\"), also referred to as the Pasha Mosque or the Grand Mosque, is a mosque located in Oran, Algeria.  It was built in 1796 by order of Baba Hassan, Pasha of Algiers, in memory of the expulsion of the Spanish.\n\nArab Ahmet, Nicosia: Arab Ahmet is a Neighbourhood, Quarter, Mahalla or Parish of Nicosia, Cyprus and the mosque situated therein.  Both the Quarter and the mosque are named after Arab Ahmet Pasha, one of the Turkish commanders in the Ottoman conquest of Nicosia.  It is spelled Arabahmet in Turkish and Άραπ Άχμετ in Greek.\n\nGreat Palace Mosaic Museum: The Great Palace Mosaic Museum (Turkish: \"Büyük Saray Mozaikleri Müzesi\" ), is located close to Sultanahmet Square in Istanbul, Turkey, at Arasta Bazaar.  The museum houses mosaics from the Byzantine period, unearthed at the site of the Great Palace of Constantinople.\n\nQuestion: Great Palace Mosaic Museum and Hirami Ahmet Pasha Mosque, have which city in common?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"entity_names\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"The names of the entities mentioned in the question.\"\n    },\n    \"common_city\": {\n      \"type\": \"string\",\n      \"description\": \"The city that both entities have in common.\"\n    },\n    \"city_historical_names\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"Historical names associated with the common city, if mentioned in the context.\"\n    },\n    \"city_modern_name\": {\n      \"type\": \"string\",\n      \"description\": \"The modern name of the common city, if mentioned in the context.\"\n    }\n  },\n  \"required\": [\n    \"entity_names\",\n    \"common_city\",\n    \"city_historical_names\",\n    \"city_modern_name\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "entity_names": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "The names of the entities mentioned in the question."
      },
      "common_city": {
        "type": "string",
        "description": "The city that both entities have in common."
      },
      "city_historical_names": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "Historical names associated with the common city, if mentioned in the context."
      },
      "city_modern_name": {
        "type": "string",
        "description": "The modern name of the common city, if mentioned in the context."
      }
    },
    "required": [
      "entity_names",
      "common_city",
      "city_historical_names",
      "city_modern_name"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
