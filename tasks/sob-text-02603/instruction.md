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
Budapest Semesters in Mathematics: The Budapest Semesters in Mathematics program is a study abroad opportunity for North American undergraduate students in Budapest, Hungary.  The coursework is primarily mathematical and conducted in English by Hungarian professors whose primary positions are at Eötvös Loránd University or the Alfréd Rényi Institute of Mathematics of the Hungarian Academy of Sciences.  Originally started by László Lovász, László Babai, Vera Sós, and Pál Erdős, the first semester was conducted in Spring 1985.  The North- American part of the program is currently run by Tina Garrett (North American Director) out of St. Olaf College in Northfield, MN.  She is supported by Kendra Killpatrick (Associate Director) and Eileen Shimota (Program Administrator).  The former North American Directors were Paul D. Humke (1988–2011) and Tom Trotter.  The Hungarian director is Dezső Miklós.

Shrunken Heads (film): Shrunken Heads is a 1994 American horror film directed by Richard Elfman and written by Matthew Bright.  It is Full Moon Entertainment's first theatrical feature, and the last film in which Julius Harris appeared.

Scarecrow (2002 film): Scarecrow is a 2002 direct-to-video horror film B movie, directed by French director Emmanuel Itier.  It stars B movie scream queen Tiffany Shepis and Tim Young as Lester among others, including director and cofounder of Oingo Boingo Richard Elfman.  The film is described as "so bad it's good", due to its poor acting, writing, and overall story.

Forbidden Zone (soundtrack): The Forbidden Zone OST is the soundtrack to "Forbidden Zone", the 1980 cult film directed by Richard Elfman.  The film's music was composed by Danny Elfman and performed by The Mystic Knights of the Oingo Boingo.  The original LP version contained 22 tracks.  In 1990 it was released with two tracks removed (possibly because of performing rights and copyright infringement).  An 18-track version is also known to exist.

Streets of Rage (film): Streets of Rage is a 1994 American action crime romance film directed by Richard Elfman (credited as Aristride Sumatra) and co-written by Elfman and Mimi Lesseos, based on a story by Lesseos.  The film stars Lesseos and Oliver Page.

Richard Elfman: Richard "Rick" Elfman (born March 6, 1949 in the Crenshaw district of Los Angeles, California) is an American film actor, director, producer, screenwriter, author, and magazine publisher.

Drew Renaud: Michael "Drew" Renaud (born 1985) is an American film director, screenwriter, editor and producer.  He has received awards from the San Diego Film Festival and LA Shorts Fest.

Bodhi Elfman: Bodhi Pine Elfman (born Bodhi Pine Saboff; July 19, 1969) is an American actor and the only child of filmmaker Richard Elfman and Rhonda Joy Saboff.  He is best known for playing Avram Hader in the Fox series "Touch" and for his recurring role in "Criminal Minds" as Peter Lewis/Mr.  Scratch.

Forbidden Zone: Forbidden Zone is a 1980 American musical fantasy comedy film directed and produced by Richard Elfman, and co-written by Elfman and fellow Mystic Knights member Matthew Bright.  Originally shot on black-and-white film, the film is based upon the stage performances of the Mystic Knights of the Oingo Boingo.  and revolves around an alternate universe accessed through a door in the house of the Hercules family.

Modern Vampires: Modern Vampires (also billed as Revenant) is a 1998 black horror/comedy film that was released Oct 19, 1999 straight to video, written by Matthew Bright and directed by Richard Elfman.

Question: Are Drew Renaud and Richard Elfman both American directors?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "question_answer": {
      "type": "boolean",
      "description": "True if both Drew Renaud and Richard Elfman are American directors, false otherwise."
    },
    "individuals_analyzed": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the individual."
          },
          "is_american": {
            "type": "boolean",
            "description": "True if the individual is identified as American in the context."
          },
          "is_director": {
            "type": "boolean",
            "description": "True if the individual is identified as a director in the context."
          }
        },
        "required": [
          "name",
          "is_american",
          "is_director"
        ],
        "additionalProperties": false
      },
      "description": "Details about each individual mentioned in the question."
    },
    "summary": {
      "type": "object",
      "properties": {
        "number_of_individuals_checked": {
          "type": "integer",
          "description": "The total number of individuals whose director and nationality status was checked."
        },
        "number_of_american_directors": {
          "type": "integer",
          "description": "The count of individuals who are both American and directors among those checked."
        }
      },
      "required": [
        "number_of_individuals_checked",
        "number_of_american_directors"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "question_answer",
    "individuals_analyzed",
    "summary"
  ],
  "additionalProperties": false
}
