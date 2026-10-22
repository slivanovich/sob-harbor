Use the following extraction rules and source material. Write your final JSON object to `/tmp/answer.json`. The verifier reads that file, not your final chat message.

Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.

Rules:
- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.
- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.
- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.
- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.
- Include all required fields: Every field listed as required in the schema must appear in the JSON.
- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing.

Context:
Hassan Pasha Mosque: The Hassan Pasha Mosque (Arabic: مسجد حسن الباشا‎ ‎ , "Masjid Hassan el-Basha"), also referred to as the Pasha Mosque or the Grand Mosque, is a mosque located in Oran, Algeria.  It was built in 1796 by order of Baba Hassan, Pasha of Algiers, in memory of the expulsion of the Spanish.

Beyazıt Tower: Beyazıt Tower, also named Seraskier Tower, from the name of the Ottoman ministry of War, is an 85 m tall fire-watch tower located in the courtyard of Istanbul University's main campus (formerly Ottoman Ministry of War) on Beyazıt Square (known as the Forum Tauri in the Roman period) in Istanbul, Turkey, on top of one of the "seven hills" which Constantine the Great had built the city, following the model of Rome.

Rüstem Pasha: Rüstem Pasha Opuković (] ; Ottoman Turkish: رستم پاشا‎ ; Croatian: "Rustem-Paša Opuković" 1500 – 10 July 1561) was a Croatian -born Ottoman statesman.  He served as the grand vizier of sultan Suleiman the Magnificent.  Rüstem Pasha is also known as Damat Rüstem Pasha (the epithet "damat" meaning "son-in-law" to the Ottoman dynasty) because of his marriage to one of the sultan's daughters.

Vasat Atik Ali Pasha Mosque: Vasat Atik Ali Pasha Mosque (Turkish: "Vasat Atik Ali Paşa Camii" ), also known as Zincirlikuyu Mosque (Turkish: "Zincirlikuyu Camii" ) or Karagümrük Mosque, is an Ottoman mosque located in the Karagümrük neighbourhood of the Fatih district in Istanbul, Turkey, on Fevzipaşa Street.  Sultan Bayezid II's grand vizier Hadım Atik Ali Pasha, after whom the mosque is named, ordered its construction in 1502, and it was completed in 1512, one year after the grand vizier's death.

Gazi Atik Ali Pasha Mosque: The Gazi Atik Ali Pasha Mosque (Turkish: "Gazi Atik Ali Paşa Camii" ) is an old Ottoman mosque located in the Çemberlitaş neighbourhood of the Fatih district in Istanbul, Turkey.  Its construction was started under the orders of the future Grand Vizier Hadım Atik Ali Pasha in 1496 and was completed in 1497, during the reign of Sultan Bayezid II.  The mosque is located near the entrance to the Kapalıçarşı (Grand Bazaar), the Column of Constantine, and the historical Nuruosmaniye Mosque.

Beyazıt Square: Beyazıt Square (Turkish: "Beyazıt Meydanı" ) is a square in the district of Fatih, situated in the European part of Istanbul, Turkey.  It is officially named "Freedom Square" ("Hürriyet Meydanı" ), but is known as Beyazıt Square after the Bayezid II Mosque on one side of it.  The Square is the former site of the Forum of Theodosius built by Constantine the Great.  On one side of the square is the main entrance of Istanbul University; the Beyazıt Tower is on the university's campus and can be seen from the square.  The current form of the square was designed by Turgut Cansever.

Sinan Pasha (Ottoman admiral): Sinanüddin Yusuf Pasha or in short Sinan Pasha (Croatian: "Sinan-paša"), (died 21 December 1553) was an Ottoman Grand Admiral (Kapudan Pasha), who served the Ottoman Navy for nearly four years between 1550 and the end of 1553, during the reign of Suleiman the Magnificent.  He was of Croatian descent, the predecessor of Piali Pasha in this rank and the brother of Grand Vizier Damat Rüstem Pasha, who in turn was married to Mihrimah Sultan, a daughter of Suleiman the Magnificent.

Gazi Mehmet Pasha's Mosque: Gazi Mehmet Pasha's Mosque is one of the oldest monuments of Islamic art in Prizren.  The inscription above the entrance states it was built in 1561.  This mosque has a square base and numerous windows, while the main veneration niche (mihrab) and the pulpit (mimber) are made of marble.  A hexagonal mausoleum (madrasa) has been built in the courtyard of the mosque which Mehmet Pasha earmarked as his grave.  Building complex that mosque settles in, includes a high school (madrasa), a primary school (maktab), a library and a mausoleum for the founder, a bath of Gazi Mehmet Pasha, which is about 150m away from the mosque.  This Mosque, nowadays known as Bajrakli Mosque is behind Albanian League Museum.  Together with Albanian League Complex, Bath of Gazi Mehmet Pasha, and old urban houses, Mehmet Pasha Mosque gives you the sense of Ottoman architecture.

Sinan Pasha Mosque (Istanbul): The Sinan Pasha Mosque (Turkish: "Sinan Paşa Camii" ) is an Ottoman mosque located in a densely populated district of Beşiktaş, in Istanbul, Turkey.  It was built by famous Ottoman architect Mimar Sinan from the order of the admiral Sinan Pasha.  The "türbe" (tomb) of Barbaros Hayrettin Pasha is located just across the street.  Mosques of Mimar Sinan has been "said to have changed the history of architecture."

Rüstem Pasha Mosque: The Rüstem Pasha Mosque (Turkish: "Rüstem Paşa Camii" ) is a 16th-century Ottoman mosque located in Hasırcılar Çarşısı (Strawmat Weavers Market) in the Tahtakale neighborhood, of the Fatih district of Istanbul, Turkey.

Question: Are both Beyazıt Tower and Rüstem Pasha Mosque located in Istanbul ?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "is_both_in_istanbul": {
      "type": "boolean",
      "description": "True if both the Beyaz\u0131t Tower and R\u00fcstem Pasha Mosque are located in Istanbul."
    },
    "entities_locations": {
      "type": "array",
      "description": "Details about the location of each entity.",
      "items": {
        "type": "object",
        "properties": {
          "entity_name": {
            "type": "string",
            "description": "The name of the landmark."
          },
          "city": {
            "type": "string",
            "description": "The city where the landmark is located."
          },
          "country": {
            "type": "string",
            "description": "The country where the landmark is located."
          }
        },
        "required": [
          "entity_name",
          "city",
          "country"
        ],
        "additionalProperties": false
      }
    },
    "common_location_city": {
      "type": "string",
      "description": "The city that is common to both entities, if any."
    }
  },
  "required": [
    "is_both_in_istanbul",
    "entities_locations",
    "common_location_city"
  ],
  "additionalProperties": false
}
