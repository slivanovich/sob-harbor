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
Tangled (Nick Heyward album): Tangled is the fifth solo album by English singer-songwriter Nick Heyward.  It was released in 1995 through Epic Records and produced two singles, "The World" (#47 in the UK Singles Chart and "Rollerblade" (#37 in the UK Singles Chart).

Simon Halfon: Simon Halfon is a graphic designer most noted for his work with The Jam, The Style Council, and Paul Weller.  Halfon has also worked with Oasis, Nick Heyward and George Michael, among others.  Halfon's most visible work has focused on solid inspiration from the design of the 1960s.  He has, however, displayed examples of a more current and sleek style as well.  His work on the Style Council's house music efforts was noticed by George Michael, who had Halfon apply a similar approach to his "Listen Without Prejudice" album in 1990.

North of a Miracle: North of a Miracle is the debut solo album by English singer-songwriter Nick Heyward.  It was released on 28 October 1983 through Arista Records and spent 10 weeks on the UK Albums Chart, peaking at number 10.

Les Nemes: Les Nemes (born 5 December 1960 in Croydon, England) is an English bassist.  After being in several bands with guitarist/vocalist Nick Heyward, the pair formed Haircut One Hundred in 1980.  The band enjoyed considerable success in the early 1980s and released a Top 3 album and four Top 10 singles in the UK.

Boogie Box High: Boogie Box High was a musical project headed by Andros Georgiou in the late 1980s that featured a range of collaborators, including Georgiou's cousin George Michael, guitarist Nick Heyward (of Haircut One Hundred), keyboardist Mick Talbot (of The Style Council), guitarist–songwriter David Austin, bassist Deon Estus, and others.

Nick Heyward: Nicholas "Nick" Heyward (born 20 May 1961) is an English singer-songwriter and guitarist known for being the frontman of the early 1980s band Haircut 100 and for his solo career.

Yeo Hoon-min: Yeo Hoon-min (Korean: 여훈민 ; born August 16, 1991), also known by his stage name Hoon, is a South Korean singer and actor.  He is best known as a member of South Korean boy band U-KISS under NH Media.  He joined the group in February 2011 after the departure of Alexander Lee Eusebio and Kim Kibum.  Hoon currently attends Dongguk University, majoring in theatre and film.

Haircut One Hundred: Haircut One Hundred were a British new wave/jazz-funk group formed in 1980 in Beckenham, London by Nick Heyward.  In 1981 and 1982 the band had four UK Top 10 hit singles: "Favourite Shirts (Boy Meets Girl)", "Love Plus One", "Nobody's Fool", and "Fantastic Day".

Woodland Echoes: Woodland Echoes is the seventh solo album by English singer-songwriter Nick Heyward.  It will be released on 4 August 2017 on Gladsome Hawk Records.  He has described it as accidentally biographical and influenced by "love, nature, togetherness, ‘70s’ pop, America, open spaces and afternoon tea".

From Monday to Sunday: From Monday to Sunday is the fourth solo album by English singer-songwriter Nick Heyward.  It was released in 1993 through Epic Records and produced two singles, ‘’Kite’’ (#44 in the UK Singles Chart, #4 in Billboard’s Hot Modern Rock Tracks chart) and ‘’He Doesn’t Love You Like I Do’’ (#58 in the UK Singles Chart).

Question: Was Nick Heyward a better guitarist than Yeo Hoon-min?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "nick_heyward_is_guitarist": {
      "type": "boolean",
      "description": "Indicates if Nick Heyward is identified as a guitarist in the context."
    },
    "yeo_hoon_min_is_guitarist": {
      "type": "boolean",
      "description": "Indicates if Yeo Hoon-min is identified as a guitarist in the context."
    },
    "comparison_conclusion": {
      "type": "boolean",
      "description": "The conclusion of whether Nick Heyward was a better guitarist than Yeo Hoon-min based on the context."
    },
    "reasoning": {
      "type": "string",
      "description": "Explanation for the comparison conclusion based on the roles described in the context."
    }
  },
  "required": [
    "nick_heyward_is_guitarist",
    "yeo_hoon_min_is_guitarist",
    "comparison_conclusion",
    "reasoning"
  ],
  "additionalProperties": false
}
