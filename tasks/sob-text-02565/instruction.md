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
Common Wealth: Economics for a Crowded Planet: Common Wealth: Economics for a Crowded Planet is a 2008 New York Times bestseller book by economist Jeffrey Sachs.  Sachs began promoting electric vehicles (PHEVs) in this book.  In this book, Sachs states that the world of economics does not depend on the law of market-determined supply and demand.

Maneet Ahuja: Maneet Ahuja (born 1984) is an American author, journalist, television news producer, and hedge fund specialist.  She is a producer of CNBC's morning business news program, "Squawk Box".  Her 2012 book, "The Alpha Masters: Unlocking the Genius of the World's Top Hedge Funds", was published by John Wiley & Sons and nominated for an FT / Goldman Sachs Book of the Year Award. " Forbes" named her to their "30 Under 30" list of media figures for 2012.  Ahuja has also produced a number of business events including CNBC's Delivering Alpha conference, a hedge fund summit that she created and co-developed.  Ahuja serves on the Council of Advocates for Mt. Sinai Hospital and is on the United Nations Commission on the Status of Women.  Her next book is on Sovereign Wealth Funds.

Jeffrey Sachs: Jeffrey David Sachs ( ; born November 5, 1954) is an American economist and director of the Earth Institute at Columbia University, where he holds the title of University Professor, the highest rank Columbia bestows on its faculty.  He is known as one of the world's leading experts on economic development and the fight against poverty.

The Price of Civilization: The Price of Civilization: Reawakening American Virtue and Prosperity (ISBN  ) is a book by economist Jeffrey Sachs.  It was published by Random House on October 4, 2011 in the US and by Bodley Head (UK 6 Oct 2011).  Sachs criticizes excessive lobbying, as well as a poor response by American government to globalization, and describes American politics as a corporatocracy in which "powerful corporate interest groups dominate the policy agenda."  Sachs suggests that both political parties are right-of-center, and identifies four powerful lobbies as (1) military-industrial complex (2) Wall Street–Washington complex (3) Big Oil–transport–military complex (4) the health care industry.

Nina Munk: Nina Munk (born 1967) is a Canadian-American journalist and non-fiction author.  She is a contributing editor at "Vanity Fair", where she writes about finance and business, and is the author of "The Idealist: Jeffrey Sachs and the Quest to End Poverty", released by Doubleday in September 2013, and "Fools Rush In: Jerry Levin, Steve Case, and the Unmaking of Time Warner".

The End of Poverty: The End of Poverty: Economic Possibilities for Our Time (ISBN  ) is a 2005 book by American economist Jeffrey Sachs.  It was a "New York Times" bestseller.

Global Competitiveness Report: The Global Competitiveness Report (GCR) is a yearly report published by the World Economic Forum.  Since 2004, the "Global Competitiveness Report" ranks countries based on the Global Competitiveness Index, developed by Xavier Sala-i-Martin and Elsa V. Artadi.  Before that, the macroeconomic ranks were based on Jeffrey Sachs's "Growth Development Index" and the microeconomic ranks were based on Michael Porter's" Business Competitiveness Index".  The "Global Competitiveness Index" integrates the macroeconomic and the micro/business aspects of competitiveness into a single index.

Aristide and the Endless Revolution: Aristide and the Endless Revolution is a 2005 feature documentary directed and produced by Nicolas Rossier about former Haitian President Jean-Bertrand Aristide and the coup d'etat that ousted him from the country in 2004.  Rossier was the first media professional to get exclusive access to Aristide while in exile and the resultant interview is featured in the film, as well as interviews with many experts on Haiti, including U.S. Representative Maxine Waters, noted economist Jeffrey Sachs and Aristide's lawyer Ira J. Kurzban.

Xiaolan Fu: Xiaolan Fu (傅晓岚) is the Founding Director of the Technology and Management Centre for Development (TMCD), Professor of Technology and International Development and Fellow of Green Templeton College.  She was appointed by the Secretary-General of the United Nations to the Ten-Member High Level Advisory Group of the UN Technology Facilitation Mechanism and to the Governing Council of the UN's Technology Bank for Least Developed Countries.  She is also a member of the UN SDSN Leadership Council led by Jeffrey Sachs and a member of the Council for Global Economic Transformation co-chaired by Joseph Stiglitz and Michael Spence.

World Happiness Report: The World Happiness Report is a measure of happiness published by the United Nations Sustainable Development Solutions Network.  The World Happiness Report is edited by John F. Helliwell, Richard Layard and Jeffrey Sachs.

Question: What was the achievement Jeffrey Sachs book "The End of Poverty" earned?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "book_title": {
      "type": "string",
      "description": "The title of the book."
    },
    "author_name": {
      "type": "string",
      "description": "The author of the book."
    },
    "publication_year": {
      "type": "integer",
      "description": "The year the book was published."
    },
    "achievement": {
      "type": "string",
      "description": "The specific achievement earned by the book."
    },
    "achievement_type": {
      "type": "string",
      "description": "The category of the achievement (e.g., 'bestseller')."
    }
  },
  "required": [
    "book_title",
    "author_name",
    "publication_year",
    "achievement",
    "achievement_type"
  ],
  "additionalProperties": false
}
