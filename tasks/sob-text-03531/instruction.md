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
Delta (TV series): Delta is an American sitcom starring Delta Burke that aired on ABC from September 15, 1992 to August 25, 1993.  The series was a new starring vehicle for Burke, as her return to television following her dismissal from the CBS sitcom "Designing Women" in the spring of 1991.

The Designing Women Reunion: The Designing Women Reunion is a 2003 American television special celebrating the 1986–1993 sitcom "Designing Women" starring Dixie Carter, Annie Potts, Delta Burke, Jean Smart and Meshach Taylor.  It originally aired on Lifetime on July 28, 2003.

Filthy Rich (1982 TV series): Filthy Rich was an American sitcom that aired on CBS from August 1982 to July 1983.  Starring Dixie Carter and Delta Burke, the series satirized prime-time soap operas such as "Dallas" and "Dynasty".

The New Gidget: The New Gidget is an American sitcom sequel to the original 1965–66 sitcom "Gidget" that aired in syndication from September 15, 1986 to May 12, 1988.  The series was produced by original "Gidget" series producer Harry Ackerman and was launched after the made-for-television film "Gidget's Summer Reunion", starring Caryn Richman as Gidget, aired in 1985.

Pacific Station (TV series): Pacific Station is an American sitcom starring Robert Guillaume and Richard Libertini that aired on NBC from September 15, 1991 to January 3, 1992.  The series was created by the team of Barry Fanaro, Mort Nathan, Kathy Speer and Terry Grossman.

Alan Burke: Alan S. Burke (September 15, 1922 – August 25, 1992) was an American conservative television and radio talk show host who was on the air primarily in New York City from 1966 to 1969 on WNEW (now Fox Broadcasting O&O WNYW).

Women of the House: Women of the House is an American sitcom and a spin-off of "Designing Women" that aired on CBS from January 4, 1995 to August 18, 1995 and the last four episodes airing on Lifetime on September 8, 1995.  The series starred Delta Burke, reprising her role of Suzanne Sugarbaker, who had reconciled with producers of "Designing Women" after a bitter, highly publicized, off-screen battle.

Delta Burke: Delta Ramona Leah Burke (born July 30, 1956) is an American television, stage and film actress, producer and author.  From 1986 to 1991, she starred as Suzanne Sugarbaker in the CBS sitcom "Designing Women", for which she was nominated for two Emmy Awards for Outstanding Lead Actress in a Comedy Series.

The Tycoon (TV series): The Tycoon is a 32-episode American sitcom television series broadcast by ABC.  It starred Walter Brennan as the fictitious businessman Walter Andrews, similar to his birth name of Walter Andrew Brennan.  As chairman of the board of the Thunder Corporation that he founded but no longer actively runs, Brennan plays an eccentric and cantankerous millionaire (when such persons were much fewer in number) with a common touch who helps promising persons in need.  The series aired with new episodes at 9 p.m. Eastern time Tuesday from September 15, 1964, until April 27, 1965.  It continued in reruns until September 7, 1965.  The program did not develop sufficient audience, presumably because viewers may have preferred the versatile Brennan as the bucolic Grandpa Amos McCoy in his 1957-1963 ABC and CBS sitcom "The Real McCoys".  Oddly, "The Tycoon" has the same name as an episode of "The Real McCoys" also called "The Tycoon," which aired four years earlier on August 23, 1960.

Joey King: Joey Lynn King (born July 30, 1999) is an American actress.  She is known for her starring role as Ramona Quimby in "Ramona and Beezus", the 2010 adaptation of Beverly Cleary's book series with the same title.  She has also appeared in the films "Oz the Great and Powerful", "The Conjuring" and "White House Down".

Question: Delta is an American sitcom, that aired on which station, from September 15, 1992 to August 25, 1993, starring Delta Ramona Leah Burke (born July 30, 1956) is an American television, stage and film actress, producer and author?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "series_name": {
      "type": "string",
      "description": "The name of the television series."
    },
    "network": {
      "type": "string",
      "description": "The television network on which the series aired."
    },
    "starring_actress": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The full name of the starring actress."
        },
        "birth_date": {
          "type": "string",
          "format": "date",
          "description": "The birth date of the starring actress."
        }
      },
      "required": [
        "name",
        "birth_date"
      ],
      "additionalProperties": false
    },
    "air_dates": {
      "type": "object",
      "properties": {
        "start_date": {
          "type": "string",
          "format": "date",
          "description": "The date the series began airing."
        },
        "end_date": {
          "type": "string",
          "format": "date",
          "description": "The date the series stopped airing."
        }
      },
      "required": [
        "start_date",
        "end_date"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "series_name",
    "network",
    "starring_actress",
    "air_dates"
  ],
  "additionalProperties": false
}
