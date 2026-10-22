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
The Phantom of the Opera (2004 film): The Phantom of the Opera is a 2004 British-American musical drama film based on Andrew Lloyd Webber's 1986 musical of the same name, which in turn is based on the French novel "Le Fantôme de l'Opéra" by Gaston Leroux.  It was produced and co-written by Lloyd Webber and directed by Joel Schumacher.  It stars Gerard Butler in the title role, Emmy Rossum as Christine Daaé, Patrick Wilson as Raoul, Miranda Richardson as Madame Giry, Minnie Driver as Carlotta Giudicelli, and Jennifer Ellison as Meg Giry.

Joseph Buquet: Joseph Buquet is a fictional character in "The Phantom of the Opera", the 1909 novel by French writer Gaston Leroux.  He appears in many film and stage adaptations of the story.

Le Gaulois: Le Gaulois (] ) was a French daily newspaper, founded in 1868 by Edmond Tarbé and Henri de Pène.  After a printing stoppage, it was revived by Arthur Meyer in 1882 with notable collaborators Paul Bourget, Alfred Grévin, Abel Hermant, and Ernest Daudet.  Among its many famous contributing editors was Guy de Maupassant.  Gaston Leroux's novel "The Phantom of the Opera" was first published as a serialization in its pages between September 1909 and January 1910.

Pierrot (short story): "Pierrot" is a short story by French writer Guy de Maupassant.  It was originally published on 1 October 1882 in the French newspaper "Le Gaulois".  A year later, in 1883, it appeared in the short story collection "Contes de la bécasse".  The story was dedicated to Henry Roujon, novelist and public servant.

Madame Giry: Madame Giry is a fictional character from Gaston Leroux's 1909 novel "The Phantom of the Opera".  She is a fairly intermediate character in the novel, although her role is much increased in the Andrew Lloyd Webber musical.  This article will deal with both versions separately.

The Necklace: "The Necklace" or "The Diamond Necklace" (French: "La Parure" ) is an 1884 short story by French writer Guy de Maupassant.  It is known for its twist ending, which was a hallmark of de Maupassant's style.  The story was first published on 17 February 1884 in the French newspaper "Le Gaulois".

The Phantom of the Opera: The Phantom of the Opera (French: Le Fantôme de l'Opéra) is a novel by French writer Gaston Leroux.  It was first published as a serialisation in "Le Gaulois" from 23 September 1909, to 8 January 1910.  It was published in volume form in late March 1910 by Pierre Lafitte.  The novel is partly inspired by historical events at the Paris Opera during the nineteenth century and an apocryphal tale concerning the use of a former ballet pupil's skeleton in Carl Maria von Weber's 1841 production of "Der Freischütz".  It has been successfully adapted into various stage and film adaptations, most notable of which are the 1925 film depiction featuring Lon Chaney, and Andrew Lloyd Webber's 1986 musical.

Meg Giry: Meg Giry is one of the fictional characters from Gaston Leroux's novel "The Phantom of the Opera".  In the story she is Madame Giry's oldest daughter.

Suicides (short story): "Suicides" is a short story by French writer Guy de Maupassant.  It was originally published on 29 August 1880 in the French newspaper "Le Gaulois".  On 17 April 1883, it was published in "Gil Blas" under the pseudonym Maufrigneuse, and by other three periodicals, before being republished in the short story collection "Les Sœurs Rondoli" in 1884.

The Mystery of the Yellow Room (1919 film): The Mystery of the Yellow Room is a 1919 American crime drama film made by the Mayflower Photoplay Company and distributed through Realart Pictures Corporation.  Emile Chautard was a French actor, director, and producer.  Chautard was 55 years old when "The Mystery of the Yellow Room" was released in 1919.  "The Mystery of the Yellow Room" (in French "Le mystère de la chambre jaune") was first a novel by Gaston Leroux.  The novel was one of the first locked room mystery crime fiction novels.  It was first published in France in the periodical "L'Illustration" from September 1907 to November 1907, then in its own right as a book in 1908.

Question: Meg Giry is one of the fictional characters from the French writer Gaston Leroux's novel,first published as a serialisation in "Le Gaulois", is titled what?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "novel_title": {
      "type": "string",
      "description": "The title of the novel."
    },
    "author_name": {
      "type": "string",
      "description": "The name of the author of the novel."
    },
    "featured_character": {
      "type": "string",
      "description": "The name of the fictional character from the novel."
    },
    "publication_details": {
      "type": "object",
      "properties": {
        "first_published_as_serialization": {
          "type": "boolean",
          "description": "Indicates if the novel was first published as a serialization."
        },
        "serialization_newspaper": {
          "type": "string",
          "description": "The name of the newspaper where the novel was serialized."
        },
        "serialization_start_date": {
          "type": "string",
          "description": "The start date of the serialization."
        },
        "serialization_end_date": {
          "type": "string",
          "description": "The end date of the serialization."
        }
      },
      "required": [
        "first_published_as_serialization",
        "serialization_newspaper",
        "serialization_start_date",
        "serialization_end_date"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "novel_title",
    "author_name",
    "featured_character",
    "publication_details"
  ],
  "additionalProperties": false
}
