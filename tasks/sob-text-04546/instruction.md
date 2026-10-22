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
William Buckley (convict): William Buckley (178030 January 1856) was an English convict who was transported to Australia, escaped, was given up for dead, and lived in an Aboriginal community for many years.

Mark Jeffrey: Mark Jeffrey (1825-1903) Mark Jeffery (or “Big Mark”) was an English convict who departed England on the 12th of December 1849 and arrived in Australia on the 30th of April 1850.  Mark Jeffery was described as “A terror to those in authority.  He always fought against injustice…”.

George Atkinson (convict): George Atkinson (1764 20 June 1834), also known as George Atkins, was an English convict sent to Australia aboard a ship of the First Fleet.

Bathurst rebellion: The Bathurst rebellion of 1830 was an outbreak of bushranging near Bathurst in the British colony of New South Wales, Australia, involving a group of escaped convicts who ransacked villages and engaged in shootouts between October and November of that year.  Led by 25-year-old English convict Ralph Entwistle, the group, known as the Ribon Gang, numbered up to 130 men at its peak, making it the largest convict uprising in New South Wales history since the Castle Hill convict rebellion of 1804.

William Sykes (convict): William Sykes (  1827 – 4 January 1891) was an English convict, transported to Western Australia for manslaughter.

Strandloper (novel): Strandloper is a novel by English writer Alan Garner, published in 1996.  It is loosely based on the story of a Cheshire labourer, William Buckley.  The historical figures of Edward Stanley and John Batman also appear as characters in the novel.

Solomon Blay: Solomon Blay (20 January 1816 – 20 August 1897) was an English convict transported to the Australian penal colony of Van Diemen's Land (present-day Tasmania).  Once his sentence was served, he gained notoriety as a hangman in Hobart, and is believed to have hanged over 200 people in the course of a long career spanning from 1840 to 1891.  This made him the longest serving hangman in the British Empire.

John Guard: John 'Jacky' Guard (ca. 1791/92 – 1857) was an English convict sent to Australia who was one of the first European settlers in the South Island of New Zealand, working as a whaler and trader.

Ruth Bowyer: Ruth Bowyer (c. 1761 – 5 June 1788), also known as Ruth Baldwin, was an English convict sent to Australia aboard a ship of the First Fleet.  Convicted in 1786 for the theft of five spoons from a Surrey hotel, she was sentenced to seven years transportation but died two years later and was buried beside the shore of Sydney Cove.

James Hasleby: James Hasleby (born 1833, Stamford Lincs UK; died 1903, Northampton, Western Australia), was an English convict transported to Western Australia.  He was one of only 37 convicts transported to the colony to overcome the social stigma of convictism to become schoolteachers, and one of only four convicts to be elected a member of a local Education Board.  Notably, given his previous conviction at the Old Bailey, in 1893 he was appointed Clerk of the Local Court at Northampton.

Question: Strandloper was based on the story about an English convict who was transported to what country?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "novel_title": {
      "type": "string",
      "description": "The title of the novel."
    },
    "convict_name": {
      "type": "string",
      "description": "The name of the English convict whose story the novel is based on."
    },
    "transported_country": {
      "type": "string",
      "description": "The country to which the convict was transported."
    }
  },
  "required": [
    "novel_title",
    "convict_name",
    "transported_country"
  ],
  "additionalProperties": false
}
