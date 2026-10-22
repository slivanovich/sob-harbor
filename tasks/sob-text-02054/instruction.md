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
List of accolades received by Philomena (film): "Philomena" is a 2013 British comedy-drama film directed by Stephen Frears.  Steve Coogan and Jeff Pope adapted the screenplay from "The Lost Child of Philomena Lee" by Martin Sixsmith.  The film focuses on Philomena Lee's (Judi Dench) 50-year-long search for the son she was forced to give up for adoption.  It was screened in the main competition section at the 70th Venice International Film Festival, where it competed for the Golden Lion.  "Philomena" was released in the United Kingdom by The Weinstein Company on 1 November 2013.  As of March 2014, the film has earned over £86 million in its combined total gross at the box office.

Roshan Seth: Roshan Seth is an Indian-born British actor, who appears mainly in British and American films.  He is known for his critically acclaimed performances in the films "Gandhi", "Mississippi Masala", "Not Without My Daughter", "My Beautiful Laundrette", "Indiana Jones and the Temple of Doom", "Such a Long Journey", and "Street Fighter: The Movie".  He is the brother of retired Indian diplomat Aftab Seth.

Derrick Branche: Derrick Branche (born 1947) is a British actor, best known for his role in the film "My Beautiful Laundrette" and television roles in "The Jewel in the Crown" and "Father Ted".

Florence Foster Jenkins (film): Florence Foster Jenkins is a 2016 biographical comedy-drama film directed by Stephen Frears and written by Nicholas Martin.  The film stars Meryl Streep as Florence Foster Jenkins, a New York heiress who became an opera singer known for her painful lack of singing skill.  Hugh Grant plays her husband and manager, English Shakespearean actor, St. Clair Bayfield.  Other cast members include Simon Helberg, Rebecca Ferguson, and Nina Arianda.

Stephen Frears: Stephen Arthur Frears (born 20 June 1941) is an English film director.  Frears has directed British films since the 1980s including "My Beautiful Laundrette", "Dangerous Liaisons", "High Fidelity", "The Queen", "Philomena" and "Florence Foster Jenkins".  He has been nominated for two Academy Awards for Best Director for "The Grifters" and "The Queen".  In 2008 "The Telegraph" named him among the most influential people in British culture.

Hero (1992 film): Hero (released in the United Kingdom and Ireland as Accidental Hero) is a 1992 American comedy-drama film directed by Stephen Frears.  The film was written by David Webb Peoples from a story written by Peoples, Laura Ziskin and Alvin Sargent and stars Dustin Hoffman, Geena Davis, Andy García, Joan Cusack and Chevy Chase (uncredited).  Following the critically acclaimed "The Grifters" (1990), "Hero" was the second American feature film by British filmmaker Frears.

Gordon Warnecke: Gordon Warnecke (born 24 August 1962 in London) is a British actor of Indo-Guyanese and German descent.  He may be best known for his role as Omar in the 1985 film "My Beautiful Laundrette", co-starring as the lover of Johnny (Daniel Day-Lewis).  Other film credits include Franco Zeffirelli's "Young Toscanini" and Hanif Kureishi's "London Kills Me".

My Beautiful Laundrette: My Beautiful Laundrette is a 1985 British comedy-drama film directed by Stephen Frears from a screenplay by Hanif Kureishi.  The film was also one of the first films released by Working Title Films.

High Fidelity (film): High Fidelity is a 2000 American romantic comedy-drama film directed by Stephen Frears.  It stars John Cusack, Iben Hjejle, Jack Black, Todd Louiso, and Lisa Bonet.  The film is based on the 1995 British novel of the same name by Nick Hornby, with the setting moved from London to Chicago and the name of the lead character changed.

Victoria &amp; Abdul: Victoria & Abdul is a 2017 biographical comedy-drama film directed by Stephen Frears and written by Lee Hall.  A sequel to "Mrs Brown" (1997), the film is based on the book of same name by Shrabani Basu, and on the real-life relationship between Queen Victoria of the United Kingdom and her Indian muslim servant Abdul Karim.  The film stars Judi Dench, Ali Fazal, Michael Gambon, Eddie Izzard, Tim Pigott-Smith (in his last film role), and Adeel Akhtar.  Dench reprises her role as Queen Victoria from "Mrs. Brown".  The film had its world premiere at the 74th Venice Film Festival.

Question: Derrick Branche (born 1947) is a British actor, best known for his role in the film "My Beautiful Laundrette",a British comedy-drama film, released in what year, and directed by Stephen Frears? 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "release_year": {
      "type": "integer",
      "description": "The year the film was released."
    },
    "director": {
      "type": "string",
      "description": "The director of the film."
    }
  },
  "required": [
    "film_title",
    "release_year",
    "director"
  ],
  "additionalProperties": false
}
