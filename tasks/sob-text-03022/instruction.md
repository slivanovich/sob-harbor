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
Cold Comfort Farm: Cold Comfort Farm is a comic novel by English author Stella Gibbons, published in 1932.  It parodies the romanticised, sometimes doom-laden accounts of rural life popular at the time, by writers such as Mary Webb.

Patrick McCabe (novelist): Patrick McCabe (born 27 March 1955) is an Irish writer.  Known for his mostly dark and violent novels set in contemporary—often small-town—Ireland, McCabe has been twice shortlisted for the Booker Prize, for "The Butcher Boy" and "Breakfast on Pluto", both of which have been made into films.

The Country Life (novel): The Country Life is a comedic novel by Rachel Cusk, first published in 1997, which draws on Stella Gibbons' "Cold Comfort Farm" and Charlotte Brontë's "Jane Eyre".  It won a 1998 Somerset Maugham Award.

Breakfast on Pluto (film): Breakfast on Pluto is a 2005 British-Irish comedy-drama film written and directed by Neil Jordan and based on the novel of the same name by Patrick McCabe, as adapted by Jordan and McCabe.  This dark comedy stars Cillian Murphy as a transgender foundling searching for love and her long-lost mother in small town Ireland and London in the 1970s.

Cold Comfort Farm (film): Cold Comfort Farm is a 1995 British comedy film directed by John Schlesinger and produced by the BBC and Thames Television, an adaptation of Stella Gibbons' 1932 book of the same name, the film stars Kate Beckinsale, Joanna Lumley, Ian McKellen and Rufus Sewell.  Originally broadcast on 1 January 1995 on the BBC, it was Schlesinger's final film shot in his home country of Britain, and was picked up for theatrical release in North America through Gramercy Pictures, where it was a small success.

Catholic (album): catholic is the fourth solo album from Gavin Friday, written and recorded with musician Herbie Macken and released in 2011.  It was released in Ireland on Good Friday (22 April), 16 years after the release of his previous album, "Shag Tobacco".  "catholic" deals with concepts of letting go and coming to terms with loss.  It was produced by Ken Thomas (Throbbing Gristle, Cocteau Twins, Sigur Rós) and recorded in Dublin, Cork and West Yorkshire.  Patrick McCabe wrote the novella "Requiem for the Dying" for the album liner notes.  The video for "Able" was directed by Kevin Godley.

Breakfast on Pluto: Breakfast on Pluto is a 1998 novel by Patrick McCabe.  The book was shortlisted for the 1998 Booker Prize, and was adapted for the screen by McCabe and Neil Jordan; Jordan directed the 2005 film.  The author derived the novel's title from the 1969 hit record "Breakfast On Pluto" by Don Partridge.

José C. Vales: José C. Vales (born 1965, Zamora) is a Spanish writer and translator of English literature.  He studied in Salamanca and Madrid.  He has translated numerous English and American authors into Spanish, including Dickens, Trollope, Austen, Wilkie Collins, Defoe, Mary Shelley, Arnold Bennett, Eudora Welty, Stella Gibbons, E.F. Benson, and Edmund Crispin.

The Butcher Boy (1997 film): The Butcher Boy is an 1997 Irish-American tragicomic drama film adapted to film by Neil Jordan and Patrick McCabe from McCabe's 1992 novel of the same name.

Stella Gibbons: Stella Dorothea Gibbons (5 January 1902 – 19 December 1989) was an English author, journalist, and poet.  She established her reputation with her first novel, "Cold Comfort Farm" (1932) which has been reprinted many times.  Although she was active as a writer for half a century, none of her later 22 novels or other literary works—which included a sequel to "Cold Comfort Farm"—achieved the same critical or popular success.  Much of her work was long out of print before a modest revival in the 21st century.

Question: Stella Gibbons and Patrick McCabe, have which similar occupation?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_1_name": {
      "type": "string",
      "description": "The name of the first person mentioned."
    },
    "person_2_name": {
      "type": "string",
      "description": "The name of the second person mentioned."
    },
    "common_occupation": {
      "type": "string",
      "description": "The occupation shared by both individuals."
    },
    "person_1_specific_roles": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of specific roles or types of work for the first person related to the common occupation."
    },
    "person_2_specific_roles": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of specific roles or types of work for the second person related to the common occupation."
    }
  },
  "required": [
    "person_1_name",
    "person_2_name",
    "common_occupation",
    "person_1_specific_roles",
    "person_2_specific_roles"
  ],
  "additionalProperties": false
}
