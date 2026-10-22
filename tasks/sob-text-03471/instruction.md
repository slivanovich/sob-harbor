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
2014 Lunar New Year Cup: 2014 Lunar New Year Cup (), also known as the Lunar New Year AET Cup 2014 () due to sponsorship reason, is the annual football event held in Hong Kong in Lunar New Year.  Citizen are authorised by the Hong Kong Football Association to hold the event.

Khorol (game): Khorol or Khorlo (Mongolian: Хорол or Хорло) is a multi-trick tile-based game played in Mongolia, Inner Mongolia, and Tuva, usually on Lunar New Year's.  It is played between two and eight players with four being the most common.  The game appeared during Manchu rule (1645-1912).

2013 Lunar New Year Cup: 2013 Lunar New Year Cup (), also known as the China Mobile Satellite Communication Cup () due to sponsorship reason, is the annual football event held in Hong Kong in Lunar New Year.  The name of this event was changed back to Lunar New Year Cup after two editions of Asian Challenge Cup were held in 2011 and 2012.

2008 Lunar New Year Cup: The 2008 Lunar New Year Cup, officially known as Wing Lung Bank 2008 Lunar New Year Cup, is a football tournament held in Hong Kong on the first and fourth day of the Chinese New Year of the Year of Rat (7 February and 10 February 2008).

Sajibu nongma panba: Sajibu Nongma Pānba, also called Meetei Cheiraoba or Sajibu Cheiraoba, is the lunar new year festival of the people who follow the sanamahism religion of the Indian state of Manipur.  The name Sajibu Nongma Pānba derives from the Manipuri words: Sajibu - the first month of the year which usually falls during the month of April according to Meitei lunar calendar, Nongma - first date of a Month, Pānba - to be.  Literally, it means the first day of the month of Sajibu.  Similarly, according to the Hindu lunar calendar, the lunar new year is celebrated on the same day as in Karnataka, Andhra Pradesh, Maharashtra and many other Indian states.

2015 Lunar New Year Cup: 2015 Lunar New Year Cup (), also known as the Lunar New Year AET Cup 2015 () due to sponsorship reason, is the annual football event held in Hong Kong to celebrate the Chinese New Year.  South China of Hong Kong Premier League were authorised by the Hong Kong Football Association to hold the 2015 event; and New York Cosmos of North American Soccer League were invited to participate.  It was the first time an American football team had joined this event.  The football march between these two teams was played in Hong Kong Stadium on 19 February 2015, the Chinese New Year Day.  The Cup was won by New York Cosmos after a penalty shootout.

Lunar New Year Fair: Lunar New Year Fair (年宵市場, or flowermarket 花市) is a type of fair held annually a few days before Lunar New Year in Chinese New Year markets in China.  Flower fairs are primarily practiced by the Cantonese, and spread with Cantonese immigration.

Tsagaan Sar: The Mongolian Lunar New Year, commonly known as Tsagaan Sar (Mongolian: Цагаан сар , "Cagán sar" / ᠴᠠᠭᠠᠨ ᠰᠠᠷᠠ , ] or literally White Moon), is the first day of the year according to the Mongolian lunisolar calendar.  The festival of the Lunar New Year is celebrated by the Mongols along with the people of the Arctic.

Lunar New Year Fireworks Display in Hong Kong: Lunar New Year Fireworks Display in Hong Kong is an annual event to celebrate the Chinese New Year in Hong Kong.  It is held on The Second Day of Lunar New Year above the sky of Victoria Harbour in the evening.

2017 Lunar New Year Cup: The 2017 Lunar New Year Cup is the annual edition of the Lunar New Year Cup, held in Hong Kong to celebrate the Chinese New Year in late January 2017.  This year, four teams were invited to participate, playing two games each in a knockout tournament.  Australia under-23 withdrew before the tournament and were replaced by Auckland City.

Question: Khorol or Khorlo, is a multi-trick tile-based game played in Mongolia, Inner Mongolia, and Tuva, usually on Lunar New Year's, the Mongolian Lunar New Year, is commonly known as what?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "game_name": {
      "type": "string",
      "description": "The name of the game."
    },
    "game_type": {
      "type": "string",
      "description": "Description of the game type."
    },
    "regions_played": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "List of regions where the game is played."
    },
    "lunar_new_year_variant": {
      "type": "string",
      "description": "The specific variant of Lunar New Year mentioned."
    },
    "common_name_of_variant": {
      "type": "string",
      "description": "The common name for the specified Lunar New Year variant."
    }
  },
  "required": [
    "game_name",
    "game_type",
    "regions_played",
    "lunar_new_year_variant",
    "common_name_of_variant"
  ],
  "additionalProperties": false
}
