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
1966 Australian Championships: The 1966 Australian Championships was a tennis tournament that took place on outdoor Grass courts at the White City Tennis Club, Sydney, Australia from 21 to 31 January.  It was the 54th edition of the Australian Championships (now known as the Australian Open), the 15th held in Sydney, and the first Grand Slam tournament of the year.  The singles titles were won by Australians Roy Emerson and Margaret Smith.

1961 Australian Championships: The 1961 Australian Championships was a tennis tournament that took place on outdoor Grass courts at the Kooyong Lawn Tennis Club, Melbourne, Australia from 17 January to 27 January.  It was the 49th edition of the Australian Championships (now known as the Australian Open), the 14th held in Melbourne, and the first Grand Slam tournament of the year.  The singles titles were taken by Roy Emerson and Margaret Smith.

1937 Australian Championships: The 1937 Australian Championships was a tennis tournament that took place on outdoor Grass courts at the White City Tennis Club, Sydney, Australia from 22 January to 30 January.  It was the 30th edition of the Australian Championships (now known as the Australian Open), the 8th held in Sydney, and the first Grand Slam tournament of the year.  The singles titles were won by Australians Vivian McGrath and Nancye Wynne.

1958 Australian Championships: The 1958 Australian Championships was a tennis tournament that took place on outdoor Grass courts at the White City Tennis Club, Sydney, Australia from 17 January to 27 January.  It was the 46th edition of the Australian Championships (now known as the Australian Open), the 13th held in Sydney, and the first Grand Slam tournament of the year.  The singles titles were taken by Ashley Cooper and Angela Mortimer.

1934 Australian Championships: The 1934 Australian Championships was a tennis tournament that took place on outdoor Grass courts at the White City Tennis Club, Sydney, Australia from 18 January to 27 January.  It was the 27th edition of the Australian Championships (now known as the Australian Open), the 7th held in Sydney, and the first Grand Slam tournament of the year.  The singles titles were won by British Fred Perry and Australian Joan Hartigan Bathurst.

Australian Open: The Australian Open is a major tennis tournament held annually over the last fortnight of January in Melbourne, Australia.  First held in 1905, the tournament is chronologically the first of the four Grand Slam tennis events of the year – the other three being the French Open, Wimbledon and the US Open.  It features men's and women's singles; men's, women's and mixed doubles and junior's championships; as well as wheelchair, legends and exhibition events.  Prior to 1988 the tournament had been played on grass courts, but since then two types of hardcourt surfaces have been used at Melbourne Park – green coloured Rebound Ace up to 2007 and, afterwards, blue Plexicushion.

1931 Australian Championships: The 1931 Australian Championships was a tennis tournament that took place on outdoor Grass courts at the White City Tennis Club, Sydney, Australia from 27 February to 8 March.  It was the 24th edition of the Australian Championships (now known as the Australian Open), the 6th held in Sydney, and the first Grand Slam tournament of the year.  The singles titles were won by Australians Jack Crawford and Coral McInnes Buttsworth.

1951 Australian Championships: The 1951 Australian Championships was a tennis tournament that took place on outdoor Grass courts at the White City Tennis Club, Sydney, Australia from 20 January to 31 January.  It was the 39th edition of the Australian Championships (now known as the Australian Open), the 11th held in Sydney, and the first Grand Slam tournament of the year.  The singles titles were won by American Dick Savitt and Australian Nancye Wynne Bolton.

Joyce Fitch: Joyce Fitch Rymer (born 3 April 1922) is a former tennis player from Australia who reached the women's singles final of the 1946 Australian Championships, losing to Nancye Wynne Bolton 6–4, 6–4.  She teamed with Mary Bevis Hawton to win the women's doubles title at the 1946 Australian Championships, defeating Bolton and Thelma Coyne Long in the final 9–7, 6–4.  Rymer and Hawton reached the women's doubles final at the 1947 and 1951 Australian Championships, losing both years to the Bolton-Long team.  In 1946, 1947 and 1949 she reached the finals of the Australian Championships in mixed doubles with partner, John Bromwich and again in 1950 with Eric Sturgess, losing all four times.

1962 Australian Championships: The 1962 Australian Championships was a tennis tournament that took place on outdoor Grass courts at the White City Tennis Club, Sydney, Australia from 5 January to 15 January.  It was the 50th edition of the Australian Championships (now known as the Australian Open), the 14th held in Sydney, and the first Grand Slam tournament of the year.  The singles titles were taken by Rod Laver and Margaret Smith.  Laver's win was the first step towards his first Grand Slam.

Question: When was the tennis tournament which has 1951 Australian Championships as the 39th edition first held? 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "tournament_series_name": {
      "type": "string",
      "description": "The current name of the tennis tournament series."
    },
    "first_held_year": {
      "type": "integer",
      "description": "The year the tournament series was first held."
    },
    "referenced_championship": {
      "type": "object",
      "properties": {
        "year": {
          "type": "integer",
          "description": "The year of the specific championship referenced in the question."
        },
        "edition_number": {
          "type": "integer",
          "description": "The edition number of the referenced championship."
        }
      },
      "required": [
        "year",
        "edition_number"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "tournament_series_name",
    "first_held_year",
    "referenced_championship"
  ],
  "additionalProperties": false
}
