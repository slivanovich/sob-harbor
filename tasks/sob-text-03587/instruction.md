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
The Absent One (2014 film): The Absent One (Danish: Fasandræberne), also known as Department Q: The Absent One, is a 2014 Danish crime mystery film directed by and co-written by Nikolaj Arcel and , based on Jussi Adler-Olsen's novel of the same name.  It is the second film in the Department Q series following the 2013 film "The Keeper of Lost Causes", and preceding the 2016 film "A Conspiracy of Faith".

Jussi Adler-Olsen: Carl Valdemar Jussi Henry Adler-Olsen (born 2 August 1950) is a Danish writer of crime fiction, as well as a publisher, editor and entrepreneur.

A Conspiracy of Faith: A Conspiracy of Faith (Danish: "Flaskepost fra P"), also known as Department Q: A Conspiracy of Faith, is a 2016 Danish film, directed by Hans Petter Moland, based on a novel by Jussi Adler-Olsen.  It is the third film in the Department Q series, after The Keeper of Lost Causes (2013) and The Absent One (2014)".

Birger Larsen (director): Birger Larsen (22 December 1961 – 26 October 2016) was a Danish film director and screenwriter.  He won the Bodil Award for Best Danish Film for his 1990 film "Dance of the Polar Bears" (Danish: "Lad isbjørnene danse" ).  He was also nominated for the Academy Award for Live Action Short Film for his film "Sweethearts" (1996).  In 2013, he directed the first episode of "Crimes of Passion".

Babette's Feast: Babette's Feast (Danish: "Babettes gæstebud" ) is a 1987 Danish drama film directed by Gabriel Axel.  The film's screenplay was written by Axel based on the story by Isak Dinesen (Karen Blixen).  Produced by Just Betzer, Bo Christensen, and Benni Korzen with funding from the Danish Film Institute, "Babette's Feast" was the first Danish cinema film of a Blixen story.  It was also the first Danish film to win the Academy Award for Best Foreign Language Film.  The film premiered in the Un Certain Regard section of the 1987 Cannes Film Festival.

The End of the World (1916 film): The End of the World (Danish: Verdens Undergang ) is a 1916 Danish science fiction drama film directed by August Blom and written by Otto Rung, starring Olaf Fønss and Ebba Thomsen.  The film depicts a worldwide catastrophe when an errant comet passes by Earth and causes natural disasters and social unrest.  Blom and his crew created special effects for the comet disaster using showers of fiery sparks and shrouds of smoke.  The film attracted a huge audience because of fears generated during the passing of Halley's comet six years earlier, as well as the ongoing turbulence and unrest of World War I.  The film is also known as The Flaming Sword.  It was restored by the Danish Film Institute and released on DVD in 2006.

Facing the Truth (film): Facing the Truth (Danish: "At kende sandheden" ) is a 2002 Danish drama written and directed by Nils Malmros.  Shot in black-and-white documentary style, and based on the real life of Malmros' father, the film relates the hardships of a young neurosurgeon struggling through a medical lawsuit.  Malmros, whose films are known for their realism, is educated as a surgeon and performed all the film's brain surgery scenes.  The film was nominated for the 2003 Bodil Award for Best Danish Film and won the 2003 Danish Film Academy's Robert Award for Film of the Year.

The Keeper of Lost Causes: The Keeper of Lost Causes (Danish: "Kvinden i buret"), also known as Department Q: The Keeper of Lost Causes, is a 2013 Danish film, directed by Mikkel Nørgaard.  The movie is based on a novel by Jussi Adler-Olsen.  It is the first film in the Department Q series, followed by the 2014 film "The Absent One", and the 2016 film "A Conspiracy of Faith".

Waltzing Regitze: Waltzing Regitze, also known as Memories of a Marriage, (Original title: Dansen med Regitze) is a 1989 Danish drama film directed by Kaspar Rostrup.  Based upon a popular Danish novel by Martha Christensen, the film is an unsentimental portrait of the history and changes of a middle-aged couple's marriage, told through flashbacks during a summer party.  The film stars Ghita Nørby and Frits Helmuth.  "Waltzing Regitze" was nominated for the Academy Award for Best Foreign Language Film.  In 1990, it won the Robert Award for Film of the Year and swept the Bodil Awards, winning Best Danish Film as well as all four of acting categories.

Det Sande Ansigt: Det Sande Ansigt (English translation: The True Face) is a 1951 Danish film directed by Bodil Ipsen and Lau Lauritzen Jr., written by Johannes Allen, and based upon the novel by Gerhard Rasmussen.  The film received the Bodil Award for Best Danish Film of the Year.

Question: The Keeper of Lost Causes, also known as Department Q: The Keeper of Lost Causes, is a 2013 Danish film, directed by who, the movie is based on a novel by Jussi Adler-Olsen?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The primary title of the film."
    },
    "alternative_titles": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Other known titles for the film."
    },
    "release_year": {
      "type": "integer",
      "description": "The year the film was released."
    },
    "director": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the film's director."
        }
      },
      "required": [
        "name"
      ],
      "additionalProperties": false
    },
    "based_on_novel": {
      "type": "object",
      "properties": {
        "author_name": {
          "type": "string",
          "description": "The name of the author whose novel the film is based on."
        }
      },
      "required": [
        "author_name"
      ],
      "additionalProperties": false
    },
    "series_information": {
      "type": "object",
      "properties": {
        "series_name": {
          "type": "string",
          "description": "The name of the film series."
        },
        "series_position": {
          "type": "integer",
          "description": "The film's position within the series (e.g., 1st, 2nd)."
        }
      },
      "required": [
        "series_name",
        "series_position"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "film_title",
    "release_year",
    "director",
    "based_on_novel"
  ],
  "additionalProperties": false
}
