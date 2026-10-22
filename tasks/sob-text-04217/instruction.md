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
Panjdeh incident: The Panjdeh incident of 1885 was a diplomatic crisis between Britain and Russia caused by the Russian Empire's expansion southeast toward Afghanistan and India.  After nearly completing their conquest of central Asia the Russians captured an Afghan border fort.  Seeing a threat to India, Britain came close to threatening war.  Both sides backed down and the matter was settled by diplomacy.  The effect was to stop further Russian expansion in Asia, except for the Pamirs, and to define the northwest border of Afghanistan.

Legend of the White Cowl: The Legend of the White Cowl (Church Slavonic: По́вѣсть ω бѣ́ломъ клобуцѣ́ , Russian: Повесть о белом клобуке ) is a Russian Orthodox story first recorded by the monk Philotheus of Pskov in 1510.  It tells of the passage of a religious relic of great significance through great danger from Rome to Constantinople and finally to Moscow, at a time that many Russians believed the pre-eminent Christian Church in the world to be transferred in Moscow.

Battle of Olkieniki (1706): The Battle of Olkieniki took place at March 6, 1706 close to the town of Olkieniki in the Polish–Lithuanian Commonwealth (today Valkininkai in Lithuania) during the Great Northern War.  A Swedish detachment of 1,000 dragoons sent out by Charles XII from Grodno under Carl Gustaf Dücker sought to meet up with a larger Polish contingent under Józef Potocki and Jan Kazimierz Sapieha the Elder at Olkieniki, before marching towards Vilnius in order to secure the Swedish connection to Swedish Livonia which had been disturbed by Russian forces ever since the battle of Gemauerthof.  However, at the same time an allied force of about 4,600–7,000 Russians, Poles and Lithuanians under Christian Felix Bauer, Michał Serwacy Wiśniowiecki and Grzegorz Antoni Ogiński marched in their direction in order to beat the pro–Swedish Poles and Lithuanians before regrouping with their Swedish allies.  The Swedish and Russian–Polish forces soon, rather unexpectedly, stumbled upon each other outside of the town where a fierce fight took place.  The Swedes repulsed two attacks executed by their enemies, before withdrawing a distance away to some woods, in order to initiate a third attack prepared by the allied forces.  Meanwhile, the battle was witnessed from a distance away by the Swedish–friendly Poles and Lithuanians who had yet to participate in the fighting.  The Swedes soon, however, counterattacked on their own and managed to beat the allied forces from the field, after which the Poles and Lithuanians on the Swedish side decided the intervene and persecute the allies for a distance.  The battle resulted in more than 60 wounded Swedes and up to 50 killed and 100 wounded Russians and another 70 killed and equally many wounded Poles and Lithuanians siding with the Russians.  The Swedes soon arrived at Vilnius where they captured a large bulk of Russian supplies.

Afghanistan–Russia relations: Afghanistan–Russia relations (Russian: Российско-афганские отношения ) refers to the relations between the nations of Afghanistan and Russia.  The Great Game is the story of Russian-British confrontations over Afghanistan since 1840.

Russians in Georgia: There is no substantial Russian population in Georgia.  For many years, Georgia was a part of the Russian Empire, and later the Soviet Union.  As the two countries share a border, many Russians settled in various regions of Georgia.  In recent years, the number of Russians living in Georgia has sharply declined.

Russian language in the United States: The Russian language is among the top fifteen most spoken languages in the United States.  Since the dissolution of the Soviet Union, many Russians have migrated to the United States and brought the language with them.  Most Russian speakers in the United States today are Russian Jews.  According to the 2010 United States Census the number of Russian speakers was 854,955, which made Russian the 12th most spoken language in the country.

Valenki: Valenki (Russian: ва́ленки ; ] ; sg valenok (Russian: ва́ленок ; ] )) are traditional Russian winter footwear, essentially felt boots: the name "valenok" literally means "made by felting".  Valenki are made of wool felt.  They are not water-resistant, and are often worn with galoshes to keep water out and protect the soles from wear and tear.  Valenki were once the footwear of choice for many Russians, but in the second half of the 20th century they lost most of their appeal in cities, due to their association with rustic dress.

Hasan Israilov: Hasan Israilov (Chechen: "Israil Khant Hasan"/Исраил КIант Хьасан ; Russian: Хасан Исраилов "Khasan Israilov"; 1910 - December 29, 1944) was a Chechen nationalist, guerrilla fighter, journalist, and poet who led a Chechen and Ingush resistance and rebellion against the Soviet Union from 1940 until his death in 1944.  Israilov is regarded as the most influential Chechen resistance leaders during World War II, and he is considered by many Chechens to be a national hero.  He was infamous to the Soviets, and to many Russians, for his 1940-1944 uprising, which many Russians connected to an abortive German plot to undermine Soviet control over the North Caucasus (in reality, however, relations between Israilov's Chechen partisans and the Germans were tense at best, hostile at worst).  His name is also sometimes translitrated to Latin alphabet as Hassan Izrailov.

Russians in Afghanistan: There are estimated to be 1,500 Russians living in Afghanistan.  In the 1960s and 1970s, due to cooperation between the Soviet Union and Afghanistan, there were roughly 10,000 Russian expatriate engineers, interpreters, construction workers, and other similar professionals living in the country, a figure which had grown to 15,000 by the eve of the Soviet war in Afghanistan.  However, they mostly left the country during or after the war.  The remaining continue to leave since the War in Afghanistan.  There was some Russian-language media, but it closed down during the period of Taliban government.

Russians in Hong Kong: Russians in Hong Kong form one of the territory's smaller groups of expatriates and a minor portion of the worldwide Russian diaspora.  Many Russians from China passed through Hong Kong in the 1950s through 1970s on their way to resettlement in Australia, Brazil, and Canada.

Question: During what war did many Russians leave Afghanistan?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "main_event_description": {
      "type": "string",
      "description": "Description of the primary event being queried."
    },
    "conflict_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the war or conflict."
        },
        "type": {
          "type": "string",
          "description": "The type of conflict, e.g., 'War', 'Incident'."
        }
      },
      "required": [
        "name",
        "type"
      ],
      "additionalProperties": false
    },
    "population_movement": {
      "type": "object",
      "properties": {
        "group": {
          "type": "string",
          "description": "The population group involved in the movement."
        },
        "action": {
          "type": "string",
          "description": "The action taken by the population group, e.g., 'left', 'migrated'."
        },
        "location_from": {
          "type": "string",
          "description": "The country or region from which the population moved."
        },
        "timing_relative_to_conflict": {
          "type": "string",
          "description": "When the movement occurred in relation to the conflict."
        }
      },
      "required": [
        "group",
        "action",
        "location_from",
        "timing_relative_to_conflict"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "main_event_description",
    "conflict_details",
    "population_movement"
  ],
  "additionalProperties": false
}
