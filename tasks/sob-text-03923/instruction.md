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
The Messenger: The Story of Joan of Arc: The Messenger: The Story of Joan of Arc (French: Jeanne d'Arc ) is a 1999 French epic historical drama film directed by Luc Besson.  The film stars Milla Jovovich, John Malkovich, Faye Dunaway and Dustin Hoffman.  The screenplay was written by Besson and Andrew Birkin, and the original music score was composed by Éric Serra.

Troy (film): Troy is a 2004 American epic period war film written by David Benioff and directed by Wolfgang Petersen.  The film features an ensemble cast led by Brad Pitt, Eric Bana, and Orlando Bloom.  It is loosely based on Homer's "Iliad" in its narration of the entire story of the decade-long Trojan War - condensed into little more than a couple of weeks - rather than just the quarrel between Achilles and Agamemnon in the ninth year.  Achilles leads his Myrmidons along with the rest of the Greek army invading the historical city of Troy, defended by Hector's Trojan army.  The end of the film (the sack of Troy) is not taken from the "Iliad", but rather from Virgil's "Aeneid" as the "Iliad" concludes with Hector's death and funeral.

The Eagle (2011 film): The Eagle is a 2011 epic historical drama film set in Roman Britain directed by Kevin Macdonald, and starring Channing Tatum, Jamie Bell and Donald Sutherland.  Adapted by Jeremy Brock from Rosemary Sutcliff's historical adventure novel "The Eagle of the Ninth" (1954), the film tells the story of a young Roman officer searching to recover the lost Roman eagle standard of his father's legion in the northern part of Great Britain.  The story is based on the Ninth Spanish Legion's supposed disappearance in Britain.

The Hobbit: The Battle of the Five Armies: The Hobbit: The Battle of the Five Armies is a 2014 epic high fantasy action film directed by Peter Jackson and written by Jackson, Fran Walsh, Philippa Boyens, and Guillermo del Toro.  It is the third and final installment in Peter Jackson's three-part film adaptation based on the novel "The Hobbit" by J. R. R. Tolkien, following "" (2012) and "" (2013), and together they act as a prequel to Jackson's "The Lord of the Rings" film trilogy.  It was produced by New Line Cinema, Metro-Goldwyn-Mayer and WingNut Films, and distributed by Warner Bros. Pictures.  "The Battle of the Five Armies" was released on 11 December 2014 in New Zealand, 12 December 2014 in the United Kingdom, and on 17 December 2014 in the United States.  It stars Martin Freeman, Ian McKellen, Richard Armitage, Evangeline Lilly, Lee Pace, Luke Evans, Benedict Cumberbatch, Ken Stott, and James Nesbitt.  It also features Cate Blanchett, Ian Holm, Christopher Lee, Hugo Weaving, and Orlando Bloom.  The film received mixed reviews and grossed over $956 million worldwide, making it the second highest-grossing film of 2014 and the 38th highest-grossing film of all time.  At the 87th Academy Awards, the film received a nomination for Best Sound Editing.

Messalina (1951 film): Messalina or The Affairs of Messalina is a 1951 historical drama film directed by Carmine Gallone and starring María Félix, Georges Marchal and Memo Benassi.  It was a co-production between France, Italy and Spain.  It was shot at the Cinecittà studios in Rome with sets designed by Gastone Medin and Vittorio Nino Novarese.  It was part of a growing trend of epic historical films of 1950s.  In 1954 a dubbed English version was released in the United States by Columbia Pictures.

Ponnar Shankar (film): Ponnar Shankar is a 2011 Indian epic historical drama film produced and directed by Thiagarajan.  It is a fictionalised account of the Ponnar Shankar epic, adapted from M. Karunanidhi' s novel of the same name.  It features Thiagarajan's son Prashanth in lead dual roles as warrior princes, portraying the title characters, with actresses Pooja Chopra and Divya Parameshwaran making their film debut as princesses.  The film also features an extensive cast of supporting actors with Prabhu, Rajkiran, Napoleon, Prakash Raj, Jayaram, Sneha and Kushboo amongst others.  The background score and soundtrack of the film, composed by Ilaiyaraaja, was released on 27 March 2011.

Ned Kelly (2003 film): Ned Kelly is a 2003 Australian historical drama film based on Robert Drewe's 1991 novel "Our Sunshine".  Directed by Gregor Jordan, the film's adapted screenplay was written by John Michael McDonagh.  The film dramatises the life of Ned Kelly, a legendary bushranger and outlaw who was active mostly in Victoria, the colony of his birth.  In the film, Kelly, his brother Dan, and two other associates—Steve Hart and Joe Byrne—form a gang of Irish Australians in response to Irish and English tensions that arose in 19th century Australia.  Heath Ledger stars in the title role, with Orlando Bloom, Naomi Watts and Geoffrey Rush.

Karnan (film): Karnan is a 1964 Indian Tamil-language epic historical drama film produced and directed by B. R. Panthulu.  It features Sivaji Ganesan leading an ensemble cast consisting of N. T. Rama Rao, S. A. Ashokan, R. Muthuraman, Devika, Savitri and M. V. Rajamma.  The film is based on the story of Karna, a character from the Hindu epic "Mahabharata".  He is born to an unmarried mother Kunti who abandons him in the Ganges to avoid embarrassment.  The child is discovered and adopted by a charioteer.  Karnan does not want to follow his foster father's profession, and instead, becomes a warrior.  He then befriends Duryodhana, the Kaurava prince, eventually setting the initial grounds of the Kurukshetra War, where he will join Duryodhana to fight against his own half-brothers, the Pandavas.

Kingdom of Heaven (film): Kingdom of Heaven is a 2005 epic historical drama film directed and produced by Ridley Scott and written by William Monahan.  It stars Orlando Bloom, Eva Green, Ghassan Massoud, Jeremy Irons, David Thewlis, Brendan Gleeson, Iain Glen, Marton Csokas, Liam Neeson, Edward Norton, Michael Sheen, Velibor Topic and Alexander Siddig.

Eva Green: Eva Gaëlle Green (] ; ] ; born 6 July 1980) is a French actress and model.  She started her career in theatre before making her film debut in 2003 in Bernardo Bertolucci's film "The Dreamers".  She achieved international recognition when she appeared as Sibylla, Queen of Jerusalem in Ridley Scott's historical epic "Kingdom of Heaven" (2005), and portrayed Bond girl Vesper Lynd in the "James Bond" film "Casino Royale" (2006).  In 2006, Green was awarded the BAFTA Rising Star Award.

Question: Orlando Bloom starred alongside a French actress and model in the epic historical drama film Kingdom of Heaven which was released in what year?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the epic historical drama film."
    },
    "release_year": {
      "type": "integer",
      "description": "The year the film was released."
    },
    "main_actors": {
      "type": "array",
      "description": "A list of key actors in the film, including Orlando Bloom and the specified French actress/model.",
      "items": {
        "type": "object",
        "properties": {
          "actor_name": {
            "type": "string",
            "description": "The name of the actor."
          },
          "is_french_actress_model": {
            "type": "boolean",
            "description": "True if the actor is the French actress and model mentioned in the question."
          }
        },
        "required": [
          "actor_name"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "film_title",
    "release_year",
    "main_actors"
  ],
  "additionalProperties": false
}
