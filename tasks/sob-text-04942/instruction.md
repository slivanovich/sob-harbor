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
Europe's Strongest Man: Europe's Strongest Man is an annual strength athletics competition which began in 1980.  The event is held in various locations throughout Europe, and features exclusively European strongman competitors.  Mariusz Pudzianowski currently holds the record for most wins with 6 titles.  Zydrunas Savickas, Geoff Capes, Riku Kiri and Hafþór Júlíus Björnsson each hold 3 titles.  As of 2010, the Europe's Strongest Man contest has become a part of the Giants Live season of annual grand prix events.  The contest serves as a qualifying event for the World's Strongest Man contest, with the top 3 placings qualifying for that year's WSM contest.

2013 World's Strongest Man: The 2013 World's Strongest Man was the 36th edition of World's Strongest Man.  The event was held in Haitang Bay, Sanya, China, the same host city as the 2006 World's Strongest Man contest.  The qualifying heats were held from August 17–20 and the finals on Aug. 23 & 24.  The event was sponsored by the Commerce Casino and will be broadcast in the United States on the CBS Sports Network.  Brian Shaw from the United States placed first, winning his second WSM title after winning in 2011.  Zydrunas Savickas from Lithuania was second after finishing 1st the year before, and Hafþór Júlíus Björnsson from Iceland was third for the second year in a row.

The Strongest Man in the World: The Strongest Man in the World is a 1975 Disney film starring Kurt Russell, still a student in the fictional Medfield College.  It is the sequel to the 1972 film "Now You See Him, Now You Don't", itself a sequel to the 1969 film, "The Computer Wore Tennis Shoes".

Eddie Hall: Edward Hall (born 15 January 1988) is an English professional strongman, notable for being the current World's Strongest Man and the only man to deadlift 500 kg under strongman rules.  He has also won on multiple occasions both the UK's Strongest Man and England's Strongest Man titles.  He is the 2017 World's Strongest Man and the current world record holder in the deadlift with straps.

1980 World's Strongest Man: The 1980 World's Strongest Man was the fourth edition of World's Strongest Man and was won by Bill Kazmaier from the United States.  It was his first title after finishing third the previous year.  Lars Hedlund from Sweden finished second after finishing second the previous year, and Geoff Capes from the United Kingdom finished third.  Defending champion Don Reinhoudt withdrew from the competition due to injury; this would be his final World's Strongest Man.

Tuxedo Gin: Tuxedo Gin (タキシード銀 , Takishiido Gin ) is a romantic comedy manga series by Tokihiko Matsuura.  It was published by Shogakukan in "Shōnen Sunday" from 1997 to 2000 and collected in 15 bound volumes.  It is published North America in English by Viz Communications.  The series is about a teenaged boxer named Ginji Kusanagi who is reincarnated as a penguin in order to be close to the girl he likes.  On August 4, 2011, Walt Disney Pictures and Viz Pictures announced they were adapting the Tuxedo Gin manga into a feature film under the name, "Tux".

Ben Kelsey (strongman): Ben Kelsey (born 23 September 1984) is a British strongman competitor, notable for having won the England's Strongest Man title, the title of World's Strongest Man Under 105 kg and having competed at the World's Strongest Man.

All-American Strongman Challenge: The All-American Strongman Challenge is a leading competition in strength athletics that takes place within the annual Californian FitExpo.  Although North America has a number of prestigious strongman events determining the "Strongest Man in America", the "Strongest Man in Canada" and the "Strongest Man in North America", the All-American Strongman Challenge has added kudos because it is open to entrants from overseas with the potential to bring in leading international competitors as well.  It is notable for the calibre of entrants it has attracted, with many World's Strongest Man finalists being represented.

Robert Oberst: Robert Oberst (born December 20, 1984) is an American professional strongman who was awarded his "Pro Card" at the 2012 Dallas Europa Amateur Strongman Competition.  He is a yearly competitor of the World's Strongest Man including the 2013 World's Strongest Man, 2014 World's Strongest Man, 2015 World's Strongest Man and the 2016 World's Strongest Man competitions.

2014 World's Strongest Man: The 2014 World's Strongest Man was the 37th edition of World's Strongest Man.  The event was held at the Commerce Casino in Los Angeles, California, the same host city as the 2012 World's Strongest Man contest.  The qualifying heats were held from March 22–25 and the finals on March 28 & 29.  Unlike previous years when 10 athletes qualified for the finals, this year there were 12 qualifying spots.  The top 2 from each heat qualified, as well as the 2 highest scoring 3rd place athletes from all 5 heats.  The event was sponsored by the Commerce Casino and will begin broadcasting in the United States on the CBS Sports Network from July 4-August 13, 2014.  Zydrunas Savickas from Lithuania finished in first place, this was his fourth WSM title.  Hafþór Júlíus Björnsson from Iceland finished in second place, and Brian Shaw from the United States came in third.

Question: TuxWhich film was most recent, "The Strongest Man in the World" or "Tux" which is based on the manga series "Tuxedo Gin"?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "most_recent_film_title": {
      "type": "string",
      "description": "The title of the film that was most recently released."
    },
    "most_recent_film_release_year": {
      "type": "integer",
      "description": "The release year of the most recent film."
    },
    "films_compared": {
      "type": "array",
      "description": "Details of the films that were compared.",
      "items": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the film."
          },
          "release_year": {
            "type": "integer",
            "description": "The release or announcement year of the film."
          }
        },
        "required": [
          "title",
          "release_year"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "most_recent_film_title",
    "most_recent_film_release_year",
    "films_compared"
  ],
  "additionalProperties": false
}
