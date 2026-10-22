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
The 1989 World Tour: The 1989 World Tour was the fourth concert tour by American singer-songwriter Taylor Swift, in support of her fifth studio album, "1989" (2014).  The tour's European and North American dates, as well as two shows in Japan, were announced in November 2014, followed by the Oceania dates in December 2014.  Additional dates for Singapore and Shanghai were announced in June 2015 with a third and final Melbourne show announced in July 2015.  The tour began on May 5, 2015, in Tokyo, Japan and concluded on December 12, 2015 in Melbourne, Australia, the day before her 26th birthday.  The tour became Swift's highest grossing and most attended tour to date, mobilizing 2,278,647 fans and $250,733,097 revenue.  It was the highest grossing tour in the world in 2015.

Victory Tour (The Jacksons tour): The Victory Tour was a concert tour of the United States and Canada by Michael Jackson and The Jackson family between July and December 1984.  It was the first and only tour with all six Jackson brothers (even though Jackie was injured for most of the tour).  The group performed 55 concerts to an audience of approximately 2 million.  Most came to see Michael, whose album "Thriller" was dominating the popular music world at the time.  Many consider it to be his "Thriller" tour, with most of the songs on the set list coming off of his "Off the Wall" album and from the "Thriller" album.  The tour reportedly grossed approximately $75 million (US$ in 2016 dollars ) and set a new record for the highest grossing tour.  It showcased Michael's single decorated glove, black sequined jacket and moonwalk.

Loud Tour: The Loud Tour was the fourth overall and third world concert tour by Barbadian recording artist Rihanna.  Performing in over twenty countries in the Americas and Europe, the tour was launched in support of Rihanna's fifth studio album "Loud" (2010) but eventually supported her following album "Talk that Talk" as it was released during the tour, in November 2011.  Critics acclaimed the show for its liveliness and higher caliber of quality when compared to Rihanna's previous tours.  The Loud Tour was a large commercial success, experiencing demand for an extension of shows in the United Kingdom due to popularity.  In London, Rihanna played a record breaking 10 dates at The O2 Arena.  The tour ultimately grossed an estimated value of US$90 million from 98 reported shows and a total audience of 1,200,800.  The Loud Tour became the 7th highest grossing tour of 2011.

Voodoo Lounge Tour: The Voodoo Lounge Tour was a worldwide concert tour by The Rolling Stones to promote their 1994 album "Voodoo Lounge".  This was their first tour without bassist Bill Wyman, and their first with touring bassist Darryl Jones.  The tour grossed $320 million, replacing Pink Floyd's "Division Bell" tour as the highest grossing of any artist at that time.  This was subsequently overtaken by a few other tours, but it remains The Rolling Stones' second highest grossing tour behind their 2005–2007 A Bigger Bang Tour.

A Bailar Tour: The A Bailar Tour was the first headlining concert tour by Argentine recording artist Lali in support of her debut studio album, "A Bailar" (2014).  The tour began in Buenos Aires, Argentina on April 19, 2014 and concluded in Tel Aviv, Israel on April 25, 2016.  The "A Bailar Tour" was the highest grossing tour of 2015 in Argentina.

No Strings Attached Tour: The No Strings Attached Tour was the third concert tour by American boy band, NSYNC.  Primarily visiting North America, the tour supported the band's second studio album, "No Strings Attached".  Beginning in May 2000, the tour sold out all dates within the first day of the ticket sale.  Additional dates in North America were added for the Fall of 2000.  When the tour ended in December 2000, it became the second highest grossing tour in North America, earning more than $70 million.

Bad (tour): Bad was the first solo concert tour by American recording artist Michael Jackson, launched in support of his seventh studio album "Bad" (1987).  Sponsored by Pepsi and spanning 16 months, the tour included 123 concerts to 4.4 million fans across 15 countries making it the second highest grossing tour of the 80s.  When the tour concluded it grossed a total of $125 million, adding two new entries in the "Guinness World Records" for the largest grossing tour in history and the tour with the largest attended audience.  In April 1989, the tour was nominated for "Tour of the Year 1988" at the inaugural International Rock Awards.

Ronan (song): "Ronan" is a charity single released on September 8, 2012, by American singer Taylor Swift to the iTunes Store.  Swift's lyrics are based on a blog she read about a four-year-old boy, Ronan Thompson, who died from neuroblastoma in 2011.  Swift wrote the song by putting together quotes from blog creator Maya Thompson, Ronan's mother.  Thompson is credited as a co-writer of the song.  Swift first performed the song live for Stand Up to Cancer in September 2012, and has only performed it publicly one other time, at the Glendale, Arizona stop of The 1989 World Tour, at which Thompson was in attendance.  All proceeds from sales of the single go to help fight cancer.

The Police Reunion Tour: The Reunion Tour was a 2007–2008 worldwide concert tour by The Police, marking the 30th anniversary of their beginnings.  At its conclusion, the tour became the third (now seventh) highest grossing tour of all time, with revenues reaching over $360 million.  The tour began in May 2007 to overwhelmingly positive reviews from fans and critics alike and ended in August 2008 with a final show at Madison Square Garden.

Crazy Love Tour: Crazy Love Tour was the fourth concert tour by Canadian singer Michael Bublé.  The tour supported his sixth studio album, "Crazy Love".  Visiting the Americas, Europe, Australia, Asia, and Africa, the tour has played to over one million spectators in nearly 21 countries.  The tour has received remarkable praise from both music critics and spectators of the show.  In 2010, Pollstar announced the trek became the sixth highest grossing tour worldwide, earning over $100 million with 99 sold out shows.  Additionally was the fourth highest grossing tour in North America—bringing in over $60 million in revenue with 50 sold out shows.  The tour ranked 16th in Pollstar's "Top 50 Worldwide Tour (Mid-Year)", earning over 30 million dollars in 2011.  At the conclusion of 2011, the tour placed eleventh on Billboard's annual "Top 25 Tours", earning nearly $50 million with 57 shows in 2011.

Question: Which artist performed at Stand Up to Cancer, and had the highest grossing tour in the world in 2015

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "artist_name": {
      "type": "string",
      "description": "The name of the artist."
    },
    "highest_grossing_tour_2015": {
      "type": "object",
      "properties": {
        "tour_name": {
          "type": "string",
          "description": "The name of the tour that was the highest grossing in 2015."
        },
        "gross_revenue_usd": {
          "type": "integer",
          "description": "The total revenue of the tour in USD."
        },
        "year_of_achievement": {
          "type": "integer",
          "description": "The year the tour was the highest grossing worldwide."
        }
      },
      "required": [
        "tour_name",
        "gross_revenue_usd",
        "year_of_achievement"
      ],
      "additionalProperties": false
    },
    "charity_performance": {
      "type": "object",
      "properties": {
        "event_name": {
          "type": "string",
          "description": "The name of the charity event where the artist performed."
        },
        "performance_year": {
          "type": "integer",
          "description": "The year of the charity performance."
        }
      },
      "required": [
        "event_name",
        "performance_year"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "artist_name",
    "highest_grossing_tour_2015",
    "charity_performance"
  ],
  "additionalProperties": false
}
