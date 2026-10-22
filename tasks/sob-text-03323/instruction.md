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
Gugu Mbatha-Raw: Gugulethu Sophia Mbatha, MBE (born 21 April 1983), known as Gugu Mbatha-Raw (pronounced ), is a British stage and film actress.

Irreplaceable You: Irreplaceable You is an upcoming American drama film directed by Stephanie Laing.  It stars Gugu Mbatha-Raw and Michiel Huisman.

Free State of Jones (film): Free State of Jones is a 2016 American historical period war film inspired by the life of Newton Knight and his armed revolt against the Confederacy in Jones County, Mississippi, throughout the American Civil War.  Written and directed by Gary Ross, the film stars Matthew McConaughey, Gugu Mbatha-Raw, Mahershala Ali, and Keri Russell.

Beauty and the Beast (2017 film): Beauty and the Beast is a 2017 American musical romantic fantasy film directed by Bill Condon from a screenplay written by Stephen Chbosky and Evan Spiliotopoulos, and co-produced by Walt Disney Pictures and Mandeville Films.  The film is based on Disney's 1991 animated film of the same name, itself an adaptation of Jeanne-Marie Leprince de Beaumont's eighteenth-century fairy tale.  The film features an ensemble cast that includes Emma Watson and Dan Stevens as the titular characters with Luke Evans, Kevin Kline, Josh Gad, Ewan McGregor, Stanley Tucci, Audra McDonald, Gugu Mbatha-Raw, Ian McKellen, and Emma Thompson in supporting roles.

Belle (2013 film): Belle is a 2013 British period drama film directed by Amma Asante, written by Misan Sagay and produced by Damian Jones.  It stars Gugu Mbatha-Raw, Tom Wilkinson, Miranda Richardson, Penelope Wilton, Sam Reid, Matthew Goode, Emily Watson, Sarah Gadon, Tom Felton and James Norton.

The Ferryman (2007 film): The Ferryman is a New Zealand made horror film directed by Chris Graham and starring British actor John Rhys-Davies and New Zealand actress Amber Sainsbury; the film was released in the middle of 2007.

Beyond the Lights: Beyond the Lights is a 2014 American romantic drama film directed and written by Gina Prince-Bythewood.  The film stars Gugu Mbatha-Raw, Minnie Driver, Nate Parker, Danny Glover, and rapper Machine Gun Kelly.  The film premiered at the 2014 Toronto International Film Festival on September 7, 2014 and was released theatrically in the United States on November 14, 2014.  In 2015, the song "Grateful", written by Diane Warren for the film, was nominated for the Academy Award for Best Original Song.

Concussion (2015 film): Concussion is a 2015 American biographical sports drama film directed and written by Peter Landesman, based on the exposé "Game Brain" by Jeanne Marie Laskas, published in 2009 by "GQ" magazine.  Set in 2002, the film stars Will Smith as Dr. Bennet Omalu, a forensic pathologist who fights against the National Football League trying to suppress his research on chronic traumatic encephalopathy (CTE) brain degeneration suffered by professional football players.  It also stars Alec Baldwin, Gugu Mbatha-Raw, and Albert Brooks.

Miss Sloane: Miss Sloane is a 2016 political thriller film directed by John Madden and written by Jonathan Perera.  The film stars Jessica Chastain, Mark Strong, Gugu Mbatha-Raw, Michael Stuhlbarg, Alison Pill, Jake Lacy, John Lithgow, and Sam Waterston.

The Whole Truth (2016 film): The Whole Truth is a 2016 American thriller film directed by Courtney Hunt and written by Nicholas Kazan.  The film stars Keanu Reeves, Gabriel Basso, Gugu Mbatha-Raw, Renée Zellweger, and Jim Belushi.

Question: Who directed Irreplaceable You starring British stage and film actress Gugu Mbatha-Raw?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "director": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the director."
        }
      },
      "required": [
        "name"
      ],
      "additionalProperties": false
    },
    "starring_actress": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the starring actress."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the actress."
        },
        "profession": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "The professions of the actress."
        }
      },
      "required": [
        "name",
        "nationality",
        "profession"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "film_title",
    "director",
    "starring_actress"
  ],
  "additionalProperties": false
}
