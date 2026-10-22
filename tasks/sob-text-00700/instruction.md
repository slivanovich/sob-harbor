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
Molla Çelebi Mosque: The Molla Çelebi Mosque (Turkish: "Molla Çelebi Camii" ), sometimes known as Fındıklı Mosque (Turkish: "Fındıklı Camii" ) also as The Hazelnut is an Ottoman mosque located in the Fındıklı neighbourhood of Beyoğlu district in Istanbul, Turkey.  It was built by Ottoman architect Mimar Sinan under the order of Kazasker Mehmet Vusuli Efendi, Chief Judge of Istanbul.  The mosque is located on the Bosphorus waterfront, close to the Kabataş ferry port and Dolmabahçe Mosque.

Rahmi M. Koç Museum: The Rahmi M. Koç Museum is a private industrial museum in Istanbul, Turkey dedicated to history of transport, industry and communications.  Rahmi M. Koç, member of the wealthiest dynasty in Turkey and retired boss of the Koç Group, founded the museum in 1991, which was opened on December 13, 1994.  The museum is located in the suburb of Hasköy on the north shore of the Golden Horn and situated in two historical buildings connected to each other.  It is open to public every day except Monday.  The museum's general manager is Ertuğrul Duru.

Ishak Çelebi Mosque: The Ishak Çelebi Mosque (Macedonian: Исак џамија, "Isak džamija" ) is the largest mosque in Bitola, Macedonia.  It is situated along the north bank of the Dragor River.  This area was known as Bit-Pazar in the quarter of Emir Bey or Eyne Bey, also known as Ishak Çelebi mahalle.

Çengelhan Rahmi M. Koç Museum: The Çengelhan Rahmi M. Koç Museum (Turkish: "Çengelhan Rahmi M. Koç Müzesi" ) is a technology museum in Ankara, Turkey.

Mahmud Çelebi Mosque: The Mahmud Çelebi Mosque (Greek: Τζαμί του Μαχμούτ Τσελεμπή ) or Boyali Mosque (Μπογιαλί Τζαμί) is an Ottoman mosque in the northern Greek city of Veria.

Hüseyin Rahmi Gürpınar Museum: Hüseyin Rahmi Gürpınar Museum (Turkish: "Hüseyin Rahmi Gürpınar Müzesi" ) is a historic house museum dedicated to the writer Hüseyin Rahmi Gürpınar in İstanbul, Turkey.

Mosque Katip Sinan Qelebi: The Mosque Katip Sinan Qelebi, also known as "Katip Çelebi" (Turkish: "Sinan Katip Camii" ), is located on the Adem Jaschari Street in Prizren, Kosovo.  "Katip" means "secretary" in Turkish.  It may be named after Katip Çelebi but it also maybe named like the Plaošnik mosque in Ohrid,

Ali Yıldırım Koç: Ali Yıldırım Koç (] , born 2 April 1967) is a Turkish businessman.  He is a third-generation member of Turkey's wealthiest Koç family and the youngest son of Rahmi Koç.

Gümüşçay: Gümüşçay (former Güvercinli ) is a belde (town) in Biga district of Çanakkale Province, Turkey.  At it is situated in the Anatolian portion of the province 10 km south of Marmara Sea coast.  The distance to Biga is 6 km .  The population of Gümüşçay was 2118 as of 2013.  The settlement was an Ottoman district center named Güvercinli.  The mosque of Gümüşçay, the Nasuh Çelebi mosque was built during the reign of Mahmut I (1730-1754).  The settlement was declared a seat of township in 1949.  The main economic sector of the town is agriculture.

Çelebi Sultan Mehmed Mosque: The Çelebi Sultan Mehmed Mosque (Turkish: "Çelebi Sultan Mehmed Camii" ; Greek: Τέμενος Μεχμέτ Α' ), also known as the Bayezid Mosque (Τέμενος Βαγιαζήτ) and the Great Mosque (Turkish: "Büyük Camii" or "Ulu Camii"), is an early 15th-century Ottoman mosque in Didymoteicho, East Macedonia and Thrace, in the far northeast of Greece.

Question: In which city will you find Molla Çelebi Mosque and the Rahmi M. Koç Museum?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "city_name": {
      "type": "string",
      "description": "The name of the city where the entities are located."
    },
    "country": {
      "type": "string",
      "description": "The country where the city is located."
    },
    "entities_found": {
      "type": "array",
      "description": "A list of entities found in the specified city.",
      "items": {
        "type": "object",
        "properties": {
          "entity_name": {
            "type": "string",
            "description": "The name of the entity."
          },
          "entity_type": {
            "type": "string",
            "description": "The type of the entity (e.g., Mosque, Museum)."
          }
        },
        "required": [
          "entity_name",
          "entity_type"
        ],
        "additionalProperties": false
      }
    },
    "number_of_entities_found": {
      "type": "integer",
      "description": "The total count of entities found in the city that were mentioned in the question."
    }
  },
  "required": [
    "city_name",
    "country",
    "entities_found",
    "number_of_entities_found"
  ],
  "additionalProperties": false
}
