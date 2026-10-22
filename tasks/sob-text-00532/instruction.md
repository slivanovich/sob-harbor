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
Hero and Leander (poem): Hero and Leander is a poem by Christopher Marlowe that retells the Greek myth of Hero and Leander.  After Marlowe's untimely death it was completed by George Chapman.  The minor poet Henry Petowe published an alternative completion to the poem.  The poem was first published posthumously, five years after Marlowe's demise.

Nicholas Skeres: Nicholas Skeres (March 1563 – c. 1601) was an Elizabethan con-man and government informer—i.e. a "professional deceiver"—and one of the three "gentlemen" who were with the poet and playwright Christopher Marlowe when he was killed in Deptford in May 1593.  Together with another of the men there, Robert Poley, he had played a part in the discovery of the Babington plot against the life of the Queen in 1586, and at the time of Marlowe's death was engaged in a money-lending swindle with the third of them, Marlowe's reported killer Ingram Frizer.

Return to the Hiding Place: Return to the Hiding Place (2013) is a film based upon the factual accounting of Hans Poley's World War II encounter with Corrie ten Boom, his involvement in the Dutch resistance and the wartime harboring of Jewish refugees.  A non-Jewish fugitive himself, for refusing to pledge his allegiance to the Nazi party; Poley was the first person hidden from the Nazis in Ten Boom House, which today is a museum in Haarlem, Netherlands.  The film is adapted, in part, from Poley's book, "Return to the Hiding Place" (1993), personal recollections, relayed to screenwriter Dr. Peter C. Spencer, and research from the Dutch National Archives.  The film is neither a prequel, nor a sequel to the 1975 film, "The Hiding Place"; rather, "Return to the Hiding Place" is a congruent accounting of Dutch underground resistance efforts from Hans Poley's perspective.  It was directed by Peter C. Spencer and starred John Rhys-Davies, Mimi Sagadin and Craig Robert Young.

Open information extraction: In natural language processing, open information extraction (OIE) is the task of generating a structured, machine-readable representation of the information in text, usually in the form of triples or n-ary propositions.  A proposition can be understood as truth-bearer, a textual expression of a potential fact (e.g., "Dante wrote the Divine Comedy"), represented in an amenable structure for computers [e.g., ("Dante", "wrote", "Divine Comedy")].  An OIE extraction normally consists of a relation and a set of arguments.  For instance, ("Dante", "passed away in" "Ravenna") is a proposition formed by the relation "passed away in" and the arguments "Dante" and "Ravenna".  The first argument is usually referred as the subject while the second is considered to be the object.

Bob Poley: Robert Poley (born November 15, 1955 in Saskatoon, Saskatchewan) is a former professional Canadian football offensive lineman who played fifteen seasons in the Canadian Football League for two different teams.  He was named CFL All-Star in 1986.

Thomas Walsingham (literary patron): Sir Thomas Walsingham (c. 1561 – 11 August 1630) was a courtier to Queen Elizabeth I and literary patron to such poets as Thomas Watson, Thomas Nashe, George Chapman and Christopher Marlowe.  He was related to Elizabeth's spymaster Francis Walsingham and the employer of Marlowe's murderer Ingram Frizer.  This connection is one of the reasons offered for suggesting that Marlowe's death may have been linked with intelligence work, and not a dispute over a bill for food and accommodation, as in the coroner's verdict.

Christopher Marlowe: Christopher Marlowe, also known as Kit Marlowe (baptised 26 February 156430 May 1593), was an English playwright, poet and translator of the Elizabethan era.  Marlowe was the foremost Elizabethan tragedian of his day.  He greatly influenced William Shakespeare, who was born in the same year as Marlowe and who rose to become the pre-eminent Elizabethan playwright after Marlowe's mysterious early death.  Marlowe's plays are known for the use of blank verse and their overreaching protagonists.

Robert Poley: Robert Poley, or Pooley (fl.  1568–1602) was an English double agent, government messenger and "agent provocateur" employed by members of the Privy Council during the reign of Queen Elizabeth I; he was described as "the very genius of the Elizabethan underworld".  Poley is particularly noted for his central role in uncovering the so-called Babington plot to assassinate the Queen in 1586, and for being a witness of, and even a possible party to, the reported killing in self-defence by Ingram Frizer of the famous poet/dramatist Christopher Marlowe in May 1593.

Englands Helicon: Englands Helicon is an anthology of Elizabethan pastoral poems compiled by John Flasket, and first published in 1600.  There was an enlarged edition in 1614.  The poets involved cannot all be identified, since there are a number of poems marked as 'anonymous': they do include Edmund Bolton, William Byrd, Henry Chettle, Michael Drayton, Robert Greene, Christopher Marlowe, Anthony Munday, George Peele, Walter Raleigh, Henry Constable, William Shakespeare, Philip Sidney, Edmund Spenser, John Wootton, William Smith.  The most celebrated poem is Marlowe's 'Come live with me and be my love'.  This and several other lyrics have musical settings extant, in this case by William Corkine.

Marlowe Memorial: The Marlowe Memorial is a statue and four statuettes erected in memory of the playwright and poet Christopher Marlowe in 1891 in Canturbury, England.  The memorial was commissioned by a Marlowe Memorial Committee, and comprises a bronze statue, The Muse of Poetry sculpted by Edward Onslow Ford, standing on a plinth decorated with statuettes of actors playing Marlowe roles.  The statue is now situated outside the city's Marlowe Theatre.

Question: Who passed away first Robert Poley or Christopher Marlowe ?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_a_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "death_year": {
          "type": "integer"
        }
      },
      "required": [
        "name",
        "death_year"
      ],
      "additionalProperties": false
    },
    "person_b_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "activity_end_year": {
          "type": "integer",
          "description": "The last known year of activity for the person, implying they were alive until at least this point."
        }
      },
      "required": [
        "name",
        "activity_end_year"
      ],
      "additionalProperties": false
    },
    "first_to_pass_away_name": {
      "type": "string",
      "description": "The name of the person who passed away first."
    },
    "comparison_reasoning": {
      "type": "string",
      "description": "Explanation of how the conclusion was reached based on the provided dates."
    }
  },
  "required": [
    "person_a_details",
    "person_b_details",
    "first_to_pass_away_name",
    "comparison_reasoning"
  ],
  "additionalProperties": false
}
