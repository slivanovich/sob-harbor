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
McOndo: McOndo is a Latin American literary movement that breaks from the Magical Realism ("Realismo mágico") mode of narration, and counters it with the strong, ideologic associations of the cultural and narrative languages of the mass communications media, and with the modernity of urban living; the experience of town versus country, of McOndo "vs." Macondo.  The literature of McOndo presents urban Latin (American) life in "the City", an experience the opposite of the rural, "natural world" of Macondo, the archetypal "Latin American Country" presented in the literature of Magical Realism.  Philosophically, the McOndo "vs." Macondo intellectual opposition is to the latter's literary perpetuation of Latin America as an exotic place of exotic people, which presents the reader with "reductionist essential-isms that everyone in Latin America wears a "sombrero" and lives on trees".  Because not everyone wears "huaraches" and sports a "machete" in contemporary "Latinoamėrica", McOndo literature shows it to be a place of many countries, peoples, and cultures, not the monolithic, "Spanish-speaking worlds" of the 19th-century dictator novel and the banana republic which preceded 20th-century modernization.

The Fountain: The Fountain is a 2006 American epic magical realism romantic drama film that blends elements of fantasy, history, spirituality, and science fiction.  It is directed by Darren Aronofsky, and stars Hugh Jackman and Rachel Weisz.  The film consists of three storylines involving immortality and the resulting loves lost, and one man's pursuit of avoiding this fate in this life or beyond it.  Jackman and Weisz play sets of characters bonded by love across time and space: a conquistador and his ill-fated queen, a modern-day scientist and his cancer-stricken wife, and a traveler immersed in a universal journey alongside aspects of his lost love.  The storylines—interwoven with use of match cuts and recurring visual motifs—reflect the themes and interplay of love and mortality.

Rachel Weisz: Rachel Hannah Weisz ( "vice"; born 7 March 1970) is a British actress.

Hallucinatory realism: Hallucinatory realism is a term that has been used with various definitions since at least the 1970s by critics in describing works of art.  In some occurrences the term has had connections to the concept of magical realism, although hallucinatory realism is usually more specific to a dream-state.  The term occurs in the motivation for Mo Yan's Nobel Prize in Literature.

Daniel Kehlmann: Daniel Kehlmann (born 13 January 1975) is a German-language author of both Austrian and German nationality.  His work "Die Vermessung der Welt" (translated into English by Carol Brown Janeway as "Measuring the World", 2006) is the best selling novel in the German language since Patrick Süskind's "Perfume" was released in 1985.  Kehlmann's works, and in particular "Die Vermessung der Welt", are heavily influenced by magical realism and represent a dramatic shift from the goals of the influential Group 47.  He was awarded the Heimito von Doderer Prize for the novel.

Magical feminism: Magical feminism is a subgenre of the magical realism literary genre.  The term was first used in 1987 by Patricia Hart to describe the works of Isabel Allende.  More recent critical works on the subject feature such scholars as Ricci-James Adams or Kimberley Ann Wells.  The term "magical feminism" refers to magical realism in a feminist discourse.  Magical realism's basic assumption is the coexistence and effective merging of contradictory worldviews, the scientific and rational with the spiritual and magical.  It grants equal ontological status to real figures and spirits, everyday occurrences and supernatural events.  In its nature then is the subversion of monolithic cultural, social and political structures.  It is a mode perfect for the writers who are "in between", especially the postcolonial ones.

Magic realism: Magical realism, magic realism, or marvelous realism is a genre of narrative fiction and, more broadly, art (literature, painting, film, theatre, etc.) that, while encompassing a range of subtly different concepts, expresses a primarily realistic view of the real world while also adding or revealing magical elements.  It is sometimes called fabulism, in reference to the conventions of fables, myths, and allegory.  "Magical realism", perhaps the most common term, often refers to fiction and literature in particular, with magic or the supernatural presented in an otherwise real-world or mundane setting.

Parthiban Kanavu (2003 film): Parthiban Kanavu (English: Parthiban's Dream) is a 2003 Tamil magical realism romantic drama film written and directed by Karu Pazhaniappan.  The film stars Srikanth and Sneha in lead roles.  It had Manivannan and Vivek in supporting roles.  Sneha featured in a dual role for the first time. Jyothika was approached for the Lead Actress Role but Unavailability of Dates result in replacement of her by Sneha.  The film's score and soundtrack are composed by Vidyasagar.  The film was a sleeper hit in 2003.

Hugh Jackman: Hugh Michael Jackman (born 12 October 1968) is an Australian actor, singer, and producer.  Jackman has won international recognition for his roles in a variety of film genres.  He is known for his long-running role as Wolverine in the "X-Men" film series, as well as for his lead roles in films such as the romantic-comedy fantasy "Kate & Leopold" (2001), the action-horror film "Van Helsing" (2004), the magic-themed drama "The Prestige" (2006), the epic fantasy drama "The Fountain" (2006), the epic historical romantic drama "Australia" (2008), the film version of "Les Misérables" (2012), and the thriller "Prisoners" (2013).  His work in "Les Misérables" earned him his first Academy Award nomination for Best Actor and his first Golden Globe Award for Best Actor – Motion Picture Musical or Comedy in 2013.

Edmundo Paz Soldán: José Edmundo Paz-Soldán Ávila (Cochabamba, March 29, 1967) is a Bolivian writer.  His work is a prominent example of the Latin American literary movement known as McOndo, in which the magical realism of previous Latin American authors is supplanted by modern realism, often with a technological focus.  His work has won several awards.  He has lived in the United States since 1991, and has taught literature at Cornell University since 1997.

Question: What nationality is the female star of 2006 American epic magical realism romantic drama The Fountain?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_details": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the film."
        },
        "year": {
          "type": "integer",
          "description": "The release year of the film."
        },
        "genres": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of genres associated with the film."
        }
      },
      "required": [
        "title",
        "year",
        "genres"
      ],
      "additionalProperties": false
    },
    "female_star": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the female star."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the female star."
        }
      },
      "required": [
        "name",
        "nationality"
      ],
      "additionalProperties": false
    },
    "answer_nationality": {
      "type": "string",
      "description": "The nationality of the female star of the film."
    }
  },
  "required": [
    "film_details",
    "female_star",
    "answer_nationality"
  ],
  "additionalProperties": false
}
