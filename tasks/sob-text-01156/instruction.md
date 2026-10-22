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
Mouchette: Mouchette (] ) is a 1967 French film directed by Robert Bresson, starring Nadine Nortier and Jean-Claude Guilbert.  It is based on the novel of the same name by Georges Bernanos.  It was entered into the 1967 Cannes Film Festival, winning the OCIC Award (International Catholic Organization for Cinema and Audiovisual).

François Leterrier: François Leterrier, born 26 May 1929 in Margny-lès-Compiègne, is a French film director and actor.  He entered the film industry when he was cast in Robert Bresson's film "A Man Escaped".  After this he went on to become a director himself.

A Man Escaped: A Man Escaped or: The Wind Bloweth Where It Listeth (French: "Un condamné à mort s'est échappé ou Le vent souffle où il veut" ) is a 1956 French film directed by Robert Bresson.  It is based on the memoirs of André Devigny, a member of the French Resistance held in Montluc prison by the occupying Germans during World War II.  The protagonist of the film is called Fontaine.  The second part of the title comes from the Bible ( ) using the words of the Authorized King James Version (more recent translations use words like "wants" (which is the title in French) or "pleases" instead of "listeth").  Bresson himself was imprisoned by the Germans as a member of the French Resistance.

L'Argent (1983 film): L'argent (] , meaning "Money") is a 1983 French drama film written and directed by Robert Bresson.  The film is loosely inspired by the first part of Leo Tolstoy's novella "The Forged Coupon".  It was Bresson's last film, and earned its maker the Director's Prize at the 1983 Cannes Film Festival.

Les Dames du Bois de Boulogne: Les Dames du Bois de Boulogne (French for "The Ladies of the Bois de Boulogne") is a 1945 French film directed by Robert Bresson.  It is a modern adaptation of a section of Denis Diderot's "Jacques le fataliste" (1796) that tells the story of a man who is tricked into marrying a prostitute.

Robert Bresson: Robert Bresson (] ; 25 September 1901 – 18 December 1999) was a French film director.  Known for his ascetic approach, Bresson contributed notably to the art of cinema; his non-professional actors, ellipses, and sparse use of scoring have led his works to be regarded as preeminent examples of minimalist film.

Diary of a Country Priest: Diary of a Country Priest (French: "Journal d'un curé de campagne" ) is a 1951 French film written and directed by Robert Bresson, and starring Claude Laydu.  It was closely based on the novel of the same name by Georges Bernanos.  Published in 1936, the novel received the Grand prix du roman de l'Académie française.  It tells the story of a young, sickly priest, who has been assigned to his first parish, a village in northern France.

Angels of Sin: Angels of Sin (original French title: "Les anges du péché") was the first feature film directed by Robert Bresson.  Made in 1943, nine years after his comedy short "Affaires publiques", it was Bresson's only film released during the German occupation of France.  Working titles included "Bethany", and Bresson's favored title "The Exchange", but producers felt these titles weren't sensational enough.

Pickpocket (film): Pickpocket is a 1959 French film directed by Robert Bresson, generally believed to have been inspired by the novel "Crime and Punishment" by Fyodor Dostoevsky.  It stars the young Uruguayan Martin LaSalle, who was a nonprofessional actor at the time, in the title role, with Marika Green as the ingénue.  It was the first film for which Bresson wrote an original screenplay rather than "adapting it from an existing text."

A Gentle Woman: A Gentle Woman (French: Une femme douce ) is a 1969 French drama film directed by Robert Bresson.  It is Bresson's first film in color, and adapted from Fyodor Dostoevsky's short story "A Gentle Creature" (Кроткая ).  The film is set in contemporary Paris.

Question: What is the name of the 1956 French film directed by Robert Bresson, based on the memoirs of Andre Devigny and which starred Francois Leterrier in his debut role?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "director": {
      "type": "string",
      "description": "The director of the film."
    },
    "release_year": {
      "type": "integer",
      "description": "The year the film was released."
    },
    "source_material": {
      "type": "object",
      "properties": {
        "type": {
          "type": "string",
          "description": "The type of source material (e.g., novel, memoirs)."
        },
        "author": {
          "type": "string",
          "description": "The author or subject of the source material."
        }
      },
      "required": [
        "type",
        "author"
      ],
      "additionalProperties": false
    },
    "starring_actor": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the actor."
        },
        "role_description": {
          "type": "string",
          "description": "Description of the actor's role or significance in the film (e.g., debut role)."
        }
      },
      "required": [
        "name",
        "role_description"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "film_title",
    "director",
    "release_year",
    "source_material",
    "starring_actor"
  ],
  "additionalProperties": false
}
