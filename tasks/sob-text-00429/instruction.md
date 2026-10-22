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
The Moscow Times: The Moscow Times is an English-language weekly newspaper published in Moscow, with a circulation of 55,000 copies.  It is distributed free of charge at places frequented by English-speaking tourists and expatriates such as hotels, cafés, embassies, and airlines and is also available by subscription.  The newspaper is popular among foreign citizens residing in Moscow and English-speaking Russians.  In November 2015 the newspaper changed its design and type from daily to weekly (released every Thursday) and increased the number of pages to 24.

The Southern Star (Montevideo): The Southern Star / "La Estrella del sur" (the last name is the Spanish translation, but both names were used in conjunction) was a bilingual newspaper edited in Montevideo, Uruguay, in 1807.  It was the first newspaper edited in the city, but it only lasted for a couple of months, while Montevideo was under British rule during the second British invasions of the Río de la Plata.  The newspaper was used to promote free trade and loyalty to the British Crown, as a possible way to achieve independence from the Spanish Crown.

2014 Latakia offensive: The 2014 Latakia offensive was a rebel offensive in the Latakia Governorate of Syria launched on 21 March 2014 by rebel Islamist groups including Al-Nusra Front, which called the offensive "Anfal", while a coalition of Supreme Military Council rebel groups called the offensive "The Martyrs Mothers".  The objectives of the offensive have been stated to be the taking over of all strategic observatories, government villages and the Mediterranean coast.  Observers have stated a strategic aim was to force the Syrian army to redeploy forces to Latakia, which would relieve pressure on other rebels elsewhere in Syria.  They reportedly succeeded in this with government forces being sent from Idlib, Hama and Aleppo to bolster defenses.

The Economist: The Economist is an English-language weekly magazine-format newspaper owned by the Economist Group and edited at offices in London.  Continuous publication began under its founder, James Wilson, in September 1843.  In 2015 its average weekly circulation was a little over 1.5 million, about half of which were sold in the United States.

Sinn Féin (newspaper): Sinn Féin was a weekly Irish nationalist newspaper edited by the Dublin typesetter, journalist and political thinker Arthur Griffith.  It was published by the Sinn Féin Printing & Publishing Company Ltd. (SFPP) between 1906 and 1914, and replaced an earlier newspaper called the "United Irishman" which was liquidated after a libel suit.  The SFPP brought out the "Sinn Féin Daily" in 1909 but had to abandon it when it plunged the company into enormous debt.  The "Sinn Féin" weekly and the SFPP both came to an end when they were suppressed by the British Government in 1914.

2014 Idlib offensive: The 2014 Idlib offensive refers to a series of rebel operations in the Idlib Governorate, during the Syrian Civil War, conducted by the rebels against the Syrian Government.  The clashes were mostly concentrated around Khan Shaykhun and on the highway towards Maarrat al-Nu'man.

Proletary: Proletary (The Proletarian) was an illegal Russian Bolshevik newspaper edited by Lenin; it was published from September 3, 1906 until December 11, 1909.  A total of fifty issues having appeared.  Active participants in the editorial work were Mikhail Vladimirsky, V. V. Vorovsky, I. F. Dubrovinsky, Anatoly Lunacharsky.  The technical side of publication was in the hands of Alexander Schlichter, E. S. Schlichter and others.  The first twenty issues of the paper were edited and set up in Vyborg (matrices were sent to St. Petersburg and the paper was printed there; for purposes of concealment the newspaper was date-lined Moscow).  Later, in view of growing difficulties in the way of publishing an illegal newspaper in Russia, the St. Petersburg and Moscow Committees of the Russian Social Democratic Labour Party decided that publication of the newspaper should he organised abroad.  Nos. 21 to 40 were published in Geneva and Nos. 41 to 50 in Paris.

Advance (newspaper): Advance was an English-language weekly newspaper published in Sudan in the 1960s.  The newspaper was linked to the Sudanese Communist Party.  It was edited by Joseph Garang.

2015 Idlib offensive: The 2015 Idlib offensive refers to a series of rebel operations in the Idlib Governorate, during the Syrian Civil War.  The offensive started with a rebel assault on the capital of the province, Idlib.  According to "The Economist", the capture of Idlib came about largely because Gulf Arab states "gave more backing to their proxies despite American objections."

Second Siege of Wadi Deif: The Second Siege of Wadi Deif refers to the siege of two Syrian Army bases, Wadi Deif and Hamadiyah (both just outside Maarrat al-Nu'man), by rebel forces, during the 2014 Idlib offensive of the Syrian Civil War.  The first siege of these two bases was broken by the Syrian Army on 18 April 2013.  During the siege, rebels detonated several 'tunnel bombs' underneath Army positions surrounding the bases, which was similar to the tactics used during the First World War.

Question: 2015 Idlib offensive refers to a series of rebel operations and is mentioned in the English-language weekly magazine-format newspaper edited where?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "offensive_name": {
      "type": "string",
      "description": "The name of the military offensive."
    },
    "event_type": {
      "type": "string",
      "description": "The type of event the offensive refers to."
    },
    "referenced_publication": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the publication that reported on the offensive."
        },
        "language": {
          "type": "string",
          "description": "The language of the publication."
        },
        "frequency": {
          "type": "string",
          "description": "How often the publication is released."
        },
        "format": {
          "type": "string",
          "description": "The format of the publication."
        },
        "editing_location": {
          "type": "string",
          "description": "The city where the publication is edited."
        }
      },
      "required": [
        "name",
        "language",
        "frequency",
        "format",
        "editing_location"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "offensive_name",
    "event_type",
    "referenced_publication"
  ],
  "additionalProperties": false
}
