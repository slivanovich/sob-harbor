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
Maykopsky District: Maykopsky District (Russian: Майко́пский райо́н ; Adyghe: Мыекъуапэ къедзыгъо ) is an administrative and a municipal district (raion), one of the seven in the Republic of Adygea, Russia.  It is located in the south of the republic and borders with Giaginsky District in the north, Mostovsky District of Krasnodar Krai in the east, the territory of the City of Sochi in Krasnodar Krai in the south, Apsheronsky District of Krasnodar Krai in the west and southwest, and with Belorechensky District of Krasnodar Krai in the northwest.  The area of the district is 3667.43 km2 .  Its administrative center is the rural locality (a settlement) of Tulsky.  As of the 2010 Census, the total population of the district was 58,439, with the population of Tulsky accounting for 18.4% of that number.

Krasnogvardeysky District, Republic of Adygea: Krasnogvardeysky District (Russian: Красногварде́йский райо́н ; Adyghe: Красногвардейскэ къедзыгъо ) is an administrative and a municipal district (raion), one of the seven in the Republic of Adygea, Russia.  It is located in the northwest of the republic and borders with Ust-Labinsky District of Krasnodar Krai in the north, Shovgenovsky District in the east, Belorechensky District of Krasnodar Krai in the south, and with Krasnodar Reservoir in the west.  Its borders with Teuchezhsky District (in the west) and Dinskoy District of Krasnodar Krai (in the northwest) pass through the waters of Krasnodar Reservoir.  The area of the district is 725.52 km2 .  Its administrative center is the rural locality (a "selo") of Krasnogvardeyskoye.  As of the 2010 Census, the total population of the district was 30,868, with the population of Krasnogvardeyskoye accounting for 30.6% of that number.

Krasnodar City Police: The Krasnodar City Police ("Краснодарская полиция"; or officially "Управление МВД России по городу Краснодару" = The MVD's Directorate of Krasnodar City), established in May 6, 1801, is the main municipal police force in Krasnodar Krai with primary responsibilities in law enforcement and investigation in Krasnodar City.  The police is one of the oldest police departments established in Russia.

Krasnodar Krai: Krasnodar Krai (Russian: Краснода́рский край , "Krasnodarsky kray"; ] ) is a federal subject (a krai) of Russia.  It is geographically located in the North Caucasus region in Southern Russia, and is administratively part of the Southern Federal District.  Krasnodar Krai is the third-largest federal subject by population with  5,226,647 (2010 Census).

Teuchezhsky District: Teuchezhsky District (Russian: Теуче́жский райо́н ; Adyghe: Теуцожь къедзыгъо ) is an administrative and a municipal district (raion), one of the seven in the Republic of Adygea, Russia.  It is located in the west of the republic and borders with the territory of the City of Krasnodar of Krasnodar Krai, Krasnodar Reservoir, and Krasnogvardeysky District in the north, Belorechensky District of Krasnodar Krai in the east and southeast, the territory of the Town of Goryachy Klyuch of Krasnodar Krai in the south, and with Takhtamukaysky District in the west.  The area of the district is 700 km2 .  Its administrative center is the rural locality (an "aul") of Ponezhukay.  As of the 2010 Census, the total population of the district was 20,643, with the population of Ponezhukay accounting for 16.7% of that number.

Government: A government is the system by which a state or community is controlled.  In the Commonwealth of Nations, the word "government" is also used more narrowly to refer to the collective group of people that exercises executive authority in a state.  This usage is analogous to what is called an "administration" in American English.  Furthermore, especially in American English, the concepts of "the state" and "the government" may be used synonymously to refer to the person or group of people exercising authority over a politically organized territory.  Finally, government is also sometimes used in English as a synonym for governance.

Krasnodar Krai Police: Main Directorate for Internal Affairs of Krasnodar Krai (ГУ МВД России по Краснодарскому краю) or the Police of Krasnodar Krai (Полиция Краснодарского края) is the main law enforcement agency in Government of Krasnodar Krai in Southern Russia.

Takhtamukaysky District: Takhtamukaysky District (Russian: Тахтамука́йский райо́н ; Adyghe: Тэхъутэмыкъуае къедзыгъо ) is an administrative and a municipal district (raion), one of the seven in the Republic of Adygea, Russia.  It is located in the west of the republic and borders with Krasnoarmeysky District of Krasnodar Krai and with the territory of the City of Krasnodar in the north, Teuchezhsky District in the east, the territory of the Town of Goryachy Klyuch of Krasnodar Krai in the south, and with Seversky District of Krasnodar Krai in the south and west.  The area of the district is 463.6 km2 .  Its administrative center is the rural locality (an "aul") of Takhtamukay.  As of the 2010 Census, the total population of the district was 69,662, with the population of Takhtamukay accounting for 7.5% of that number.

Altai Krai Police: Main Directorate for Internal Affairs of Altai Krai (Главного управления Министерства внутренних дел Российской Федерации по Алтайскому краю) or the Police of Alitai Krai is the main law enforcement agency in Government of Altai Krai in Southern Russia.

2012 Krasnodar Krai floods: The 2012 Krasnodar Krai floods occurred in southwest Russia in early July, mainly in Krasnodar Krai near the coast of the Black Sea.  The equivalent of five months of rain fell overnight in some southern parts of the country according to the Hydrometeorological Centre of Russia.  One hundred seventy-one people died during the floods, and Russian police said the floods damaged the homes of nearly 13,000 people.  According to the governor of Krasnodar Krai, Aleksandr Tkachyov, "there was nothing of the kind for the last 70 years".  The flood was part of the aftermath of an intense storm that hit Krasnodar, dropping almost half a year’s worth of rainfall on the region over two days.  Close to 30,000 people were affected by the floods.

Question: Krasnodar Krai Police, is the main law enforcement agency in Southern Russia, controlled system by which state or community term, commonly called, what?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "entity_name": {
      "type": "string",
      "description": "The name of the entity being described."
    },
    "entity_type": {
      "type": "string",
      "description": "The type of entity, e.g., 'law enforcement agency'."
    },
    "governing_system_description": {
      "type": "string",
      "description": "A description of the system by which a state or community is controlled."
    },
    "common_term_for_system": {
      "type": "string",
      "description": "The common term used to refer to the system by which a state or community is controlled."
    }
  },
  "required": [
    "entity_name",
    "entity_type",
    "governing_system_description",
    "common_term_for_system"
  ],
  "additionalProperties": false
}
