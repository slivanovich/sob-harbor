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
Emma Goldman: The Anarchist Guest: Emma Goldman: The Anarchist Guest is a documentary about Emma Goldman that was released in 2000.  It was directed by Canadian sociologist and filmmaker Coleman Romalis.  The film was screened at the 2000 San Francisco Jewish Film Festival.

Winifred Peck: Winifred Frances Peck (née Knox) (1882, Headington – 20 November 1962) (Lady Peck) was an author of literary fiction and biographies.  She was a member of a remarkable family: her father was Edmund Arbuthnott Knox, the fourth Bishop of Manchester, and her siblings were E. V. Knox, editor of "Punch", Ronald Knox, theologian and writer, Dilly Knox, cryptographer, Wilfred Lawrence Knox, clergyman, and Ethel Knox.  Peck's niece was the Booker Prize-winning author Penelope Fitzgerald who wrote a biography of her father, E. V. Knox, and her uncles, entitled "The Knox Brothers".

Emma Goldman: Emma Goldman (June 27 [O.S. June 15] , 1869May 14, 1940) was an anarchist political activist and writer.  She played a pivotal role in the development of anarchist political philosophy in North America and Europe in the first half of the 20th century.

The Traffic in Women: "The Traffic in Women" is an essay written by anarchist writer Emma Goldman in 1910.  It has been published in various ways, including within Emma Goldman’s "Anarchism and Other Essays" (1911), published by Mother Earth, and as the named, leading essay of a collection of Emma Goldman essays: "The Traffic in Women, and Other Essays on Feminism" (1970, Times Change Press, 1971 paperback). " Mother Earth" was a monthly anarchist magazine founded by Goldman, Max Baginski, and others in 1906.  The essay is one of more than 20 articles that Goldman wrote during 1906 to 1940.

Living My Life: Living My Life is the autobiography of Lithuanian-born anarchist Emma Goldman, published in two volumes in 1931 (Alfred A. Knopf) and 1934 (Garden City Publishing Company).  Goldman wrote it in Saint-Tropez, France, following her disillusionment with the Bolshevik role in the Russian revolution.  The text thoroughly covers her personal and political life from early childhood through to 1927, and has constantly remained in print since, in original and abridged editions.  Since the autobiography was published nine years before Goldman died in 1940, it does not record her role in the Spanish Civil War.

Penelope Fitzgerald: Penelope Fitzgerald (17 December 1916 – 28 April 2000) was an English Booker Prize-winning novelist, poet, essayist and biographer.  In 2008, "The Times" included her in a list of "the 50 greatest British writers since 1945".  In 2012, "The Observer" named her final novel, "The Blue Flower" one of "the ten best historical novels".

My Disillusionment in Russia: My Disillusionment in Russia is a book by Emma Goldman, published in 1923 by Doubleday, Page & Co.  The book was based on a much longer manuscript entitled "My Two Years in Russia" which was an eyewitness account of events in Russia from 1920 to 1921 that ensued in the wake of the Russian Revolution of 1917 and which culminated in the Kronstadt rebellion.  Long-concerned about developments with the "Bolsheviki", Goldman described the rebellion as the "final wrench.  I [Goldman] saw before me the Bolshevik State, formidable, crushing every constructive revolutionary effort, suppressing, debasing, and disintegrating everything."

Eleanor Fitzgerald: Mary Eleanor Fitzgerald (March 16, 1877 – March 30, 1955) was an American editor and theatre professional, best known for her association with Emma Goldman and Alexander Berkman, and with the Provincetown Players.

Sasha and Emma: Sasha and Emma: The Anarchist Odyssey of Alexander Berkman and Emma Goldman is a 2012 history book about Alexander Berkman and Emma Goldman by Paul and Karen Avrich.  It was a "New York Times Book Review" Editors' Choice for 2012.

Anarchism and Other Essays: Anarchism and Other Essays is a 1910 essay collection by Russian-American anarchist philosopher Emma Goldman, first published by Mother Earth Publishing.  The essays outline Goldman's anarchist views on a number of subjects, most notably the oppression of women and perceived shortcomings of first wave feminism, but also prisons, political violence, sexuality, religion, nationalism and art theory.  Hippolyte Havel contributed a short biography of Goldman to the anthology.

Question: Which writer was also a poet, Penelope Fitzgerald or Emma Goldman?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_identified": {
      "type": "string",
      "description": "The name of the writer who was also a poet."
    },
    "was_also_a_poet": {
      "type": "boolean",
      "description": "True if the identified person was a poet, false otherwise."
    },
    "other_professions": {
      "type": "array",
      "description": "A list of other professions or roles of the identified person.",
      "items": {
        "type": "string"
      }
    },
    "compared_person": {
      "type": "string",
      "description": "The name of the other writer mentioned in the question for comparison."
    },
    "compared_person_was_poet": {
      "type": "boolean",
      "description": "True if the compared person was a poet, false otherwise."
    },
    "compared_person_professions": {
      "type": "array",
      "description": "A list of professions or roles of the compared person.",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "person_identified",
    "was_also_a_poet",
    "other_professions",
    "compared_person",
    "compared_person_was_poet",
    "compared_person_professions"
  ],
  "additionalProperties": false
}
