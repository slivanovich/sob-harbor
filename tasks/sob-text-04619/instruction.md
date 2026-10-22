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
Juan Francisco García (composer): Juan Francisco García (born June 16, 1892 - November 18, 1974) was Dominican merengue composer.  He was one of several merengue musicians who sought to promote the genre in the early 20th century, along with Juan Espínola and Julio Alberto Hernández.  Garcia was an educated musician who brought merengue to the upper-class of the country.

The Bohemian Soul: Alma de bohemio (English language: "The Bohemian Soul") is a 1949 Argentine film directed by Julio Saraceni and written by Carlos A. Petit with Rodolfo Sciammarella.  It stars Alberto Castillo and Fidel Pintos.

Rubén Oseguera González: Rubén Oseguera González (born February 14, 1990), commonly referred to by his alias El Menchito, is a suspected U.S.-born Mexican drug lord and former high-ranking leader of the Jalisco New Generation Cartel (CJNG), a criminal group based in Jalisco.  He is the son of Nemesio Oseguera Cervantes (alias "El Mencho"), one of Mexico's most-wanted drug lords.  Under his father, he allegedly worked as the CJNG's second-in-command and managed international drug trafficking operations.

Elvis González Valencia: Elvis González Valencia (born October 12, 1980), commonly referred to by his alias El Elvis, is a suspected Mexican drug lord and high-ranking leader of the Jalisco New Generation Cartel (CJNG) and Los Cuinis, two allied criminal groups based in Jalisco.  He was reportedly responsible for managing international drug trafficking operations and money laundering schemes under his brother Abigael González Valencia (alias "El Cuini") and brother-in-law Nemesio Oseguera Cervantes (alias "El Mencho").

Alberto Pineda Villa: Alberto Pineda Villa (died September 12, 2009), commonly referred to by his alias El Borrado ("The Erased One", "The Crossed-Out"), was a Mexican drug lord and high-ranking leader of the Beltrán Leyva Cartel, a drug trafficking organization.  He was killed on 12 September 2009.

Nemesio Oseguera Cervantes: Nemesio or Rubén Oseguera Cervantes (born July 17, 1966), commonly referred to by his alias El Mencho, is a suspected Mexican drug lord and leader of the Jalisco New Generation Cartel (CJNG), a criminal group based in Jalisco.  He is one of Mexico's most-wanted men, and the U.S. government is offering up to US$5 million for information that leads to his arrest and/or conviction.  He is wanted for drug trafficking, organized crime involvement, and illegal possession of firearms.  He is reportedly responsible for coordinating drug trafficking operations in the Americas, Europe, Asia, and Africa.  Under his command, the CJNG became one of Mexico's leading criminal organizations.

Antonio Oseguera Cervantes: Antonio Oseguera Cervantes (born August 20, 1958), commonly referred to by his alias Tony Montana, is a suspected Mexican drug lord and former high-ranking leader of the Jalisco New Generation Cartel (CJNG), a criminal group based in Jalisco.  His brother is Nemesio Oseguera Cervantes (alias "El Mencho"), the leader of the CJNG and one of Mexico's most-wanted drug lords.  In Mexico, he was formally charged in 2015 for drug trafficking and being in possession of military-exclusive firearms.

Abigael González Valencia: Abigael González Valencia (born October 18, 1972), commonly referred to by his alias El Cuini, is a suspected Mexican drug lord and former leader of the Jalisco New Generation Cartel (CJNG), a criminal group based in Jalisco.  He was also the head of Los Cuinis, an organization allied to the CJNG.  Along with his brother-in-law Nemesio Oseguera Cervantes (alias "El Mencho"), one of Mexico's most-wanted men, González Valencia reportedly coordinated international drug trafficking operations in the Americas, Europe, and Asia.  He was also responsible for managing the financial operations of the CJNG and Los Cuinis.

Carlos Manuel Hoo Ramírez: Carlos Manuel Hoo Ramírez (born 15 October 1978), commonly referred to by his alias El Cóndor, is a former Mexican Armed Forces commando and imprisoned high-ranking member of the Sinaloa Cartel, a drug trafficking organization.  He was the alleged communication's chief and personal bodyguard of Joaquín "El Chapo" Guzmán, once considered Mexico's most-wanted drug lord.  On 22 February 2014, he was arrested by the Mexican Navy along with Guzmán at a beach resort area in Mazatlán, Sinaloa.

Julio Alberto Castillo Rodríguez: In June 2015, he was arrested in Jalisco along with his brother-in-law Rubén Oseguera González (alias "El Menchito"), and imprisoned at the Federal Social Readaptation Center No. 1, Mexico's maximum-security prison.  He was released a month later for lack of evidences.  Mexican federal authorities re-arrested him in April 2016 for his alleged involvement in the CJNG.

Question: Julio Alberto Castillo Rodríguez was arrested in Jalisco, along with his brother-in-law, he's commonly referred to, by his alias El Menchito, true name?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The true name of the individual."
    },
    "alias": {
      "type": "string",
      "description": "The alias by which the individual is commonly referred."
    },
    "relationship_to_julio_alberto_castillo_rodriguez": {
      "type": "string",
      "description": "The relationship of the individual to Julio Alberto Castillo Rodr\u00edguez."
    },
    "arrest_details": {
      "type": "object",
      "properties": {
        "location": {
          "type": "string",
          "description": "The location where the arrest took place."
        },
        "year": {
          "type": "integer",
          "description": "The year of the arrest."
        }
      },
      "required": [
        "location",
        "year"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "person_name",
    "alias",
    "relationship_to_julio_alberto_castillo_rodriguez",
    "arrest_details"
  ],
  "additionalProperties": false
}
