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
Hannibal (Harris novel): Hannibal is a novel by American author Thomas Harris, published in 1999.  It is the third in his series featuring Dr. Hannibal Lecter and the second to feature FBI Special Agent Clarice Starling.  The novel takes place seven years after the events of "The Silence of the Lambs" and deals with the intended revenge of one of Lecter's victims.  It was adapted as a film of the same name in 2001, directed by Ridley Scott.  Elements of the novel were incorporated into the second season of the NBC television series "Hannibal", while the show's third season adapted the plot of the novel.

Potage (Hannibal): "Potage" is the third episode of the first season of the psychological thriller–horror series "Hannibal".  The episode was written by David Fury, Chris Brancato and Bryan Fuller from a story by Fury, and directed by David Slade.  It was first broadcast on April 18, 2013, on NBC.  The series is based on characters and elements appearing in Thomas Harris' novels "Red Dragon" and "Hannibal", with focus on the relationship between FBI special investigator Will Graham (Hugh Dancy) and Dr. Hannibal Lecter (Mads Mikkelsen), a forensic psychiatrist destined to become Graham's most cunning enemy.

Apéritif (Hannibal): "Apéritif" is the first episode of psychological thriller–horror series "Hannibal".  The episode was written by Bryan Fuller, and directed by David Slade.  It was first broadcast on April 4, 2013, on NBC.  The series is based on characters and elements appearing in Thomas Harris' novels "Red Dragon" and "Hannibal", with focus on the relationship between FBI special investigator Will Graham (Hugh Dancy) and Dr. Hannibal Lecter (Mads Mikkelsen), a forensic psychiatrist destined to become Graham's most cunning enemy.

The Silence of the Lambs (film): The Silence of the Lambs is a 1991 American horror-thriller film directed by Jonathan Demme and starring Jodie Foster, Anthony Hopkins, and Scott Glenn.  Adapted by Ted Tally from the 1988 novel of the same name by Thomas Harris, his second to feature the character of Dr. Hannibal Lecter; a brilliant psychiatrist and cannibalistic serial killer, the film was the second adaptation of a Harris novel featuring Lecter, preceded by the Michael Mann-directed "Manhunter" in 1986.  In the film, Clarice Starling, a young U.S. FBI trainee, seeks the advice of the imprisoned Dr. Lecter to apprehend another serial killer, known only as "Buffalo Bill".

Amuse-Bouche (Hannibal): "Amuse-Bouche" is the second episode of the first season of the psychological thriller–horror series "Hannibal".  The episode was written by Jim Danger Gray, and directed by Michael Rymer.  It was first broadcast on April 11, 2013, on NBC.  The series is based on characters and elements appearing in Thomas Harris' novels "Red Dragon" and "Hannibal", with focus on the relationship between FBI special investigator Will Graham (Hugh Dancy) and Dr. Hannibal Lecter (Mads Mikkelsen), a forensic psychiatrist destined to become Graham's most cunning enemy.

Richard Armitage (actor): Richard Crispin Armitage (born 22 August 1971) is an English film, television, theatre and voice actor.  He received notice in the UK with his first leading role as John Thornton in the British television programme "North & South" (2004).  But it was his role as dwarf prince and leader Thorin Oakenshield in Peter Jackson's film trilogy adaptation of "The Hobbit" that first brought him international recognition.  Other notable roles include John Proctor in Yaël Farber’s stage production of Arthur Miller's "The Crucible", Francis Dolarhyde in the American TV series "Hannibal", Lucas North in the British TV drama "Spooks", John Porter in the British TV drama "Strike Back", and Guy of Gisborne in the British TV drama "Robin Hood".  He more recently voiced Trevor Belmont in the Netflix adaptation of "Castlevania".

Hannibal (TV series): Hannibal is an American psychological thriller–horror television series developed by Bryan Fuller for NBC.  The series is based on characters and elements appearing in Thomas Harris' novels "Red Dragon" and "Hannibal", with focus on the relationship between FBI special investigator Will Graham (Hugh Dancy) and Dr. Hannibal Lecter (Mads Mikkelsen), a forensic psychiatrist destined to become Graham's most cunning enemy.

Oeuf (Hannibal): "Oeuf" (also known as "Ceuf" or "Œuf") is the fourth episode of the first season of the psychological thriller–horror series "Hannibal".  The episode was written by Jennifer Schuur, and directed by Peter Medak.  The series is based on characters and elements appearing in Thomas Harris' novels "Red Dragon" and "Hannibal", with focus on the relationship between FBI special investigator Will Graham (Hugh Dancy) and Dr. Hannibal Lecter (Mads Mikkelsen), a forensic psychiatrist destined to become Graham's most cunning enemy.

Dr. Lecter: Dr. Lecter is the debut studio album by the American rapper Action Bronson.  It was released on March 15, 2011.  The album's title refers to Dr. Hannibal Lecter, a character in the horror film "The Silence of the Lambs".  The album is entirely produced by Tommy Mas.  Almost all of the beats on "Dr. Lecter" were made with breakbeat samples.  After hearing this album, the producer Statik Selektah collaborated with Bronson on an album titled "Well Done", released on November 22, 2011.

Freddy Lounds: Freddy Lounds (or Fredricka "Freddie" Lounds) is a fictional character in the Hannibal Lecter series, created by author Thomas Harris.  Lounds first appears in the 1981 novel "Red Dragon" as a foil to protagonist Will Graham who is ultimately murdered by primary antagonist Francis Dolarhyde.

Question: Who plays Dr. Hannibal Lecter in the television series that Richard Armitage plays Francis Dolarhyde in? 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "tv_series_name": {
      "type": "string",
      "description": "The name of the television series."
    },
    "actor_roles": {
      "type": "array",
      "description": "Details about actors and their roles in the series.",
      "items": {
        "type": "object",
        "properties": {
          "actor_name": {
            "type": "string",
            "description": "The name of the actor."
          },
          "character_played": {
            "type": "string",
            "description": "The character played by the actor."
          }
        },
        "required": [
          "actor_name",
          "character_played"
        ],
        "additionalProperties": false
      }
    },
    "dr_hannibal_lecter_actor": {
      "type": "string",
      "description": "The actor who plays Dr. Hannibal Lecter in the specified TV series."
    }
  },
  "required": [
    "tv_series_name",
    "actor_roles",
    "dr_hannibal_lecter_actor"
  ],
  "additionalProperties": false
}
