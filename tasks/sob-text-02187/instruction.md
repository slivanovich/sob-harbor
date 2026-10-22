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
Clock Tower, Brighton: The Clock Tower (sometimes called the Jubilee Clock Tower) is a free-standing clock tower in the centre of Brighton, part of the English city of Brighton and Hove.  Built in 1888 in commemoration of Queen Victoria's Golden Jubilee, the distinctive structure included innovative structural features and became a landmark in the popular and fashionable seaside resort.  The city's residents "retain a nostalgic affection" for it, even though opinion is sharply divided as to the tower's architectural merit.  English Heritage has listed the clock tower at Grade II for its architectural and historical importance.

Victoria Centre: Intu Victoria Centre, is a shopping centre in Nottingham, England, constructed between 1967 and 1972.

Up All Night: The Live Tour: Up All Night: The Live Tour is a video album documenting the 3 January 2012 show of English-Irish boy band One Direction's "Up All Night Tour".  It was released on 28 May 2012 by Syco Music.  Filmed at the International Centre in the British city of Bournemouth, the 73-minute recording was directed by Andy Saunders and produced by Saunders and Tom Bairstaw.  "Up All Night: The Live Tour" features concert footage and backstage content.

Royal Centre tram stop: Royal Centre is a tram stop of Nottingham Express Transit (NET) in the centre of the city of Nottingham.  It derives its name from the adjacent Theatre Royal and the Royal Concert Hall.  The stop is also close to the Cornerhouse, the Victoria Centre and the Newton Building of Nottingham Trent University, although much of the university's City Campus is closer to the Nottingham Trent University stop.

Grasshopper escapement: The grasshopper escapement is a low-friction escapement for pendulum clocks invented by British clockmaker John Harrison around 1722.  An escapement, part of every mechanical clock, is the mechanism that gives the clock's pendulum periodic pushes to keep it swinging, and each swing releases the clock's gears to move forward by a fixed amount, thus moving the hands forward at a steady rate.  The grasshopper escapement was used in a few regulator clocks built during Harrison's time, and a few others over the years, but has never seen wide use.  The term "grasshopper" in this connection, apparently from the kicking action of the pallets, first appears in the "Horological Journal" in the late 19th century.

Fattorini and Sons: Fattorini & Sons was a jewellery business established by a family of Italian immigrants who arrived in the British city of Leeds, in Yorkshire, England in the early 19th century.  Antonio Fattorini opened a shop in Harrogate to take advantage of seasonal trade in Harrogate in 1831, this business is today owned and run by descendants of the founders.  In the 1850s he opened a shop in Bradford with two of his sons.  In 1883 the firm made the first ever chess clock comprising two linked pendulum clocks.

List of shopping arcades in Cardiff: Shopping arcades in Cardiff include indoor shopping centres and arcades in Cardiff city centre, Wales.  Cardiff is known as the "City of Arcades", due to the highest concentration of Victorian, Edwardian and contemporary indoor shopping arcades in any British city.

Aqua Horological Tintinnabulator: The Aqua Horological Tintinnabulator (also known as the Victoria Centre Clock or the Emett Clock or The Time Fountain is a 'water-powered' clock in Nottingham, England.

St Mark's Clocktower: The Clock Tower in Venice is an early Renaissance building on the north side of the Piazza San Marco, at the entrance to the Merceria.  It comprises a tower, which contains the clock, and lower buildings on each side.  It adjoins the eastern end of the Procuratie Vecchie.  Both the tower and the clock date from the last decade of the 15th century, though the mechanism of the clock has subsequently been much altered.  It was placed where the clock would be visible from the waters of the lagoon and give notice to everyone of the wealth and glory of Venice.  The lower two floors of the tower make a monumental archway into the main street of the city, the Merceria, which linked the political and religious centre (the Piazza) with the commercial and financial centre (the Rialto).  Today it is one of the 11 venues managed by the Fondazione Musei Civici di Venezia.

What Happened to the Corbetts: What Happened to the Corbetts (US title: Ordeal) is a novel by Nevil Shute, a fictional depiction of the effect of aerial bombing on the British city of Southampton, a major maritime centre.  It was written in 1938, and published in April 1939 by William Heinemann Ltd, when the outbreak of World War II was already a very likely development.

Question: The Aqua Horological Tintinnabulator is a water-powered clock in the Victoria Centre in which British city?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "clock_name": {
      "type": "string",
      "description": "The primary name of the clock."
    },
    "alternative_names": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Other names by which the clock is known."
    },
    "location": {
      "type": "object",
      "properties": {
        "city": {
          "type": "string",
          "description": "The city where the clock is located."
        },
        "country": {
          "type": "string",
          "description": "The country where the clock is located."
        }
      },
      "required": [
        "city",
        "country"
      ],
      "additionalProperties": false
    },
    "power_source": {
      "type": "string",
      "description": "The mechanism or source of power for the clock."
    },
    "located_within_building": {
      "type": "string",
      "description": "The name of the building or center where the clock is situated."
    }
  },
  "required": [
    "clock_name",
    "location",
    "power_source",
    "located_within_building"
  ],
  "additionalProperties": false
}
