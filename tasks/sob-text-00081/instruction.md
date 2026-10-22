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
Brian Stann: Brian Michael Stann (born September 24, 1980) is a retired American mixed martial artist and U.S. Marine who competed as a Middleweight in the Ultimate Fighting Championship (UFC).  He is a former WEC Light Heavyweight Champion.  Stann is President and CEO of Hire Heroes USA, a nonprofit organization that helps U.S. military veterans.  He was also a color commentator for both the Ultimate Fighting Championship and ACC football games on Fox Sports Net.

Brian Ortega: Brian Ortega (born February 21, 1991) is an American mixed martial artist currently competing in the Featherweight division of the Ultimate Fighting Championship.  A professional competitor since 2010, he has also formerly competed for the RFA, where he was the Featherweight Champion.  He currently fights in the UFC featherweight division.

Ricardo Lamas: Ricardo Alejandro Lamas (born May 21, 1982) is an American mixed martial artist who currently fights as a Featherweight in the Ultimate Fighting Championship organization.  He trains with local powerhouse MMA Masters in Miami, Florida and Team Top Notch in Villa Park, Illinois.  In December 2013, Lamas was awarded his black belt in Brazilian Jiu-jitsu under 2007 World Nogi Jiu Jitsu champion and owner of MMA Masters Daniel Valverde.  As of May 31, 2016, he is #5 in the official UFC featherweight rankings and ranked the #3 featherweight in the world by Sherdog.

Urijah Faber: Urijah Christopher Faber (born May 14, 1979) is an American retired mixed martial artist who fought as a bantamweight and featherweight in the Ultimate Fighting Championship.  Faber won the WEC Featherweight Championship at "WEC 19" on March 17, 2006, and held the title for over two years until losing it to Mike Brown at "WEC 36" on November 5, 2008.  Faber is widely regarded as one of the sport's pioneers for establishing legitimacy to lighter weight classes in MMA.

Gilbert Melendez: Gilbert "El Niño" Melendez (born April 12, 1982) is an American mixed martial artist who has fought at Featherweight and currently fights at featherweight in the Ultimate Fighting Championship (UFC).  He is a two-time Strikeforce Lightweight Champion and a former WEC Lightweight Champion.  He also competed in PRIDE FC, Shooto and Rumble on the Rock.

José Aldo: José Aldo da Silva Oliveira Junior (] ; born September 9, 1986) is a Brazilian mixed martial artist in the Ultimate Fighting Championship.  He was the fourth and final WEC Featherweight Champion and thus, became the first UFC Featherweight Champion during the UFC/WEC merger.  He is a former two-time UFC Featherweight Champion.  He was named Sherdog's 2009 Fighter of the Year.  He is currently #12 in official UFC pound-for-pound rankings, having been ranked as high as #1 in 2015, and ranked the #2 featherweight in the world and #7 pound-for-pound by Sherdog.  In the decade from November 2005 through December 2015, Aldo was undefeated in 18 fights.  In Sherdog's April 2017 Pound-For-Pound ranking, Aldo was called "the greatest featherweight in mixed martial arts history."

Joseph Benavidez: Joseph Rolando Benavidez (born July 31, 1984) is an American mixed martial artist.  After fighting in smaller shows while working as a screen printer in Las Cruces, New Mexico, he joined up with Urijah Faber's Team Alpha Male in 2007.  He has since fought in Dream and more recently the World Extreme Cagefighting promotion.  He currently fights as a flyweight in the Ultimate Fighting Championship.  His fighting style has drawn comparisons to training partner and former WEC Featherweight Champion Urijah Faber.  As of February 6, 2017, he is #1 in the official UFC flyweight rankings and ranked the #2 flyweight in the world by Sherdog.  On April 27, 2010, the Mayor and City Council of the City of Las Cruces proclaimed April 27 as Joseph Benavidez Day in Las Cruces.

Erik Koch: Erik Jon Koch (born October 4, 1988) is an American mixed martial artist who currently fights as a Lightweight in the Ultimate Fighting Championship.  A professional competitor since 2007, he formerly competed for the WEC.

Rick Glenn: Rick "The Gladiator" Glenn (born April 12, 1989) is an American mixed martial artist.  He was the Professional Fighters League (formerly known as World Series of Fighting (WSOF) ) featherweight champion and Midwest Cage Fight featherweight champion.  Glenn currently fights in Featherweight division in the Ultimate Fighting Championship (UFC).

Bendy Casimir: He made his WEC debut against Ricardo Lamas on March 6, 2010 at WEC 47, losing via first-round knockout.

Question: Bendy Casimir, made his WEC debut on March 6, 2010 at WEC 47, losing via first-round knockout, against which American mixed martial artist who currently fights as a Featherweight in the Ultimate Fighting Championship organization?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "opponent_name": {
      "type": "string",
      "description": "The full name of the American mixed martial artist who fought Bendy Casimir."
    },
    "opponent_nationality": {
      "type": "string",
      "description": "The nationality of the opponent."
    },
    "opponent_current_organization": {
      "type": "string",
      "description": "The organization the opponent currently fights for."
    },
    "opponent_current_weight_class": {
      "type": "string",
      "description": "The weight class the opponent currently fights in."
    },
    "match_details": {
      "type": "object",
      "properties": {
        "event_name": {
          "type": "string",
          "description": "The name of the WEC event where the debut occurred."
        },
        "event_date": {
          "type": "string",
          "format": "date",
          "description": "The date of the WEC debut match."
        },
        "casimir_result": {
          "type": "string",
          "description": "The outcome for Bendy Casimir in the match."
        },
        "method_of_loss": {
          "type": "string",
          "description": "The method by which Bendy Casimir lost."
        },
        "round_of_loss": {
          "type": "string",
          "description": "The round in which Bendy Casimir lost."
        }
      },
      "required": [
        "event_name",
        "event_date",
        "casimir_result",
        "method_of_loss",
        "round_of_loss"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "opponent_name",
    "opponent_nationality",
    "opponent_current_organization",
    "opponent_current_weight_class",
    "match_details"
  ],
  "additionalProperties": false
}
