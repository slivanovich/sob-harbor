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
Secret Story 4 (Portugal): Secret Story - A Casa dos Segredos 4 (2013) is the fourth season of the Portuguese reality television show "Secret Story".  It is based on the French version of "Secret Story", which itself is based on the international format, "Big Brother".  All episodes will be broadcast on TVI.  It started on 29 September.

Big Brother (French TV series): The French version of the international reality television format "Big Brother" has broadcast in the country since 2001.  Unlike most other territories, which use the name "Big Brother" (or a local equivalent) for their adaptations of the show, France used the name "Loft Story" for the initial two series of the format, broadcast on M6 in 2001-02, and then "Secret Story" for a revived version of the format, broadcast on TF1 since 2007.  The "Loft Story"/"Secret Story" format is also used in Canada (which used "Loft Story" from 2003 to 2009, "Big Brother" in 2010).  In addition, the "Secret Story" format first used in France has been introduced in the Netherlands (from 2011, five years after the last "Big Brother" series in the territory) and Portugal (from 2010, seven years after "Big Brother" ceased in the country).

Secret Story 7 (France): Secret Story 7 is the seventh season of the French reality television series "Secret Story", a show which is based loosely on the international "Big Brother" format.  Casting for this season opened on 24 August 2012.  The season began on 7 June 2013 and will finish airing on 13 September 2013, with all episodes airing on TF1, as in previous years.  The format of "Before Secret" this season was alike the concept used in the fourth edition.

Secret Story 5 (Portugal): Secret Story - A Casa dos Segredos 5 (2014) is the fifth season of the Portuguese reality television show "Secret Story".  It is based on the French version of "Secret Story", which itself is based on the international format, "Big Brother".  The reality show is being broadcast on TVI.  The casting were opened on June 11, 2014.  The launch was on September 21, 2014.  The finale was on December 31, 2014, and Elisabete was the winner.  This was the first time a woman won in a main "Secret Story - A Casa dos Segredos" season.

Secret Story 3 (Portugal): Secret Story - A Casa dos Segredos 3 (2012) was the third season of the Portuguese version of the reality show Secret Story, based on the original French version and of Big Brother.  The season started on 16 September 2012 and ended 107 days later with the final on 31 December 2012, which acclaimed Rúben as the winner.

Granite Flats: Granite Flats is BYUtv's first original scripted television drama series.  The show is set in a small Colorado town in the early 1960s during the Cold War, and follows several of the town's citizens as mysterious and potentially dangerous circumstances arise.  Season 1 launched on April 7, 2013.  The cast was joined by actors Christopher Lloyd and Cary Elwes for its second season, that premiered April 6, 2014.  Parker Posey and George Newbern joined the cast for season 3, premiered online April 4, 2015, before the TV season launch scheduled for October.  It has an audience of approximately 500,000 households per episode.

Secret Story 6 (Portugal): Secret Story - A Casa dos Segredos 6 (2016) is the sixth season of the Portuguese reality television show "Secret Story".  It is based on the French version of "Secret Story", which itself is based on the international format, "Big Brother".  The reality show is being broadcast on TVI.  The castings were opened on May 21, 2016.  The launch was on September 11, 2016.  Lasting 112 days, the season ended on December 31, 2016, and Helena was the winner.

Nadège Lacroix: Nadège Lacroix (born 30 June 1986) is a Swiss actress, television personality.  She became famous thanks to a French reality show, Secret Story.  She starred in the "Sous le soleil de Saint-Tropez" and the scripted television drama series, "Hollywood Girls : Une nouvelle vie en Californie".

Secret Story 6 (France): Secret Story 6 is the sixth season of "Secret Story".  The show started on May 25, 2012 and concluded on September 7, 2012.  The winner is Nadège Lacroix.

Secret Story: Desafio Final 1: Secret Story - A Casa dos Segredos: Desafio Final 1 (2013) is the first All-Stars season with housemates from Secret Story 2 & 3 of the Portuguese version of the reality show "Secret Story" based on the original French version and of "Big Brother".  The season started on 6 January 2013 and will end 22 days later with the final on 27 January 2013.  The prize is €10,000.

Question: The winner of Secret Story 6 starred in which scripted television drama series?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "winner_information": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the winner."
        },
        "won_season": {
          "type": "string",
          "description": "The specific season and show the person won."
        }
      },
      "required": [
        "name",
        "won_season"
      ],
      "additionalProperties": false
    },
    "series_starred_in": {
      "type": "array",
      "description": "A list of series the winner starred in.",
      "items": {
        "type": "object",
        "properties": {
          "series_name": {
            "type": "string",
            "description": "The title of the series."
          },
          "is_scripted_television_drama": {
            "type": "boolean",
            "description": "Indicates if the series is a scripted television drama."
          }
        },
        "required": [
          "series_name",
          "is_scripted_television_drama"
        ],
        "additionalProperties": false
      }
    },
    "answer_series_name": {
      "type": "string",
      "description": "The name of the scripted television drama series the winner starred in."
    }
  },
  "required": [
    "winner_information",
    "series_starred_in",
    "answer_series_name"
  ],
  "additionalProperties": false
}
