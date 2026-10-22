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
Giovanni Sirovich: Giovanni Sirovich (born 8 September 1971) is an Italian sabre fencer.  He competed in the men's team sabre at the 1992 Summer Olympics.  He won the gold medal in the 1993 Summer Universiade and the same year a team silver medal in the World Championships.  He became a fencing coach after his retirement as an athlete.  He is now technical director for sabre at the Federazione Italiana Scherma.

Cornel Milan: Cornel Milan (born 8 September 1971) is a Romanian fencer and fencing coach.

Silver Star (NZR train): The Silver Star was a luxury passenger train that ran overnight between Auckland and Wellington on the North Island Main Trunk railway of New Zealand.  The train ran from Monday, 6 September 1971 until Sunday, 8 June 1979.  It replaced the "Night Limited" express passenger trains, which provided a faster service than the "Ordinary" Expresses by stopping at only six intermediate stations en route and not dragging postal or parcels vans at the rear.  Designed as a "hotel on wheels", its carriages were distinctive in New Zealand; rather than being painted in the traditional red, the "Silver Star"' s carriages were made of stainless steel, and silver in appearance.  Original planning of the train envisaged the sleeping cars being the basis of new standard NZR passenger stock with future passenger trains of 6 carriages and van, 7 stainless steel units of 30 tons each (210) tons pulled by a 1425 hp DA.  However planning for the Limited replacement became more ambitious in the early 1960s, moving away from 25 ton, 55 ft stainless carriages of the type used on the 3 ft 6inch, QR Sunlander to sleeping cars of standard gauge 9 ft 9inch, standard gauge loading gauge.  As a result the usual Silver star consist of 35 ton carriages would weigh 410 tons and lead to the order for superpower DX locomotive of 2750 hp from General Electric to pull them and express freight on the NIMT and result in a large trackside work on the NIMT and the Silver stars alternative route via Marton- Wanganu-Stratford - Taurmaranui, to accommodate standard gauge width carriages running on 3 ft 6 inch.

Richard Van Camp: Richard Van Camp (born 8 September 1971) is a Tłı̨chǫ writer from Fort Smith, Northwest Territories.  He is best known for his 1996 novel "The Lesser Blessed", which was adapted into a film by director Anita Doron in 2012.

Martin Freeman: Martin John Christopher Freeman (born 8 September 1971) is an English actor, who became known for portraying Tim Canterbury in the original UK version of sitcom mockumentary "The Office", Dr. John Watson in the British crime drama "Sherlock", Bilbo Baggins in Peter Jackson's "The Hobbit" film trilogy, and Lester Nygaard in the dark comedy-crime drama TV series "Fargo".

Martin Doktor (footballer): Martin Doktor (born 26 September 1981 in Ilava – died 8 September 2004 in Dubodiel) was a Slovak football midfielder, who played as a midfielder.  He died of congestive heart failure during the night of 7 to 8 September 2004, as the official date of death is given 8 September 2004.

Vladimir Epifantsev: Vladimir Georrievich Epifantsev (Russian: Владимир Георгиевич Епифанцев ; born 8 September 1971 Moscow USSR) is a Russian theatre and cinema actor, filmmaker, television presenter and music video director.

Gillian van den Berg: Gillian van den Berg (born 8 September 1971, in Gouda) is a water polo player of the Netherlands who represents the Dutch national team in international competitions.

The Good Night: The Good Night is a 2007 romantic comedy film written and directed by Jake Paltrow.  The film stars his sister Gwyneth Paltrow, Penélope Cruz, Martin Freeman, Danny DeVito, Simon Pegg and others.  The movie takes place in London and New York City, where a former pop star (Freeman) who now writes commercial jingles for a living experiences a mid-life crisis.

Reece Mastin: Reece Mastin (born 24 November 1994) is an English-born Australian singer and songwriter who won the third season of "The X Factor Australia" in 2011.  Mastin subsequently signed with Sony Music Australia.  His debut single "Good Night" reached number one in Australia and New Zealand, and became Sony Music Australia's fastest selling digital single.  Mastin's self-titled debut album debuted at number two on the ARIA Albums Chart and was certified double platinum.  His second studio album "Beautiful Nightmare" (2012) included the hit singles "Shut Up & Kiss Me" and "Shout It Out", the latter became Mastin's second number-one single in Australia.  "Good Night" and "Shout It Out" earned him two ARIA No. 1 Chart Awards.  In 2015, Mastin parted ways with Sony and signed with independent label Social Family Records.  His third studio album "Change Colours" was released in October 2015, and debuted at number 12.

Question: Which star of the movie the Good Night was born on 8 September 1971 ?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the person."
    },
    "birth_date": {
      "type": "string",
      "format": "date",
      "description": "The birth date of the person in YYYY-MM-DD format."
    },
    "movie_details": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the movie."
        },
        "release_year": {
          "type": "integer",
          "description": "The release year of the movie."
        }
      },
      "required": [
        "title",
        "release_year"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "person_name",
    "birth_date",
    "movie_details"
  ],
  "additionalProperties": false
}
