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
Gladys Powers: Gladys Stokes Luxford Powers (10 May 1899 – 15 August 2008) was thought to be, at age 109, the last female veteran of the First World War following the 27 March 2007 death of fellow 109-year-old Charlotte Winters from the US.  However the subsequent discovery of fellow Britons Ivy Campany, who died on 19 December 2008, and Florence Green has disproved this.  Regardless, Powers was the last veteran living in Canada, following the death of Dwight Wilson on 9 May 2007, the day before Powers' 108th birthday.  The last Canadian-born veteran, 109-year-old John Babcock, later moved to the United States where he lived until his death on 18 February 2010.

List of last surviving World War I veterans: The following is a list of known veterans of the First World War (28 July 1914 – 11 November 1918) who died in 2009 (5 veterans), 2010 (1 veteran), 2011 (2 veterans) and 2012 (1 veteran).  WRAF member Florence Green, who died on 4 February 2012, was the last surviving veteran of any nation.

Harry Patch: Henry John Patch (17 June 1898 – 25 July 2009), dubbed in his later years "the Last Fighting Tommy", was a British supercentenarian, briefly the oldest man in Europe and the last surviving combat soldier of the First World War from any country.  He is known to have fought in the trenches of the Western Front.  Patch was the longest surviving combat soldier of World War I, but he was the fifth longest surviving veteran of any sort from World War I, behind British veterans Claude Choules and Florence Green, Frank Buckles of the United States and John Babcock of Canada.  At the time of his death, aged 111 years, 1 month, 1 week and 1 day, Patch was the third-oldest man in the world and the oldest man in Europe.

Allie Esiri: Allie Esiri (born 1967), née Allie Byrne, is a British writer and former stage, film, and television actress.  She created "iF Poems", an educational poetry app, the accompanying hardback anthology "iF: A Treasury of Poems for Almost Every Possibility", and "The Love Book", both an interactive literary app on iOS and Android and a hardback book of best-loved poems, quotations, and letters on the theme of love.  Esiri's anthology, published by Pan Macmillan on 8 September 2016, "A Poem for Every Night of the Year" won the IBW 2017 (Independent Bookshop Award, best Children's book).  Esiri's new anthology, "A Poem for Every Day of the Year" was published by Pan Macmillan on 7 September 2017.

Anne Middleton: Anne Middleton (18 Jul 1940–23 Nov 2016) was an American medievalist, and the Florence Green Bixby Professor of English at the University of California, Berkeley.

List of last World War I veterans by country: This is a list of the last World War I veterans to die by country.  The last living veteran of World War I (28 July 1914 – 11 November 1918) was Florence Green, a British citizen who served in the Allied armed forces, and who died 4 February 2012, aged 110.  The last combat veteran was Claude Choules who served in the British Royal Navy (and later the Royal Australian Navy) and died 5 May 2011, aged 110.  The last veteran who served in the trenches was Harry Patch (British Army) who died on 25 July 2009, aged 111.  The last Central Powers veteran, Franz Künstler of Austria-Hungary, died on 27 May 2008 at the age of 107.

Colette Descombes: Colette Descombes is a French film actress, active between 1961 and 1978.  If she was of legal age (18) in 1961, she was probably born circa 1943, but her birthdate is nowhere on the internet.

The Bookshop (film): The Bookshop is a Spanish, British and German coproduced drama film.  Directed and written by the Spanish director Isabel Coixet, based on the novel by Penelope Fitzgerald, the film stars Emily Mortimer as Florence Green, Patricia Clarkson as Violet Gamart, and (Bill Nighy) as Edmund Brundish.  This is the third collaboration between Patricia Clarkson and Isabel Coixet, after Elegy and Learning to Drive, and the second time Emily Mortimer and Patricia Clarkson appear together in 2017.

Ivy Campany: Ivy Lillian Campany (23 September 1901 – 19 December 2008) was, at age 107, the second from last World War I female army veteran of any country.  The last was Florence Green (1901–2012), who was not identified as a veteran of the conflict until January 2010.  This meant that Campany was believed to be the conflict's last surviving female veteran by the time of her death in December 2008.

Emily Mortimer: Emily Kathleen Anne Mortimer (born 1 December 1971) is an English actress and screenwriter.  She began acting in stage productions, and has since appeared in several film and television roles.  In 2003, she won an Independent Spirit Award for her performance in "Lovely and Amazing".  She is also known for playing roles in "Match Point" (2005), "Lars and the Real Girl" (2007), "Chaos Theory" (2008), "Harry Brown" (2009), "Shutter Island" (2010), "Hugo" (2011), and the HBO series "The Newsroom".

Question: What is the birthdate of the actress who portrays Florence Green in the film The Bookshop?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "character_portrayed": {
      "type": "string",
      "description": "The name of the character portrayed in the film."
    },
    "actress_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The full name of the actress."
        },
        "birthdate": {
          "type": "string",
          "description": "The birthdate of the actress in 'Day Month Year' format."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the actress."
        }
      },
      "required": [
        "name",
        "birthdate",
        "nationality"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "film_title",
    "character_portrayed",
    "actress_details"
  ],
  "additionalProperties": false
}
