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
Brother, I'm Dying: Brother I'm Dying, published in 2007 by Random House, is a family memoir by novelist Edwidge Danticat.  In 2007, the title won the National Book Critics Circle Award and was also nominated for the National Book Award.

Gary Klang: Gary Klang (born December 28, 1941, in Port-au-Prince Haiti), is a Haitian-Canadian poet and novelist.  Since 2007, he is the president of the prestigious "Conseil des Écrivains francophones d'Amérique" (Council of America's francophone writers).  Klang's work is very rich.  It includes novels, poetry, short stories and essays.  On July 14, 2000, "l'Union Française à Montréal" (the French Union of Montreal) chose Gary as the promoter of the French national holiday marking the storming of the Bastille.  The same day, the same French Union participated in the launch of his collection of verses "La terre est vide comme une étoile".  Gary Klang is also a member of the "Association des Ecrivains Québécois (UNEQ)” (Association of Quebec's writers), a member of the "Association des Ecrivains de langue française" (Association of writers of French origin) and of the PEN Club of Montreal.  He was nominated for the Haitian grand Literary Prize of 2004, together with Edwidge Danticat, René Depestre, Frankétienne, Dany Laferrière, Josaphat-Robert Large and Leslie Manigat (Ex President of Haiti, the winner of the Prize).

Stones in the Sun: Stones in the Sun is a 2012 Haitian American film written and directed by Patricia Benoit and starring Edwidge Danticat, Michele Marcelin, Diana Masi, Thierry Saintine, Patricia Rhinvil, James Noel, and Carlo Mitton.  It premiered at the 2012 Tribeca Film Festival, where it won the Special Jury Prize for Best Narrative Director.

David James Duncan: David James Duncan (born 1952) is an American novelist and essayist, best known for his two bestselling novels, "The River Why" (1983) and "The Brothers K" (1992).

Claire of the Sea Light: Claire of the Sea Light is a novel published in August 2013 by Knopf and written by Edwidge Danticat.  Set in the island-town of Ville Rose, Haiti, it narrates the story of the disappearance of a seven-year-old girl, Claire Limyè Lanmè Faustin, and of the memories of an entire townspeople that are brought to life in the wake of her disappearance.  In the words of "Guardian" reviewer Kamila Shamsie, "Danticat shows us a town scarred by violence, corruption, class disparities and social taboo, which is also a town of hope, dreams, love and sensuality.  But these are enmeshed rather than opposing elements.  Love leads to violence, dreams lead to corruption."

Edwidge Danticat: Edwidge Danticat (] ; born January 19, 1969) is a Haitian-American novelist and short story writer.

The Dew Breaker: The Dew Breaker is a novel by Edwidge Danticat, published in 2004.  The title "comes from a Creole phrase which refers to those who break the serenity of the grass in the morning dew.  It is a Creole nickname for torturer."  In this case, the "Dew Breakers" are members of the Tonton Macoutes, a group of volunteers who tortured and killed thousands of civilians under the regimes of François and Jean-Claude Duvalier in Haiti.

Josaphat-Robert Large: Josaphat-Robert Large (born November 15, 1942 in Jérémie, Haïti) is a Haitian-American poet, novelist and art critic.  His novel "Les terres entourées de larmes" [Shore surrounded with tears] won the prestigious Prix littéraire des Caraïbes (Caribbean literary Prize) in 2003.  He was nominated for the Haitian grand Literary Prize of 2004, together with Edwidge Danticat, René Depestre, Frankétienne, Gary Klang, Dany Laferrière and Leslie Manigat (Ex President of Haiti, the winner of the Prize).  Large was also one of the finalist at the Ushant' (Ouessant in French) Literary Contest in 2002. .  He writes in both French and Haitian Creole.  Josaphat-Robert Large is a member of " La Société des Gens de Lettres de France" (Society of French intellectuals), of the "Association des Écrivains de langue française" (Association of writers of French origin) and of the PEN Club America.  Josaphat-Robert Large's work is becoming more and more important in the French literary world.  The Society of French and francophone teachers of America has organized two colloquium on his literary production (specially his novels), one at Florida International University in 2001 and one at Fordham University in 2006.  .  Large also participated in the famous festival Étonnants-Voyageurs in 2007  and in 2008, he was one of the author in the great literary opening organized in Port-au-Prince by the Presses Nationales d'Haiti (National Press of Haiti).

Ciné Institute: Ciné Institute is a film school in Jacmel, Haiti, which grew out of the Jacmel Film Festival in 2008.  It is the first and only film school in Haiti founded by David Belle.  The college offers a free two-year tuition made possible by private donors.  The school encourages professionals, filmmakers, business people and artists from other mediums to come visit and perform workshops (called "master classes") within its weekly schedule; time slots that are pre-reserved in its curriculum.  Some notable attendees include, Paul Haggis, Jonathan Demme, Ben Stiller, Susan Sarandon and Edwidge Danticat.

Steven Church: Steven Church (born 1971) is an American essayist and writer of memoir and literary nonfiction.  Winner of the Glenna Luschei Prize from Prairie Schooner, Recipient of Colorado Book Award in Creative Nonfiction for "The Guinness Book of Me: A Memoir of Record", "Auscultation" chosen by Edwidge Danticat for inclusion in the 2011 Best American Essays.  Church is the author of "The Guinness Book of Me: A Memoir of Record" (2005), "Theoretical Killings: Essays & Accidents" (2009), "The Day After The Day After: My Atomic Angst" (2010),"Ultrasonic: Essays". (2014), "One with the Tiger: Sublime and Violent Encounters between Humans and Animals" (2016)

Question: Which writer wrote more essays, David James Duncan or Edwidge Danticat?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "comparison_subject": {
      "type": "string",
      "description": "The type of literary work being compared between authors."
    },
    "authors_compared": {
      "type": "array",
      "description": "Details for each author involved in the comparison.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the author."
          },
          "is_identified_as_essayist": {
            "type": "boolean",
            "description": "True if the author is explicitly identified as an essayist in the context."
          },
          "known_work_types": {
            "type": "array",
            "description": "A list of types of works attributed to the author in the context.",
            "items": {
              "type": "string"
            }
          }
        },
        "required": [
          "name",
          "is_identified_as_essayist",
          "known_work_types"
        ],
        "additionalProperties": false
      }
    },
    "author_with_more_essays": {
      "type": "string",
      "description": "The name of the author who wrote more essays based on the context."
    },
    "reasoning": {
      "type": "string",
      "description": "Explanation for why one author wrote more essays than the other, based on the provided context."
    }
  },
  "required": [
    "comparison_subject",
    "authors_compared",
    "author_with_more_essays",
    "reasoning"
  ],
  "additionalProperties": false
}
