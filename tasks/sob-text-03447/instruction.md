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
Christopher Marlowe: Christopher Marlowe, also known as Kit Marlowe (baptised 26 February 156430 May 1593), was an English playwright, poet and translator of the Elizabethan era.  Marlowe was the foremost Elizabethan tragedian of his day.  He greatly influenced William Shakespeare, who was born in the same year as Marlowe and who rose to become the pre-eminent Elizabethan playwright after Marlowe's mysterious early death.  Marlowe's plays are known for the use of blank verse and their overreaching protagonists.

Shadowland (Arnold novel): "Shadowland: Search for Frances Farmer" is a 1978 biographical novel by William Arnold, ostensibly about the life of actress Frances Farmer.  The book is a fictionalized account which was further distorted when adapted as the film "Frances" in 1982.  Arnold sued for copyright infringement, claiming the film's screenplay writers appropriated several of his "fictionalized" elements, but eventually lost.

Charles de Batz de Castelmore d'Artagnan: Charles Ogier de Batz de Castelmore, Comte d'Artagnan (] ) ( 1611 – 25 June 1673) served Louis XIV as captain of the Musketeers of the Guard and died at the Siege of Maastricht in the Franco-Dutch War.  A fictionalized account of his life by Gatien de Courtilz de Sandras formed the basis for the d'Artagnan Romances of Alexandre Dumas, most famously including "The Three Musketeers" (1844).  The heavily fictionalized version of d'Artagnan featured in Dumas' works and their subsequent screen adaptations is now far more widely known than the real historical figure.

Too Close to the Sun: Too Close to the Sun is a musical with a book by Roberto Trippini and music and lyrics by Trippini and John Robinson, based on a play by Ron Read.  The musical is a fictionalized account of the last days in the life of Ernest Hemingway.

Jammers Minde: Jammers Minde (literally A Memory of Lament), translated into English as Memoirs of Leonora Christina, is an autobiography completed in 1674 by Leonora Christina, daughter of Christian IV of Denmark and Kirsten Munk.  The work, first published in 1869, is included in the Danish Culture Canon.  It is considered to be the finest piece of prose work written in 17th-century Denmark.  It relates a partly fictionalized account of Christina's time during captivity, with a detailed personal account of prison life, often drawing upon biblical references and black humour, and contrasting the comical with the macabre.  Radical for its period in its personal account, it is considered an existential religious writing.

The Invention of Everything Else: The Invention of Everything Else is a novel written by American author Samantha Hunt, published in 2008.  The novel presents a fictionalized account of the last days in the life of Nikola Tesla, the Serbian-American electrical engineer.  Other fictionalized versions of historical characters include Thomas Edison (a rival), George Westinghouse, and Mark Twain.  Tesla is the novel's protagonist along with a chambermaid named Louisa with whom he shares some common interests including science and pigeons.  Much of the book takes place in the New Yorker Hotel.  The book also includes elements of science fiction, namely time travel.

My Life in Crime: My Life in Crime is a 1984 novel by Kenyan author John Kiriamiti.  It is a fictionalized account of Kiriamiti's criminality in Kenya during the 1960s and 1970s.  The novel details Kiriamiti's crimes under the alias Jack Zollo that led to his imprisonment.  It is the first novel in Kiriamiti's "My Life..." trilogy, which is currently being made into a film.

The Wave (novel): The Wave is a 1981 young adult novel by Todd Strasser under the pen name Morton Rhue (though it has been reprinted under Todd Strasser's real name).  It is a novelization of a teleplay by Johnny Dawkins for the movie "The Wave", a fictionalized account of the "Third Wave" teaching experiment by Ron Jones that took place in a Ellwood P. Cubberley High School history class in Palo Alto, California.  The novel by Strasser won the 1981 Massachusetts Book Award for Children's/Young Adult literature.

Marlowe (musical): Marlowe is a 1981 musical with a book by Leo Rost, lyrics by Rost and Jimmy Horowitz, and music by Horowitz.  Despite a claim in the "Playbill" that "the story of this drama is essentially true and accurate," much of it is a fictionalized account of the life of Elizabethan playwright Christopher Marlowe.

The Unsinkable Molly Brown (film): The Unsinkable Molly Brown is a 1964 American musical film directed by Charles Walters and starring Debbie Reynolds.  The screenplay by Helen Deutsch is based on the book of the 1960 musical "The Unsinkable Molly Brown" by Richard Morris.  The song score was composed by Meredith Willson.  The plot is a fictionalized account of the life of Margaret Brown, who survived the 1912 sinking of the  .  Debbie Reynolds was nominated for the Academy Award for Best Actress for her portrayal of Brown.

Question: Who was born in the same year as the playwright who had a musical fictionalized account of his life made in 1981?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "target_playwright": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the playwright whose life was fictionalized."
        },
        "era": {
          "type": "string",
          "description": "The historical era the playwright belonged to."
        }
      },
      "required": [
        "name",
        "era"
      ],
      "additionalProperties": false
    },
    "fictionalized_musical": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the musical that fictionalized the playwright's life."
        },
        "year_released": {
          "type": "integer",
          "description": "The year the musical was released."
        }
      },
      "required": [
        "title",
        "year_released"
      ],
      "additionalProperties": false
    },
    "person_born_in_same_year": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the person born in the same year as the target playwright."
        },
        "relationship_detail": {
          "type": "string",
          "description": "A description of the relationship to the playwright regarding birth year."
        }
      },
      "required": [
        "name",
        "relationship_detail"
      ],
      "additionalProperties": false
    },
    "final_answer": {
      "type": "string",
      "description": "The name of the person who was born in the same year as the playwright."
    }
  },
  "required": [
    "target_playwright",
    "fictionalized_musical",
    "person_born_in_same_year",
    "final_answer"
  ],
  "additionalProperties": false
}
