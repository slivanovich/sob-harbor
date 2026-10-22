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
Italy Fed Cup team: The Italy Fed Cup team represents Italy in international women's tennis and is directed by the Federazione Italiana Tennis.  The team played in the first ever tournament in 1963, and is one of four teams that has taken part in every single edition since.

Katarína Kachlíková: Katarína Kachlíková (born 2 June 1985 in Žilina, Czechoslovakia) is a former professional Slovak tennis player.  She took part in the 2006 Bangalore Open and qualified but lost in the first round to Isha Lakhani.  She won 3 ITF Women's Circuit doubles titles and 1 singles title.  She has played on the WTA Tour and also taken part in the 2009 Summer Universiade.  Kachlíková retired from tennis 2011.

List of Universiade records in swimming: The fastest times swum in events at the Universiades (World University Games) are listed by International University Sports Federation (FISU) as a list of Universiade records in swimming.  Swimming has been part of every Universiade, and the events are always held in a long course (50 m) pool.  The last Universiade was held in Kazan, Russia in 2013.

1934 FIFA World Cup qualification: The 1934 FIFA World Cup was the first World Cup where the teams had to qualify, since the first edition in 1930 had no qualification rounds (the participating teams were invited by FIFA).  This time, a total of 32 teams entered the competition, so FIFA had to organize qualification (or preliminary) rounds to reduce the field to 16 teams for the final tournament.  Even Italy, the host of the World Cup, had to qualify (the only time the hosts had to qualify, and one of only two occasions the hosts have ever taken part in the qualification process), while the defending champions Uruguay refused to participate and defend their title because many European nations declined to take part in the 1930 World Cup held in Uruguay.

Fencing at the Summer Universiade: Fencing events have been contested at every Universiade since 1959 Summer Universiade in Turin.  After not being included in 1975.

1959 Summer Universiade: The 1959 Summer Universiade, also known as the I Summer Universiade, took place in Turin, Italy.

Commemorative Medal of the Unity of Italy: The Italian Risorgimento was celebrated by a series of medals set up by the three kings who ruled during the long process of unification - the Commemorative Medal for the Campaigns of the War of Independence and the various versions of the Commemorative Medal of the Unity of Italy, which were granted by the Kingdom of Italy to those who had taken part in the military operations which had led to Italian independence and later to all who participated in the First World War, since at that time it was traditionally held that Italy completed its unification with the annexation of the Trentino.  Its final awards were to participants in the March on Rome and the Impresa di Fiume.

Slovakia at the Paralympics: Slovakia as such made its Paralympic Games début at the 1994 Winter Paralympics in Lillehammer, following the break-up of Czechoslovakia, which had taken part in the Paralympics from 1972 to 1992.  Slovakia has taken part in every edition of both the Summer and Winter Paralympics since then.

Thailand at the Universiade: Thailand first participated at the Universiade in 1985, and has sent athletes to compete in every Summer Universiade since then.

Italy at the Universiade: Italy has participated in all editions of the Summer Universiade held since the first edition of 1959 Summer Universiade.

Question: Italy has taken part in every Universiade since the first one, held in what city?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "event_name": {
      "type": "string",
      "description": "The name of the international multi-sport event."
    },
    "first_edition_details": {
      "type": "object",
      "properties": {
        "year": {
          "type": "integer",
          "description": "The year the first edition of the event was held."
        },
        "host_city": {
          "type": "string",
          "description": "The city where the first edition of the event was held."
        },
        "host_country": {
          "type": "string",
          "description": "The country where the first edition of the event was held."
        }
      },
      "required": [
        "year",
        "host_city",
        "host_country"
      ],
      "additionalProperties": false
    },
    "italy_participation_since_first_edition": {
      "type": "boolean",
      "description": "Indicates if Italy has participated in all editions of the event since the first one."
    }
  },
  "required": [
    "event_name",
    "first_edition_details",
    "italy_participation_since_first_edition"
  ],
  "additionalProperties": false
}
