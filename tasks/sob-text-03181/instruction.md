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
Luis Omar Salinas: Luis Omar Salinas (1937–2008) was a leading Chicano poet who published a number of well-received collections of poetry, including the "Crazy Gypsy", which has been described as "a classic of contemporary and Chicano poetry"), "I Go Dreaming Serenades", and "Afternoon of The Unreal".  He was awarded the Stanley Kunitz award by "Columbia Magazine" for one of his poems, and a General Electric Foundation Award.  Salinas is regarded as "one of the founding fathers of Chicano poetry in America," with many of his poems being "canonized in U.S. Hispanic literature."

Helen Curtin Moskey: Helen Curtin Moskey (March 27, 1931, Hartford, Connecticut – March 25, 2003, Hartford) was an Irish-American poet of dual U.S.-Irish nationality.  She earned her Bachelor of Arts degree in English, with honors, from Trinity College (Connecticut), Hartford, Connecticut, and studied poetry with several established American poets, including Mark Doty, Stanley Kunitz, and Yusef Komunyakaa, and at the Fine Arts Work Center in Provincetown, Massachusetts.  Additionally, the Irish poet Eiléan Ní Chuilleanáin was a friend and advisor.  Moskey’s work appeared in occasional compilations of poetry.  At the time of her death, she was preparing a volume of her selected poetry for publication.

Alice Mayhew: Alice Mayhew is a Vice-President and Editorial Director for Simon & Schuster.  Mayhew has edited many notable authors Bob Woodward, President Jimmy Carter, Doris Kearns Goodwin, David Brooks, and Ruth Bader Ginsburg.  Mayhew is known for publishing books about Washington, D.C., such as "All the President's Men" by Bob Woodward and Carl Bernstein using a genre which is known as a political narrative, a subgenre of creative nonfiction.

Fine Arts Work Center: The Fine Arts Work Center is a non-profit enterprise devoted to encouraging the growth and development of emerging visual artists and writers through residency programs, to the propagation of aesthetic values and experience, and to the restoration of the year-round vitality of the historic art colony of Provincetown, Massachusetts.  The Work Center was founded in 1968 by a group of American artists and writers to support promising individuals in the early stages of their creative careers.  The Work Center, whose founders included Stanley Kunitz, Robert Motherwell, Myron Stout and Jack Tworkov, annually offers ten writers and ten visual artists seven-month residencies, including a work area and a monthly stipend.  The Center also offers a Master of Fine Arts degree in collaboration with the Massachusetts College of Art and Design, seasonal programs, and readings and other events.  The Center was awarded a 2010 National Endowment for the Arts Access to Artistic Excellence grant to support the Winter Fellowship program.

Charlotte Turner Smith: Charlotte Turner Smith (4 May 1749 – 28 October 1806) was an English Romantic poet and novelist.  She initiated a revival of the English sonnet, helped establish the conventions of Gothic fiction, and wrote political novels of sensibility.  A successful writer, she published ten novels, three books of poetry, four children's books, and other assorted works, over the course of her career.  She saw herself as a poet first and foremost, poetry at that period being considered the most exalted form of literature.  Scholars now credit her with transforming the sonnet into an expression of woeful sentiment.  During adulthood, Charlotte Smith eventually left husband Benjamin Smith and began writing to support their children.  Smith's struggle to provide for her children and her frustrated attempts to gain legal protection as a woman provided themes for her poetry and novels; she included portraits of herself and her family in her novels as well as details about her life in her prefaces.  Her early novels are exercises in aesthetic development, particularly of the Gothic and sentimentality.  "The theme of her many sentimental and didactic novels was that of a badly married wife helped by a thoughtful sensible lover" (Smith's entry in "British Authors Before 1800: A Biographical Dictionary" Ed.  Stanley Kunitz and Howard Haycraft.   New York: H.W. Wilson, 1952.  pg.  478.)  Her later novels, including "The Old Manor House", often considered her best, supported the ideals of the French Revolution.   After 1798, however, Smith's popularity waned and by 1803 she was destitute and ill—she could barely hold a pen, and sold her books to pay off her debts.  In 1806, Smith died.  Largely forgotten by the middle of the 19th century, her works have now been republished and she is recognized as an important Romantic writer.

Atukwei Okai: Atukwei (John) Okai (born 1941) is a Ghanaian poet, cultural activist and academic.  He is Secretary-General of the Pan African Writers' Association, and former president of the Ghana Association of Writers.  His early work was published under the name John Okai.  With his poems rooted in the oral tradition, he is generally acknowledged to be the first real performance poets to emerge from Africa, and his work has been called "also politically radical and socially conscious, one of his great concerns being Pan-Africanism".  His performances on radio and television worldwide include an acclaimed 1975 appearance at Poetry International at Queen Elizabeth Hall in London, where he shared the stage with US poets Stanley Kunitz and Robert Lowell, and Nicolas Guillen of Cuba.

Stanley Kunitz: Stanley Jasspon Kunitz ( ; July 29, 1905May 14, 2006) was an American poet.  He was appointed Poet Laureate Consultant in Poetry to the Library of Congress twice, first in 1974 and then again in 2000.

Bob Woodward: Robert Upshur "Bob" Woodward (born March 26, 1943) is an American investigative journalist and non-fiction author.  He has worked for "The Washington Post" since 1971 as a reporter and is now an associate editor there.

Blue Moon Tavern: The Blue Moon is a tavern located on the west edge of the University District, Seattle, Washington, that has been visited by many counterculture icons over the years.  It opened in April 1934, soon after the repeal of Prohibition in December 1933.  It is the first and oldest tavern in the U-District.  It was an instant hit with students (together with the still-thriving Duchess Tavern in Ravenna); under state law, students had to trek one mile from the campus to purchase drinks.  The Blue Moon was one of the rare bars outside of the Central District to serve African American servicemen during World War II.  The tavern also provided a haven for UW professors such as Joe Butterworth who were caught up in the McCarthyist purge.  It had further heyday in the 1950s and 1960s.  Regulars included author Tom Robbins, poets Theodore Roethke, Richard Hugo, Carolyn Kizer, Stanley Kunitz, and David Wagoner, and painters Richard Gilkey and Leo Kenney.  Visitors included Dylan Thomas, Ken Kesey, Allen Ginsberg and Mik Moore.

Poetry Society of America: The Poetry Society of America is a literary organization founded in 1910 by poets, editors, and artists including Witter Bynner.  It is the oldest poetry organization in the United States.  Past members of the society have included such renowned writers as Robert Frost, Langston Hughes, Edna St. Vincent Millay, Marianne Moore, and Wallace Stevens.  Current members include John Ashbery, Louise Glück, Rita Dove, Stanley Kunitz, Robert Pinsky, Molly Peacock, Billy Collins and James Tate.

Question: What profession do both Bob Woodward and Stanley Kunitz have?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_one": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "profession": {
          "type": "string"
        }
      },
      "required": [
        "name",
        "profession"
      ],
      "additionalProperties": false
    },
    "person_two": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "profession": {
          "type": "string"
        }
      },
      "required": [
        "name",
        "profession"
      ],
      "additionalProperties": false
    },
    "shared_profession": {
      "type": "string",
      "description": "The profession shared by both individuals."
    }
  },
  "required": [
    "person_one",
    "person_two",
    "shared_profession"
  ],
  "additionalProperties": false
}
