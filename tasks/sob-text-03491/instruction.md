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
Unto the Sons: Unto the Sons is a 1992 book by Gay Talese.  The book traces the origins of Talese's own family, beginning with his great-grandfather in Maida, Italy, his grandfather who immigrated to Pennsylvania and Talese's father, who immigrated to the United States separately following World War I.

Gay Talese: Gay Talese ( ; born February 7, 1932) is an American writer.  As a journalist for "The New York Times" and "Esquire" magazine during the 1960s, Talese helped to define literary journalism.  Talese's most famous articles are about Joe DiMaggio and Frank Sinatra.

Buckminster Fuller: Thinking Out Loud: Buckminster Fuller: Thinking Out Loud (1996) is a PBS "American Masters" documentary on the inventor, visionary, and thinker R. Buckminster Fuller produced and directed by Academy Award nominees Karen Goodman and Kirk Simon.  Cinematography by Buddy Squires, edited by Sara Fishko, and a production of Simon & Goodman Picture Company.

R. Buckminster Fuller and Anne Hewlett Dome Home: The R. Buckminster Fuller and Anne Hewlett Dome Home, located at 407 S. Forest Ave. in Carbondale, Illinois, is a geodesic dome house which was the residence of Buckminster Fuller from 1960 to 1971.  The house, inhabited by Fuller while he taught at Southern Illinois University, was the only geodesic dome Fuller lived in as well as the only property he ever owned.  Fuller, a prolific architect and engineer, popularized the geodesic dome as a building design, and his house was one of the first geodesic dome residences to be constructed.  The home was built and designed by Al Miller of the Pease Woodworking Company.  While living in the home, Fuller was awarded nine patents, published eleven books, and designed the Montreal Biosphère, one of his most famous works.

Buckminster Fuller Challenge: The Buckminster Fuller Challenge is an annual international design competition that awards $100,000 to the most comprehensive solution to a pressing global problem.  The Challenge was launched in 2007 and is a program of The Buckminster Fuller Institute.  The competition, open to designers, artists, architects, students, environmentalists, and organizations world-wide, has been dubbed "Socially-Responsible Design's Highest Award" by Metropolis Magazine.

The Last Dymaxion: The Last Dymaxion: Buckminster Fuller’s Dream Restored is a 2012 documentary film directed by Noel Murphy.  about Buckminster Fuller's 1933 Dymaxion car as well as Fuller himself.

J. Baldwin: James Tennant Baldwin (born 1933) (whose books and articles have been published under the names J. Baldwin, Jay Baldwin, and James T. Baldwin) is an American industrial designer and writer.  Baldwin was a student of Buckminster Fuller; Baldwin's work has been inspired by Fuller's principles and (in the case of some of Baldwin's published writing) has popularized and interpreted Fuller's ideas and achievements.  In his own right, Baldwin has been a figure in American designers' efforts to incorporate solar, wind, and other renewable sources of energy.  In his career, being a fabricator has been as important as being a designer.  Baldwin is noted as the inventor of the "Pillow Dome," a design that combines Buckminster Fuller's geodesic dome with panels of inflated ETFE plastic panels.

Buckminster Fuller: Richard Buckminster "Bucky" Fuller ( ; July 12, 1895 – July 1, 1983) was an American architect, systems theorist, author, designer, and inventor.

Frank Sinatra Has a Cold: "Frank Sinatra Has a Cold" is a profile of Frank Sinatra written by Gay Talese for the April 1966 issue of "Esquire".  The article is one of the most famous pieces of magazine journalism ever written and is often considered not only the greatest profile of Frank Sinatra but one of the greatest celebrity profiles ever written.  The profile is one of the seminal works of New Journalism and is still widely read, discussed and studied.  In the 70th anniversary issue of "Esquire" in October 2003, the editors declared the piece the "Best Story Esquire Ever Published".  "Vanity Fair" called it "the greatest literary-nonfiction story of the 20th century".

The Kingdom and the Power: The Kingdom and the Power: Behind the Scenes at The New York Times: The Institution That Influences the World is a 1969 book by Gay Talese about the inner workings of "The New York Times", the newspaper where Talese had worked for 12 years.  The book was originally subtitled "The Story of The Men Who Influence The Institution That Influences the World."  The book is credited with starting the trend of "media books" as noted by "Portfolio" at the New York University School of Journalism, books that "portraying the inner-workings of a media establishment, turning the tables on the people who write and report the news, and making them the subject."

Question: Who helped more to define literary journalism, Buckminster Fuller or Gay Talese?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_who_defined_literary_journalism": {
      "type": "string",
      "description": "The name of the person who helped define literary journalism."
    },
    "contribution_description": {
      "type": "string",
      "description": "A description of how the person contributed to literary journalism."
    },
    "other_person_mentioned": {
      "type": "string",
      "description": "The name of the other person mentioned in the comparison."
    },
    "other_person_contribution_to_literary_journalism": {
      "type": "string",
      "description": "A statement about the other person's contribution to literary journalism based on the context."
    }
  },
  "required": [
    "person_who_defined_literary_journalism",
    "contribution_description",
    "other_person_mentioned",
    "other_person_contribution_to_literary_journalism"
  ],
  "additionalProperties": false
}
