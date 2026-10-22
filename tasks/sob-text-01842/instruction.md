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
Raiders of the Lost Ark: Raiders of the Lost Ark (also known as Indiana Jones and the Raiders of the Lost Ark) is a 1981 American action adventure film directed by Steven Spielberg, with a screenplay written by Lawrence Kasdan, from a story by George Lucas and Philip Kaufman.  It was produced by Frank Marshall for Lucasfilm Ltd., with Lucas and Howard Kazanjian as executive producers.  Starring Harrison Ford, it was the first installment in the "Indiana Jones" film franchise to be released, though it is the second in internal chronological order.  It pits Indiana Jones (Ford) against a group of Nazis who are searching for the Ark of the Covenant, which Adolf Hitler believes will make his army invincible.  The film co-stars Karen Allen as Indiana's former lover, Marion Ravenwood; Paul Freeman as Indiana's rival, French archaeologist René Belloq; John Rhys-Davies as Indiana's sidekick, Sallah; Ronald Lacey as Gestapo agent Arnold Toht; and Denholm Elliott as Indiana's colleague, Marcus Brody.

Chris Enss: Chris Enss (born 1961) is an American author and screenwriter.  Enss has written more than 20 books on the subject of women in the Old West, and has collaborated with producer Howard Kazanjian on four books, including two about Roy Rogers and Dale Evans.

Harkness Ballet: The Harkness Ballet (1964–1975) was a New York ballet company named after its founder Rebekah Harkness.  Ms. Harkness inherited her husband's fortune in Standard Oil holdings and was a dance lover.  Ms. Harkness funded Joffrey Ballet, but when they refused to rename the company in her honour, she withdrew funding and hired most of the Joffery dancers for her new company.  Joffery Ballet later moved to Chicago, and continues to function.  Harkness Ballet, established in 1964, gave its debut performance in Cannes in 1965, with George Skibine as director, Marjorie Tallchief as ballerina and a repertory featuring work by Alvin Ailey, Skibine, Eric Bruhn, Brian Macdonald and Stuart Hodes, the company mostly toured abroad, in the major theaters of Europe, to great acclaim, giving its dancers and choreographers a cosmopolitan experience unknown to most of their American colleagues.  Its New York debut was in 1967 and Macdonald was also appointed director, succeeded by Lawrence Rhodes (1968) and joined by Benjamin Harkarvy in 1969.  The ballet teacher David Howard was recruited in 1966 and became co-director of the school in 1971 with Maria Vegh, who had begun teaching at the school in 1968.  In 1970, Harkness combined it with the Harkness Youth Ballet (founded 1969), directed by Ben Stevenson, succeeded by Vicente Nebrada.

Return of the Jedi: Return of the Jedi (also known as Star Wars: Episode VI – Return of the Jedi) is a 1983 American epic space opera film directed by Richard Marquand.  The screenplay by Lawrence Kasdan and George Lucas was from a story by Lucas, who was also the executive producer.  It was the third installment in the original "Star Wars" trilogy and the first film to use THX technology.  The film is set one year after "The Empire Strikes Back" and was produced by Howard Kazanjian for Lucasfilm Ltd.  The film stars Mark Hamill, Harrison Ford, Carrie Fisher, Billy Dee Williams, Anthony Daniels, David Prowse, Kenny Baker, Peter Mayhew and Frank Oz.

Metropolitan Ballet: Metropolitan Ballet was a short lived British ballet company.  Founded in 1947 by Cecelia Blatch and Leon Hepner, the company performed in London and on tour in the provinces and abroad, staging shortened versions of the classics, some of the Diaghilev ballets, and new works by Victor Gsovsky (who was the company’s first ballet master), Andree Howard, Frank Staff and John Taras.  <br>

David Howard (ballet teacher): David Howard (born David Charles Edwards) (14 June 1937 – 11 August 2013) was an English ballet dancer and teacher, who taught internationally at institutions such as the Royal Ballet, the American Ballet Theatre, San Francisco Ballet, Joffrey Ballet, and the National Ballet of Canada.  Howard opened his popular eponymous dance studio in New York City, the David Howard School of Ballet (later the David Howard Dance Center) in 1977, before its closure in 1995.  His dance center welcomed all students including children, adult beginners and professionals from the Broadway musicals and ballet.  In addition to his teaching, Howard was an expert on the history of the pointe shoe worn by ballet dancers, and a pioneer in their design.

Howard Kazanjian: Howard G. Kazanjian (born July 26, 1942) is an American film producer known for "Raiders of the Lost Ark" and "Return of the Jedi".  Kazanjian is also a former 8-year Vice President of Lucasfilm, Ltd., and a published non-fiction author.

London Ballet: London Ballet was a short lived British ballet company founded by the British choreographer and former Ballet Rambert dancer Antony Tudor in 1938, along with Rambert members Hugh Laing, Andrée Howard, Agnes de Mille, Peggy van Praagh, Maude Lloyd and Walter Gore.  With the onset of World War II, in 1940 they were invited to New York, joining Richard Pleasant's and Lucia Chase's reorganized Ballet Theater, which later became the American Ballet Theatre.

Leon Danielian: Leon Danielian (31 October 1920 – 8 March 1997) was an American ballet dancer, teacher, choreographer, and educator.  As guest artist with ballet companies around the world, he became one of the first American male dancers to achieve international recognition.

The Rookie (1990 film): The Rookie is a 1990 American buddy cop film directed by Clint Eastwood and produced by Howard G. Kazanjian, Steven Siebert and David Valdes.  It was written from a screenplay conceived by Boaz Yakin and Scott Spiegel.  The film stars Charlie Sheen, Clint Eastwood, Raúl Juliá, Sônia Braga, Lara Flynn Boyle, and Tom Skerritt.  Eastwood plays a veteran police officer teamed up with a younger detective played by Sheen ("the rookie"), whose intent is to take down a German crime lord in downtown Los Angeles following months of investigation into an exotic car theft ring.

Question: Do both Leon Danielian and Howard Kazanjian do ballet?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "question_asked": {
      "type": "string",
      "description": "The original question posed."
    },
    "answer": {
      "type": "boolean",
      "description": "The direct boolean answer to the question."
    },
    "individuals_involved": {
      "type": "array",
      "description": "Details about the individuals mentioned in the question.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the individual."
          },
          "is_involved_in_ballet": {
            "type": "boolean",
            "description": "True if the individual is involved in ballet, false otherwise."
          },
          "primary_profession": {
            "type": "string",
            "description": "The primary profession or role of the individual as described in the context."
          }
        },
        "required": [
          "name",
          "is_involved_in_ballet",
          "primary_profession"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "question_asked",
    "answer",
    "individuals_involved"
  ],
  "additionalProperties": false
}
