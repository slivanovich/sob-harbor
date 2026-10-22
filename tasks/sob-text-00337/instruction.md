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
St. Anthony Messenger: St. Anthony Messenger is a national Roman Catholic family magazine published by the Franciscan Friars (O.F.M.) of St. John the Baptist Province, Cincinnati, Ohio in the United States, with the explicit ecclesiastical approval of the Archbishop of Cincinnati.

The New Journal: The New Journal is a magazine at Yale University that publishes creative nonfiction about Yale and New Haven.  Inspired by New Journalism writers like Tom Wolfe and Gay Talese, the student-run publication was established by Daniel Yergin and Peter Yeager in 1967 to publish investigative pieces and in-depth interviews.  It publishes five issues per year.  The magazine is distributed free of charge at Yale and in New Haven and was among the first university publications not to charge a subscription fee.

John Hersey: John Richard Hersey (June 17, 1914 – March 24, 1993) was an American writer and journalist.  He is considered one of the earliest practitioners of the so-called New Journalism, in which storytelling techniques of fiction are adapted to non-fiction reportage.  Hersey's account of the aftermath of the atomic bomb dropped on Hiroshima, Japan, was adjudged the finest piece of American journalism of the 20th century by a 36-member panel associated with New York University's journalism department.

New York (magazine): New York is an American biweekly magazine concerned with life, culture, politics, and style generally, and with a particular emphasis on New York City.  Founded by Milton Glaser and Clay Felker in 1968 as a competitor to "The New Yorker", it was brasher and less polite, and established itself as a cradle of New Journalism.  Over time, it became more national in scope, publishing many noteworthy articles on American culture by writers such as Tom Wolfe, Jimmy Breslin, Nora Ephron, John Heilemann, Frank Rich, and Rebecca Traister.

Franciscan Media: Franciscan Media, formerly St. Anthony Messenger Press, is a multimedia company comprising "St. Anthony Messenger" magazine, Franciscan Media and Servant books, Catholic Greetings, Saint of the Day, Minute Meditations, and AmericanCatholic.org, used by millions of people, primarily in the United States, but also worldwide.

St. Anthony of Padua Church (Manhattan): The Church of St. Anthony of Padua is a Catholic parish church in the Roman Catholic Archdiocese of New York, located at 155 Sullivan Street near the corner of West Houston Street, in the South Village section of the Greenwich Village neighborhood of Manhattan, New York City.  It was established in 1859 as the first parish in the United States formed specifically to serve the Italian immigrant community.

Bon Secours Charity Health System: The Bon Secours Charity Health System, part of the Bon Secours Health System, was established from a partnership between the Sisters of Bon Secours and the Sisters of Charity of Saint Elizabeth of Convent Station, New Jersey.  The system includes: Good Samaritan Regional Medical Center in Suffern, New York, Bon Secours Community Hospital in Port Jervis, New York and St. Anthony Community Hospital in Warwick, New York.

Saints Roch, Anthony Abbot and Lucy: Saints Roch, Anthony Abbot and Lucy or Three Saints is a 1513 oil on panel painting by Cima da Conegliano, now in the Metropolitan Museum of Art in New York.  It was painted in Parma, where it may have provided one of the inspirations for Correggio's "Four Saints".  As its name suggests, it shows saint Anthony Abbot flanked by saint Roch and saint Lucy.  Since St Anthony is in the centre and since St Roch is a patron saint of plague sufferers, it may have been commissioned for the Hospital Brothers of St. Anthony, who ministered to plague victims.  It was later misattributed to Giovanni Bellini and as such was owned by Josephine Bonaparte.

St. Anthony's Church (Pine Plains, New York): The Church of St. Anthony is a Roman Catholic parish church under the authority of the Roman Catholic Archdiocese of New York, located in Pine Plains, Dutchess County, New York.  It was originally established as mission of Immaculate Conception Parish in Amenia in 1913, and was elevated to parish status in 1958.

Good Samaritan Regional Medical Center (Suffern): Good Samaritan Community Hospital is a non-profit, 286-bed hospital located in Suffern, New York, providing services to the residents of Rockland County and southern Orange County in New York, and northern Bergen County in New Jersey.  The hospital also serves these communities as a Level II Trauma Center.  Good Samaritan Regional Medical Center is a member of the Bon Secours Charity Health System, which also includes St. Anthony Community Hospital in Warwick, New York, and Bon Secours Community Hospital in Port Jervis, New York.  The Bon Secours Charity Health System has subsequently become part of the WMCHealth Network.  The hospital currently has a staff of more than 600 doctors and 2000 employees.  Its academic affiliate is the New York Medical College School of Medicine.

Question: Which magazine established itself as a cradle of New Journalism, St. Anthony Messenger or New York?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "magazine_name": {
      "type": "string",
      "description": "The name of the magazine that established itself as a cradle of New Journalism."
    },
    "established_as_cradle_of_new_journalism": {
      "type": "boolean",
      "description": "Indicates whether the magazine established itself as a cradle of New Journalism."
    },
    "related_journalism_movement": {
      "type": "string",
      "description": "The specific journalism movement mentioned in the context."
    },
    "founding_details": {
      "type": "object",
      "properties": {
        "founders": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "The names of the founders of the magazine."
        },
        "founding_year": {
          "type": "integer",
          "description": "The year the magazine was founded."
        }
      },
      "required": [
        "founders",
        "founding_year"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "magazine_name",
    "established_as_cradle_of_new_journalism",
    "related_journalism_movement",
    "founding_details"
  ],
  "additionalProperties": false
}
