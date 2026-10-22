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
Zenobia (ship): Numerous vessels in the 19th & 20th centuries have been named Zenobia for Zenobia, the Queen (c. 240–272 CE)) of the Palmyrene Empire who conquered Egypt:

HMS Zenobia: A few ships of the British Royal Navy have borne the name HMS "Zenobia", named after Zenobia, the Queen of the Palmyrene Empire who conquered Egypt.

Zenobia (disambiguation): Zenobia (c. 240–272) was Queen of the Palmyrene Empire.

Zenobia: Septimia Zenobia (Palmyrene: (Btzby), pronounced Bat-Zabbai; AD 240–c.274) was a third-century queen of the Syria-based Palmyrene Empire.  Many legends surround her ancestry; she was certainly born to a noble Palmyrene family and married the ruler of the city, Odaenathus.  Her husband became king in 260, elevating Palmyra to supreme power in the Near East by defeating the Sassanians and stabilizing the Roman East.  After Odaenathus' assassination, Zenobia became the regent of her son Vaballathus and held "de facto" power throughout his reign.

Battle of Emesa: The Battle of Emesa was fought in 272 between Roman and Palmyran forces.  The Romans were led by Emperor Aurelian, while the Palmyrans were led by Queen Zenobia and her general Zabdas.

Aurelian: Aurelian (Latin: "Lucius Domitius Aurelianus Augustus" ; 9 September 214 or 215 – September or October 275) was Roman Emperor from 270 to 275.  Born in humble circumstances, he rose through the military ranks to become emperor.  During his reign, he defeated the Alamanni after a devastating war.  He also defeated the Goths, Vandals, Juthungi, Sarmatians, and Carpi.  Aurelian restored the Empire's eastern provinces after his conquest of the Palmyrene Empire in 273.  The following year he conquered the Gallic Empire in the west, reuniting the Empire in its entirety.  He was also responsible for the construction of the Aurelian Walls in Rome, and the abandonment of the province of Dacia.

Septimius Zabbai: Zabbai was a Palmyrene man who lived in the third century, and likely belonged to the upper-class of Palmyra.  An obscure figure, he is mainly known from Queen Zenobia's Palmyrene name mentioned in Palmyrene inscriptions, sptymy'btzby, which translates to Septimia Daughter of Zabbai.  Zenobia's Palmyrene name might hint at her family origins, and might tie with the medieval tradition recorded by medieval Persian scholar Al-Tabari that she was the daughter of an Arab sheikh.  Zenobia however, might've not been Zabbai's daughter, but the inscription might rather mean that she belonged to a family whose ancestral head was Zabbai.

Zabdas: Zabdas was the name of the general who led the forces of Queen Zenobia during her rule of the Palmyrene Empire.  He chose not to face the emperor Aurelian in Asia Minor, due to the mountainous nature of that province and its consequent negative effects on cavalry tactics, and awaited Aurelian in Syria.  He proved unable to defend Antioch, resulting in his defeat at the Battle of Immae.  Retreating, he made a stand at Emesa, but was again defeated.

Vaballathus: Lucius Julius Aurelius Septimius Vaballathus Athenodorus (Palmyrene: ; Arabic: ْوَهْبُ اللَّات Wahb Allāt ) 259 – 274 AD) was a king of the Palmyrene Empire centered at Palmyra, Syria, who came to power as a child, ruling with his regent, his mother Queen Zenobia, who led a revolt against Rome and formed the independent Palmyrene Empire.

Battle of Immae: The Battle of Immae was fought in 272 between the Roman army of Emperor Aurelian, and the armies of the Palmyrene Empire, whose leader, Queen Zenobia, had usurped Roman control over the eastern provinces.

Question: Zabdas was the name of which rank, who led the forces of Septimia Zenobia, a third-century queen, of the Syria-based Palmyrene Empire?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the person in question."
    },
    "person_rank": {
      "type": "string",
      "description": "The military rank of the person."
    },
    "associated_ruler": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the ruler associated with the person."
        },
        "title": {
          "type": "string",
          "description": "The title of the ruler."
        },
        "empire": {
          "type": "string",
          "description": "The empire ruled by the associated ruler."
        },
        "century_of_rule": {
          "type": "string",
          "description": "The century during which the ruler reigned."
        },
        "empire_location": {
          "type": "string",
          "description": "The geographical base of the ruler's empire."
        }
      },
      "required": [
        "name",
        "title",
        "empire",
        "century_of_rule",
        "empire_location"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "person_name",
    "person_rank",
    "associated_ruler"
  ],
  "additionalProperties": false
}
