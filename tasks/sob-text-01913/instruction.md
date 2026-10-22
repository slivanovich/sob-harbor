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
1921 Far Eastern Championship Games: The 1921 Far Eastern Championship Games was the fifth edition of the regional multi-sport event, contested between China, Japan and the Philippines, and was held from 30 May to 3 June in Shanghai, Republic of China.  A total of eight sports were contested over the course of the five-day event.  India, Malaya, Siam (Thailand), Ceylon (Sri Lanka) and Java were all invited to participate at the games, but did not do so due to the expense of sending teams to Shanghai.

1934 Far Eastern Championship Games: The 1934 Far Eastern Championship Games was the tenth edition of the regional multi-sport event, contested between China, Japan and the Philippines, and was held from 16–20 May in Manila, the Philippines.  A total of eight sports were contested during the four-day competition.  The Dutch East Indies (Indonesia) participated at the games, becoming only the second nation outside of the traditional three to send a delegation to the event (after India in 1925).

Regino Ylanan: Region R. Ylanan (7 September 1889 – 1963) was a Filipino athlete, physician, sports administrator, physical educator, and sports historian.  He rose to fame with three gold medals in track and field at the 1913 Far Eastern Championship Games in Manila.  He won two further medals at the 1915 Games and also represented his country in baseball at three editions of the tournament.

Athletics at the Asian Games: Athletics is an Asian Games event since 1951 in New Delhi, India.  Among major athletics tournaments of the region, it succeeded the athletics at the Far Eastern Championship Games, which had ceased to be held after 1938.

Far Eastern Championship Games: The Far Eastern Championship Games (also known as the Far Eastern Championships, Far Eastern Games or Far East Games) was an Asian multi-sport event considered to be a precursor to the Asian Games.

Anselmo Gonzaga: Anselmo Gonzaga was a Filipino sprinter.  He competed in the 100 m and 200 m events at the 1928 Summer Olympics, but failed to reach the finals.  Gonzaga won one gold and two silver medals in these events at the Far Eastern Championship Games, which were a precursor to the Asian Games.

Tennis at the Far Eastern Championship Games: Tennis was contested at the Far Eastern Championship Games.  It was one of the main eight sports to feature on the programme.  The following are the known results for the tennis event of the games.

1915 Far Eastern Championship Games: The 1915 Far Eastern Championship Games was the second edition of the regional multi-sport event, contested between China, Japan and the Philippines, and was held from 15–22 May 1915 in Shanghai, Republic of China.  A total of nine sports were contested – the inclusion of cycling increased the total from the eight held at the first edition.  This marked the first time that the event was held under its "Far Eastern Championship Games" moniker, followed a change from the naming as the "Oriental Olympic Games" in 1913.

Juan Taduran: Juan K. Taduran was a Filipino track and field athlete who competed in the decathlon and in middle-distance running events.  In the 1920s he won three consecutive gold medals in the decathlon at the Far Eastern Championship Games – a forerunner of the Asian Games.

Athletics at the Far Eastern Championship Games: Athletics was one of the sports at the biennial Far Eastern Championship Games.  Athletics competitions were held at every one of the ten editions of the games, which existed between 1913 and 1934.  This represented the first time that a regular major international athletics competition occurred between Asian nations.  It was later succeeded by athletics at the Asian Games, which began in 1951.

Question: How many golden also did Jan Tauren win at the Far eastern Championship games?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "athlete_name": {
      "type": "string",
      "description": "The name of the athlete."
    },
    "gold_medals_won": {
      "type": "integer",
      "description": "The number of gold medals won by the athlete."
    },
    "event_category": {
      "type": "string",
      "description": "The category of events in which the gold medals were won."
    },
    "games_name": {
      "type": "string",
      "description": "The name of the multi-sport event where the medals were won."
    }
  },
  "required": [
    "athlete_name",
    "gold_medals_won",
    "event_category",
    "games_name"
  ],
  "additionalProperties": false
}
